variable "function_name" {}
variable "handler" {}
variable "runtime" {}
variable "filename" {}

variable "bucket_name" {
  default = "project-s3-bucket"
}

variable "bucket_acl" {
  default = "private"
}