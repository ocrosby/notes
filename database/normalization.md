# Normalization

Key
: A KEY in SQL is a value used to identify records in a table uniquely.

An SQL KEY is a single column or combination of multiple columns used to uniquely identify rows or tuples in the table.

SQL Key is used to identify duplicate information, and it also helps establish a relationship between multiple tables
in the database.

Note: Columns in a table that are NOT used to identify a record uniquely are called non-key columns.

Primary Key
: A primary key is a single column value used to identify a database record uniquely.

* A primary key cannot be NULL
* A primary key value must be unique
* The primary key values should rarely be changed
* The primary key must be given a value when a new record is inserted


Composite Key
: A composite key is a primary key composed of multiple columns used to identify a record uniquely


Foreign Key
: A foreign key is a column or group of columns in a relational database table that provides a link between data in two tables.

Foreign Key references the primary key of another Table.  It helps connect your tables.

* A foreign key can have a different name from its primary key
* It ensures rows in one table have corresponding rows in another
* Unlike the Primary key, they do not have to be unique.  Most often they aren't
* Foreign keys can be null even though primary keys can not

Transitive Functional Dependency
: A transitive functional dependency is when changing a non-key column, might cause any of the other non-key columns to change.

## First Normal Form (1NF)

* Each table cell should contain a single value
* Each record needs to be unique

## Second Normal Form (2NF)

* Be in 1NF
* Single Column Primary Key

## Third Normal Form (3NF)

* Be in 2NF
* Has no transitive functional dependencies
