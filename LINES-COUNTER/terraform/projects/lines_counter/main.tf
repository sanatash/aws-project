provider "aws" {
  region = "us-east-1"
  access_key = ""
  secret_key = ""
}

module "rds" {
  source = "../../../../DATABASE/terraform/modules/rds"
}

output "s3_bucket_arn" {
  value = "aws_s3_bucket.s3-bucket.arn"
}

# creates s3 bucket and lambda function
module "line_counter" {
  source        = "../../modules/lines-counter"
  function_name = "LinesCounter"
  bucket_name   = "lines-counter-app-s3-bucket"
  bucket_acl    = "private"
  filename      = "lines_counter.zip"
  runtime       = "python3.9"
  handler       = "lines_counter.lambda_handler"
}

locals {
  bucket_name = "lines-counter-app-s3-bucket"
  bucket_acl  = "private"
}

resource "aws_s3_object" "threelinesfiletxt" {
  bucket       = local.bucket_name
  key          = "three_lines_file.txt"
  acl          = local.bucket_acl
  source       = "files_library/three_lines_file.txt"
  content_type = "text/html"
  etag         = filemd5("files_library/three_lines_file.txt")
}

resource "aws_s3_bucket_object" "helloworldhtml" {
  bucket       = local.bucket_name
  key          = "hello-world.html"
  acl          = local.bucket_acl
  source       = "hello-world.html"
  content_type = "text/html"
  etag         = filemd5("hello-world.html")
}

resource "aws_iam_role_policy" "allow_s3_read" {
  policy = <<EOF
{
"Version": "2012-10-17",
"Statement":	[
	{
		"Sid":	"BucketAccess",
		"Effect":	"Allow",
		"Action":	"s3:ListBucket",
		"Resource":	[
		"${module.line_counter.s3_bucket_arn}"
		]
	},
	{
		"Sid":	"BucketContentsAccess",
		"Effect":	"Allow",
		"Action":	[
		"s3:GetObject"
		],
		"Resource":	[
		"${module.line_counter.s3_bucket_arn}/*"
		]
	},
    {
         "Sid": "AllowRDSDescribe",
         "Effect": "Allow",
         "Action": "rds:Describe*",
         "Resource": "*"
    },
	{
		"Sid":	"RDSInstanceAccess",
		"Effect":	"Allow",
		"Action":	[
		"rds:CreateDBTable",
		"rds:InsertItem"
		],
		"Resource":	[
		"${module.rds.rds_arn}",
		"${module.rds.rds_arn}/table/Lines"
		]
	}
]
}
EOF
  role   = module.line_counter.iam_for_lambda_id
}