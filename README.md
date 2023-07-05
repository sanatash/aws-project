# aws-project
AWS cloud-based project

## Projects components:

 ### MySQL RDS database 
Used to store all of application data which is files path in S3 bucket and 
their amount of lines in each of them

<pre>
The MySQL RDS will be made from FilesLines table with the following structure:

  ID - a UUID string for a given file
  ObjectPath - A string showing the path of the file in S3 backet
  Date - String showing the time and date the file info is inserted into the database
  AmountOfLines - integer field describing the amount of lines in a given file
</pre>

 ### Lines Counter 
An event driven system that counts the amount of lines in an S3 bucket
objects and stores it into a MySQL RDS table.
The lines counter is an application that is made of an AWS Lambda written in python which it’s
purpose is upon a new file event in S3 bucket it will download that file, will count it’s lines and will save
the amount of lines into a MySQL RDS table called “FilesLines”.

## Project Solution:
The project solution in the git repository is constructed from the following folders:
### DATABASE
<pre>
This folder contains terraform files and modules for creating RDS MySQL database.
sql/ - the folder maintains the .sql scripts for creating the database tables.
terraform/modules/rds - module for creating MySql RDS database in AWS
terraform/projects/rds_database - this terraform project is provisioning AWS RDS database
</pre>

### LINES_COUNTER
<pre>
This folder consists terraform files and python code used to create and deploy
anything related to the lines counter application
terraform/modules/lines-counter - module for deploying anything related to lines counter application in
AWS (s3 bucket and its objects, iam role for lambda function, lambda function, s3 as trigger for lambda)
terraform/projects/lines_counter
terraform/projects/lines_counter - terraform project which deploys MySql rds, S3 bucket, S3 objects, lambda function into AWS
test/  - python test files which test lambda function and MySql RDS database table.

</pre>