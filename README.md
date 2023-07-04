# aws-project
AWS cloud-based project

## Projects components:

 ### MySQL RDS database 
Used to store all of application data, that is files path in S3 bucket, 
their amount of lines and their amount of words in each one of
them.

<pre>
The MySQL RDS will be made from two tables with the following structure:
Lines
  ID - a UUID string for a given file
  ObjectPath - A string showing the path of the file in S3 backet
  Date - String showing the time and date the file info is inserted into the database
  AmountOfLines - integer field describing the amount of lines in a given file
Words
  ObjectPath - A string showing the path of the file in S3 backet
  Date - String showing the time and date the file info is inserted to the database
  AmountOfWords - integer field describing the amount of words in a given file
 
</pre>
## Project Solution:
The project solution in the git repository is constructed with the following folders: \
### DATABASE
<pre>
    this folder contains terraform files and modules for creating RDS MySQL database,
    the folder should also maintain the .sql scripts for creating the database tables.
</pre>

### LINES_COUNTER
<pre>
this folder consists terraform files used to create and deploy
anything related to the lines counter application (S3 bucket and objects in it, lambda, python code,
firewall definitions and more)
</pre>