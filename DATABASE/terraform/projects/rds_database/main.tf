provider "aws" {
  region = "us-east-1"
  access_key = ""
  secret_key = ""
}

module "rds" {
  source = "../../modules/rds"
}