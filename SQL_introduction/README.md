# SQL - Introduction

## Description

This project is an introduction to Databases and SQL, using MySQL 8.0 on Ubuntu 22.04 LTS.
It covers the basics of relational databases, how to create and manage databases and tables,
and how to perform basic SQL queries such as SELECT, INSERT, UPDATE, and DELETE.

## Learning Objectives

At the end of this project, I am able to explain the following without the help of Google:

- What's a database
- What's a relational database
- What does SQL stand for
- What's MySQL
- How to create a database in MySQL
- What does DDL and DML stand for
- How to CREATE or ALTER a table
- How to SELECT data from a table
- How to INSERT, UPDATE or DELETE data
- What are subqueries
- How to use MySQL functions

## Requirements

- All files are executed on Ubuntu 22.04 LTS using MySQL 8.0 (version 8.0.25)
- All files end with a new line
- All SQL queries have a comment just before them
- All files start with a comment describing the task
- All SQL keywords are in uppercase (SELECT, WHERE, etc.)
- The length of files is tested using `wc`

## How to run a script

```bash
cat my_script.sql | mysql -hlocalhost -uroot -p
```

## Tasks

| Task | File | Description |
| ---- | ---- | ----------- |
| 0 | `0-list_databases.sql` | Lists all databases of the MySQL server |
| 1 | `1-create_database.sql` | Creates the database `hbtn_0c_0` if it doesn't already exist |
| 2 | `2-remove_database.sql` | Deletes the database `hbtn_0c_0` if it exists |
| 3 | `3-list_tables.sql` | Lists all tables of the database `hbtn_0c_0` in MySQL server |
| 4 | `4-first_table.sql` | Creates a table `first_table` with columns `id` and `name` |
| 5 | `5-full_table.sql` | Prints the full description of the table `first_table` |

## Author
Rahaf Alabdalh 
