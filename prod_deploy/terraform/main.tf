terraform {
    backend "s3" {
        bucket  = "terraform-egor-bot"
        encrypt = true
        key     = "terraform.tfstate"
        region  = "us-east-1"
    }
}

module "ec2_instance_docker_compose" {
  source = "./ec2_instance_docker_compose"
  BOT_TOKEN = var.BOT_TOKEN
  engine_str = var.engine_str
  git_hub_token = var.git_hub_token
}

