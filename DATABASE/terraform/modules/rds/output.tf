# Output the RDS endpoint
output "rds_endpoint" {
  value = module.rds_db_instance.db_instance_endpoint
}