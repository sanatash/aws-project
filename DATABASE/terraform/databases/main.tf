# Configure the AWS provider
provider "aws" {
  region = "us-east-1"
#  access_key = ""
#  secret_key = ""
}

# Terraform aws rds module path
module "rds" {
  source = "../../terraform/modules/rds"
}
