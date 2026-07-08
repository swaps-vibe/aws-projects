provider "aws" {
    region = "ap-south-1"
  
}

resource "aws_s3_bucket" "my_bucket" {
    bucket = "swap-terraform-learning-2026"

    tags = {
      Name = "Learning bucket"
      Enviroment = "Learning"
      Owner = "swap"
    }
  
}