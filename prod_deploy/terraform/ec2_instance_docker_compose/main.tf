data "aws_ami" "amazon-2" {
  most_recent = true

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-*"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }

  owners = ["099720109477"]
}

data aws_iam_policy_document "ec2_assume_role" {
  statement {
    actions = ["sts:AssumeRole"]

    principals {
      type        = "Service"
      identifiers = ["ec2.amazonaws.com"]
    }
  }
}

data aws_iam_policy_document "s3_read_access" {
  statement {
    actions = ["s3:Get*", "s3:List*"]

    resources = ["arn:aws:s3:::*"]
  }
}

resource "aws_iam_role" "ec2_iam_role" {
  name = "ec2_iam_role"

  assume_role_policy = "${data.aws_iam_policy_document.ec2_assume_role.json}"
}

resource "aws_iam_role_policy" "join_policy" {
  depends_on = [aws_iam_role.ec2_iam_role]
  name       = "join_policy"
  role       = "${aws_iam_role.ec2_iam_role.name}"

  policy = "${data.aws_iam_policy_document.s3_read_access.json}"
}

resource "aws_iam_instance_profile" "instance_profile" {
  name = "instance_profile"
  role = "${aws_iam_role.ec2_iam_role.name}"
}

resource "aws_instance" "egor_bot" {
  ami                         = data.aws_ami.amazon-2.id
  instance_type               = var.ec2_instance_type
  subnet_id                   = var.ec2_subnet_id
  vpc_security_group_ids = [var.ec2_security_group_id]
  key_name = var.ec2_key_name
  iam_instance_profile = "${aws_iam_instance_profile.instance_profile.name}"

  root_block_device {
    volume_size           = var.ec2_volume_size
    volume_type           = var.ec2_volume_type
    encrypted             = true
    delete_on_termination = true
  }
  tags = {
    Name = var.ec2_instance_name
    project = "egor-bot"
  }
  lifecycle {
      ignore_changes = [ami]
  }

user_data = <<EOF
#!/bin/bash
sudo apt-get update
sudo apt install -y apt-transport-https ca-certificates curl gnupg-agent software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt update
sudo apt install -y docker-ce

sudo curl -L "https://github.com/docker/compose/releases/download/1.23.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo apt install docker-compose
cd /home/ubuntu

git clone https://${var.git_hub_token}@github.com/dat-a-ish/egor-bot.git
cd egor-bot
printf 'BOT_TOKEN=${var.BOT_TOKEN}\nengine_str=${var.engine_str}\ngit_hub_token=${var.git_hub_token}' > prod_override.env
sudo docker compose -f prod_deploy/docker-compose.yml up -d

EOF
}