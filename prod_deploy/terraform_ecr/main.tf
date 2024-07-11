terraform {
    backend "s3" {
        bucket  = "terraform-egor-bot-ecr"
        encrypt = true
        key     = "terraform.tfstate"
        region  = "us-east-1"
    }
}

resource "aws_ecrpublic_repository" "egor-bot" {
  repository_name = "egor-bot"

  tags = {
    project = "egor-bot"
  }
}
