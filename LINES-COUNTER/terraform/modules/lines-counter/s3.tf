# aws s3 terraform resource documentation:
# https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/s3_bucket
# updated security defaults for new S3 buckets:
# https://github.com/hashicorp/terraform-provider-aws/issues/28353

resource "aws_s3_bucket" "s3-bucket" {
  bucket = var.bucket_name
  acl    = var.bucket_acl
  versioning {
    enabled = true
  }
}