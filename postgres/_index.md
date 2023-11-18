# PostgreSQL

A PostgreSQL instance is called a cluster because a single instance can serve and handle multiple databases.  Every
database is an isolated space where users and applications can store data.

A database is accessed by allowed users, but users connected to a database cannot cross the database boundaries and
interact with data contained in another database, unless they are explicitly connected ot the latter database as well.

A database can be organized into namespaces, called schemas.  A schema is a mnemonic name that the user can assign to
organize database objects, such as tables, into a more structured collection.  Schemas cannot be nested, so they
represent a flat namespace.

Database objects are represented by everything the user can create and manage within the database -- for instance,
tables, functions, triggers, and data types.  Every object belongs to one and only one schema that, if not specified, is
the default public schema.

Users are defined at a cluster-wide level, which means they are not tied to a particular database in the cluster.  A
user can connect with and manage any database in the cluster they have been allowed to.

PostgreSQL splits users into two main categories:

* Normal users: These users are the ones who can connect to and handle databases and objects depending on their privilege set.
* Superusers: These users can do anything with any database object.

PostgreSQL allows the configuration of as many superusers as you need, and every superuser has the very same permission:
they can do everything with every database and object and, most notably, can also control the life cycle of the cluster
(for instance, they can terminate normal uer connection, reload the configuration, top the whole cluster, and on).

PostgreSQL internal data, such as users, databases, namespaces, configuration, and database runtime status, is provided
by means of catalogs: special tables that present information in a SQL-interactive way.  Many catalogs are trimmed
depending on the user who is inspecting them, except superusers usually see the whole set of available
information.

The PGDATA directory represents what the cluster is serving as databases.

Internally, PostgreSQL, keeps track of the tables structures, indexes, functions, and all the stuff needed to manage
the cluster in dedicated storage named the catalog.  The catalog is fundamental for the life cycle of the cluster and
reflects pretty much every action the database does on the user's structures and data.  PostgreSQL provides access to
the catalog from database superusers by means of an SQL interface, which means the catalog is totally explorable and,
to some extent, manipulable, via SQL statements.

The SQL standard defines a so-called information schema, a collection of tables common to all standard database 
implementations including PostgreSQL, that the DBA can use to inspect hte internal status of the database itself.  For
instance, the information schema defines a table that collects information about all the user-defined tables so that 
it is possible to query the information schema to see whether a specific table exists or not.

The PostgreSQL catalog is what some call an "information schema on steroids": the catalog is much more accurate and 
PostgreSQL-specific than the general information schema, and the DBA can extract a lot more information about the 
PostgreSQL status from the catalog.  

When the cluster is started, PostgreSQL launches a single process called the post-master.  The aim of the postmaster is
to wait for incoming client connections, often made over a TCP/IP connection, and fork another process named the backend
process, which in turn is in charge of serving one and only one connection.

This means that every time a new connection against the cluster is opened, the cluster reacts by launching a new 
backend process to serve it until the connection ends and the process is, consequently, destroyed.  The postmaster
usually starts also some utility processes that are responsible to keep PostgreSQL in good shape while running.

To summarize, PostgreSQL provides you with executables that can be installed wherever you want on your system and can 
serve a single cluster.  The cluster, in turn, serves data out of a single PGDATA directory that contains, among other
stuff, the user data, the cluster internal status and the WALs.  Every time a client connects to the server, the 
postmaster process forks a new backend process that is the minion in charge of serving the connection.

Cluster:
:   the whole PostgreSQL service

Postmaster:
:   the first process the cluster executes, and this process is responsible for keeping track of the activities of the
    whole cluster.  The postmaster forks itself into a backend process every time a new connection is established.

Database:
:   an isolated data container which users (or applications) can connect to.  A cluster cna handle multiple databases.  
    A database can be made by different objects, including schemas (namespaces), tables, triggers, and other data
    objects you will see later.

PGDATA:
:   the name of the directory that, on persistent storage, is fully dedicated to PostgreSQL and its data.  PostgreSQL
    stores the data within such a directory.

WALs:
:   contains the intent log of database changes, used to recover data from a critical crash.


## Getting to Know Your Cluster

The psql client ships with PostgreSQL and is the recommended way to connect to your database. The main free graphical
client available for PostgreSQL is pgAdmin4, but you can choose the one you like the most.

PostgreSQL is a service that can be started, stopped, and of course monitored.

PostgreSQL ships with a tool called `pg_ctl` that helps in managing the cluster and the related running processes.

### pg_ctl

The pg_ctl command-line utility is a tool that allows you to perform different actions on a cluster, mainly 
initialize it, start it, restart and stop it, and so on. pg_ctl accepts the command to execute as the first argument
followed by other specific arguments -- the main commands are as follows:

- start, stop, and restart execute the corresponding actions on the cluster.
- status reports the current status (running or not) of the cluster.
- initdb (or init for short) executes the initialization of the cluster, possibly removing any previously existing data.
- reload causes the PostgreSQL server to reload the configuration, which is useful when you want to apply configuration changes.
- promote is used when the cluster is running as a subordinate server (named standby) in a replication setup and, from
  now on, must be detached from the original master and become independent.


Setting up the PGDATA directory is the first step to start using PostgreSQL.

I added this to my .zshrc file:

```shell
export PGDATA=/usr/local/var/postgres
```

Since the directory didn't exist I needed to create it.

when I created it I was given the message that it is not a database cluster directory.

So I deleted the PGDATA directory and ran the initdb command to initialize the cluster.

```shell
initdb -D $PGDATA
```

After doing all this and searching for a process id file I found that the PGDATA directory
was set to 

/usr/local/var/postgresql@14

when I installed PostgreSQL via homebrew

Once I set the PGDATA environment variable correctly to that the `pg_ctl status` command worked as expected,
telling me the server was running.

### The psql command-line client

The psql command is the command-line interface that ships with every installation of PostgreSQL.  A basic knowledge of
psql is mandatory in order to administer the cluster.  The client is lightweight and useful even in emergency situations
when a GUI is not available.  psql accepts several options to connect to a database, mainly the following:

- -d: The database name
- -U: The username
- -h: The host (either an IPv4 or IPv6 address or a hostname)

If no option is specified, psql assumes your operating system user is trying to connect to a database with the same 
name, and a database user user with a name that matches the operating system on a local connection.

so the command `psql` will connect to the database with the same name as the operating system user and the database

in my case it will try to connect to a local database named omarcrosby with a user named omarcrosby by default so I 
get an error because that database doesn't exist.

I can specify the database name with the -d option like so:

```shell
psql -d datacamp_courses
```

Also note that you can utilize the id command to get your current id

```shell
id
```

