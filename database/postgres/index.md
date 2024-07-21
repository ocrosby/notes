# PostgreSQL

PostgreSQL is a powerful, open source object-relational database system. It has more than 15 years of active development and a proven architecture that has earned it a strong reputation for reliability, data integrity, and correctness. It runs on all major operating systems, including Linux, UNIX (AIX, BSD, HP-UX, SGI IRIX, Mac OS X, Solaris, Tru64), and Windows. It is fully ACID compliant, has full support for foreign keys, joins, views, triggers, and stored procedures (in multiple languages). It includes most SQL:2008 data types, including INTEGER, NUMERIC, BOOLEAN, CHAR, VARCHAR, DATE, INTERVAL, and TIMESTAMP. It also supports storage of binary large objects, including pictures, sounds, or video. It has native programming interfaces for C/C++, Java, .Net, Perl, Python, Ruby, Tcl, ODBC, among others, and exceptional documentation.

## Docker Image

The official PostgreSQL Docker image is available on Docker Hub. You can pull the image with the following command:

```Shell
docker pull postgres
```

To run a PostgreSQL container, use the following command:

```Shell
docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -d postgres
```

This command will create a new PostgreSQL container with the name `some-postgres` and the password `mysecretpassword`.

## References

- [PostgreSQL](https://www.postgresql.org)
- [PostgreSQL Docker Image](https://hub.docker.com/_/postgres)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [PostgreSQL Tutorial](https://www.postgresqltutorial.com)
- [PostgreSQL Exercises](https://pgexercises.com)
