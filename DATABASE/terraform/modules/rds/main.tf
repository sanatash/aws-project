
module "rds_db_instance" {
  source  = "registry.terraform.io/terraform-aws-modules/rds/aws//modules/db_instance"
  engine_version = "8.0"
#  version = "5.9.0"
  identifier = "mysqldb"
  instance_class = "db.t3.micro"
  engine = "mysql"
  allocated_storage = "5"
  publicly_accessible = true
  #db_subnet_group_name = ""
  db_name = var.db_name
  username = var.user_name
  password = var.user_password
  vpc_security_group_ids = [aws_security_group.rds_security_group.id]

}