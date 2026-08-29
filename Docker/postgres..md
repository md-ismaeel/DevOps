# PostgreSQL with Docker

This guide explains how to download PostgreSQL from Docker Hub, run it locally using Docker, connect to PostgreSQL, and execute SQL queries.

## Prerequisites

Make sure Docker is installed and working.

Check Docker:

```bash
docker --version
```

Test Docker:

```bash
docker run hello-world
```

---

# 1. PostgreSQL Docker Image

We will use the official PostgreSQL image from Docker Hub.

Docker Hub:

https://hub.docker.com/_/postgres

The official image provides PostgreSQL and supports running a PostgreSQL instance using `docker run`.

---

# 2. Pull PostgreSQL Image

Pull the PostgreSQL image:

```bash
docker pull postgres
```

This downloads the image from Docker Hub to your local machine.

You can also specify a particular version/tag:

```bash
docker pull postgres:18
```

Check downloaded images:

```bash
docker images
```

Example:

```text
REPOSITORY   TAG       IMAGE ID       CREATED       SIZE
postgres     18        xxxxxxxxxxxx   ...           ...
```

Docker uses `latest` when no tag is specified.

---

# 3. Run PostgreSQL Container

Run PostgreSQL:

```bash
docker run -d \
  --name my-postgres \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=mysecretpassword \
  -e POSTGRES_DB=mydb \
  -p 5432:5432 \
  postgres
```

## Understanding the command

### `docker run`

Creates and starts a new container from an image.

```text
docker run IMAGE
```

### `-d`

Runs the container in detached/background mode.

```text
-d = detached
```

### `--name`

Gives the container a name:

```bash
--name my-postgres
```

We can then use:

```bash
docker stop my-postgres
docker start my-postgres
docker logs my-postgres
```

### `-e`

Sets environment variables inside the container.

```bash
-e POSTGRES_USER=postgres
-e POSTGRES_PASSWORD=mysecretpassword
-e POSTGRES_DB=mydb
```

These variables are used by the PostgreSQL image during initialization. The official image requires `POSTGRES_PASSWORD` for this basic setup.

### `-p`

Maps the host port to the container port:

```bash
-p 5432:5432
```

Meaning:

```text
Your computer                 Container
     │                            │
     │ localhost:5432             │
     └───────────────────────────>│ 5432
                                  │
                              PostgreSQL
```

### `postgres`

This is the Docker image that will be used to create the container.

---

# 4. Check Running Container

Run:

```bash
docker ps
```

Example:

```text
CONTAINER ID   IMAGE      COMMAND                  PORTS
xxxxxxxx       postgres   "docker-entrypoint..."   0.0.0.0:5432->5432/tcp
```

If you want to see all containers, including stopped containers:

```bash
docker ps -a
```

---

# 5. Check PostgreSQL Logs

Run:

```bash
docker logs my-postgres
```

You should eventually see something similar to:

```text
database system is ready to accept connections
```

This means PostgreSQL is ready.

---

# 6. Connect to PostgreSQL

You can use `psql` directly inside the running container.

Run:

```bash
docker exec -it my-postgres psql -U postgres -d mydb
```

Explanation:

```text
docker exec
    ↓
execute a command inside a running container

-it
    ↓
interactive terminal

my-postgres
    ↓
container name

psql
    ↓
PostgreSQL command-line client

-U postgres
    ↓
PostgreSQL username

-d mydb
    ↓
database name
```

You should now see:

```text
mydb=#
```

You are now inside PostgreSQL.

---

# 7. Check PostgreSQL Version

Inside `psql`:

```sql
SELECT version();
```

---

# 8. List Databases

```sql
\l
```

You should see databases including:

```text
mydb
postgres
template0
template1
```

---

# 9. Check Current Database

```sql
SELECT current_database();
```

Expected:

```text
 mydb
```

---

# 10. Create a Table

Run:

```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(150)
);
```

---

# 11. Check Tables

Run:

```sql
\dt
```

You should see:

```text
 public | users | table | postgres
```

---

# 12. Insert Data

Insert some records:

```sql
INSERT INTO users (name, email)
VALUES
    ('Rajesh', 'rajesh@example.com'),
    ('Santosh', 'santosh@example.com'),
    ('Vishal', 'vishal@example.com');
```

---

# 13. Query Data

Run:

```sql
SELECT * FROM users;
```

Example result:

```text
 id |  name   |        email
----+---------+----------------------
  1 | Rajesh  | rajesh@example.com
  2 | Santosh | santosh@example.com
  3 | Vishal  | vishal@example.com
```

---

# 14. Query Specific Data

Find one user:

```sql
SELECT *
FROM users
WHERE id = 2;
```

Find users by name:

```sql
SELECT *
FROM users
WHERE name = 'Rajesh';
```

Select only names:

```sql
SELECT name
FROM users;
```

---

# 15. Update Data

```sql
UPDATE users
SET email = 'newemail@example.com'
WHERE id = 1;
```

Check:

```sql
SELECT * FROM users;
```

---

# 16. Delete Data

