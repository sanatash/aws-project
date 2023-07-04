# Output the RDS endpoint
output "rds_endpoint" {
  value = module.rds_db_instance.db_instance_endpoint
}

output "rds_arn" {
  value = module.rds_db_instance.db_instance_arn
}