output "iam_for_lambda_id" {
  value = aws_iam_role.iam_for_lambda.id
}

output "s3_bucket_arn" {
  value = aws_s3_bucket.s3-bucket.arn
}