```sql
DELETE FROM users
WHERE id = 3;
```

Check:

```sql
SELECT * FROM users;
```

---

# 17. Exit PostgreSQL

Inside `psql`:

```sql
\q
```

You will return to your Ubuntu terminal.

---

# 18. Stop PostgreSQL

To stop the container:

```bash
docker stop my-postgres
```

Check:

```bash
docker ps
```

The container should no longer appear in the running-container list.

---

# 19. Start PostgreSQL Again

The container still exists.

Start it:

```bash
docker start my-postgres
```

Check:

```bash
docker ps
```

Then connect again:

```bash
docker exec -it my-postgres psql -U postgres -d mydb
```

Your data is available again.

---

# 20. Remove the Container

If you want to completely remove the container:

First stop it:

```bash
docker stop my-postgres
```

Then remove it:

```bash
docker rm my-postgres
```

Check:

```bash
docker ps -a
```

---

# 21. Remove the PostgreSQL Image

To remove the image:

```bash
docker rmi postgres
```

Check:

```bash
docker images
```

---

# 22. Important: Persist PostgreSQL Data

For development, it is recommended to use a Docker volume so PostgreSQL data is stored separately from the container.

Create a volume:

```bash
docker volume create postgres-data
```

Check:

```bash
docker volume ls
```

Run PostgreSQL using the volume:

```bash
docker run -d \
  --name my-postgres \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=mysecretpassword \
  -e POSTGRES_DB=mydb \
  -p 5432:5432 \
  -v postgres-data:/var/lib/postgresql/data \
  postgres
```

The important part is:

```bash
-v postgres-data:/var/lib/postgresql/data
```

This maps the Docker volume to PostgreSQL's data directory.

The flow becomes:

```text
PostgreSQL
     │
     ▼
Container
     │
     ▼
/var/lib/postgresql/data
     │
     ▼
Docker Volume
     │
     ▼
postgres-data
```

Now removing the container does not automatically remove the named volume.

---

# 23. Connect from Your Local Machine

Because we mapped:

```bash
-p 5432:5432
```

applications running on your computer can connect using:

```text
Host:     localhost
Port:     5432
Database: mydb
Username: postgres
Password: mysecretpassword
```

For example, a PostgreSQL connection URL can be:

```text
postgresql://postgres:mysecretpassword@localhost:5432/mydb
```

---

# 24. Connect Using psql Installed on Ubuntu

If `psql` is installed on Ubuntu, you can connect without using `docker exec`:

```bash
psql -h localhost -p 5432 -U postgres -d mydb
```

It will ask for the password:

```text
mysecretpassword
```

Then you can run:

```sql
SELECT * FROM users;
```

---

# 25. Complete Docker Flow

The complete workflow is:

```text
Docker Hub
    │
    │ docker pull postgres
    ▼
Local Docker Image
    │
    │ docker run
    ▼
PostgreSQL Container
    │
    ├── PostgreSQL
    │
    ├── Port 5432
    │
    └── Database: mydb
            │
            ▼
         psql
            │
            ├── CREATE TABLE
            ├── INSERT
            ├── SELECT
            ├── UPDATE
            └── DELETE
```

---

# 26. Quick Reference

## Pull image

```bash
docker pull postgres
```

## List images

```bash
docker images
```

## Run PostgreSQL

```bash
docker run -d \
  --name my-postgres \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=mysecretpassword \
  -e POSTGRES_DB=mydb \
  -p 5432:5432 \
  postgres
```

## Check container

```bash
docker ps
```

## View logs

```bash
docker logs my-postgres
```

## Connect to PostgreSQL

```bash
docker exec -it my-postgres psql -U postgres -d mydb
```

## Stop

```bash
docker stop my-postgres
```

## Start

```bash
docker start my-postgres
```

## Remove container

```bash
docker rm my-postgres
```

## Remove image

```bash
docker rmi postgres
```

## Create volume

```bash
docker volume create postgres-data
```

## List volumes

```bash
docker volume ls
```

---

# 27. Useful SQL Commands

Inside `psql`:

```sql
\l
```

List databases.

```sql
\dt
```

List tables.

```sql
\d users
```

Show table structure.

```sql
SELECT current_database();
```

Show current database.

```sql
SELECT version();
```

Show PostgreSQL version.

```sql
\q
```

Exit `psql`.

---

# 28. Final Example

The shortest complete setup is:

```bash
# Pull PostgreSQL
docker pull postgres

# Create and start PostgreSQL
docker run -d \
  --name my-postgres \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=mysecretpassword \
  -e POSTGRES_DB=mydb \
  -p 5432:5432 \
  -v postgres-data:/var/lib/postgresql/data \
  postgres

# Check container
docker ps

# Connect to PostgreSQL
docker exec -it my-postgres psql -U postgres -d mydb
```

Then inside PostgreSQL:

```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(150)
);

INSERT INTO users (name, email)
VALUES ('Rajesh', 'rajesh@example.com');

SELECT * FROM users;
```

That's the complete **Docker Hub → pull → local PostgreSQL container → connect → SQL query** workflow.
