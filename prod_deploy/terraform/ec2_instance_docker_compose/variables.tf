variable "ec2_instance_name" {
  description = "Name for the EC2 instance"
  default = "egor-bot"
}

variable "ec2_instance_type" {
  description = "EC2 instance type"
  default = "t2.small"
}

variable "ec2_subnet_id" {
  description = "EC2 subnet id"
  default = "subnet-07907faf989588ec9"
}

variable "ec2_key_name" {
  default = "data_il"
}

variable "ec2_security_group_id" {
  default = "sg-0408dd8c9be253bd1"
}

variable "ec2_volume_size" {
  default = "8"
}

variable "ec2_volume_type" {
  default = "gp2"
}

variable "BOT_TOKEN" {}
variable "engine_str" {}
variable "git_hub_token" {}