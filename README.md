# DevOps Adventure

## The goal

You and your team will start a DevOps Adventure where you will automate the development of an application. 

## Requirements
- Docker installed in your machine
- Python installed in your machine
- Github account
- Docker Hub account


## PART 1 - SETUP

### Chapter 1 - Preparing your code repo

1. You and your team needs to define a name for the team.
2. After defining the name of the team, you need to create a repository with the team name in the GitHub organization [devopsdelivery](https://github.com/devopsdelivery) following the convetion `devops-adventure-teamname`.
3. Create/edit the file `README.md` and add the team composition to the file.
4. You need to protect the branch `main` in the way that any change in this branch needs to happen thorough a Pull Request.
    - In the other words, changes to `main` branch need to be revied and approved by a different team member.

### Chapter 2 - Preparing for colaborate
1. You and your team need to define your branching strategy - your guideline of collaboration. ([GitHub Flow](https://githubflow.github.io/), [GitFlow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow), [Trunk based](https://trunkbaseddevelopment.com/)).
2. Document the branching strategy by the team in the `README` file.


## PART 2 - LOCAL DEVELOPMENT - DATABASE

### Chapter 3.1 - Database Setup - MS SQL Server

[Microsoft SQL Server](https://www.microsoft.com/en-us/sql-server/sql-server-2022) is a database server tha you will us for storing data. 

1. You will use [Microsoft SQL Server docker version](https://hub.docker.com/r/microsoft/mssql-server).
2. You should be able to execute a container of MSSQL Server on your machine (`docker run`).
3. Test the connection to the database. You can a tool like [DBeaver](https://dbeaver.io/). 
4. A new database needs to be created to store the data model. The name of the database should be `adventure-db`.


### Chapter 3.2 - Database Setup - Postgres

[Postgres](https://www.postgresql.org/) is a open source object-relational database that you can use for storing data. 

1. You should be able to execute a container of Postgres on your machine (`docker run`).
2. Test the connection to the database. You can a tool like [DBeaver](https://dbeaver.io/). 
3. A new database needs to be created to store the data model. The name of the database should be `adventure-db`.


### Chapter 4 - Data Model

1. You need to define the data model for __Users__ and __Products__:
    - The system will contain multiple `Users` (John, Jane, ...). The table Users should have (at least) the columns: ID, Name and Email.
    - The system will contain multiple `Products` (Laptop, Phone, ...). The table Products should have (at least) the columns: Id, Name and Price.
    - A user can buy multiple products and a product can be bought by multiple users.
2. The defined data model should be able to answer the question: "Which produts did the user XZY have bought so far?"

### Chapter 5 - Database Migrations

[Flyway](https://www.red-gate.com/products/flyway/) is a database migration tool that makes sure that migrations are execute according to a order and only once.  

1. You shoudl use [Flyway Docker](https://hub.docker.com/r/flyway/flyway).
2. Give it a try by runnig a Flyway container on your machine (`docker run`).
3. Now you need to create the migration scripts that will allow to define the data model. Make the migrations small as possible.
4. Flyway will be resposible to apply the migrations to the database `adventure-db`.
5. Since the database `adventure-db` needs to be running in order to Flyway apply the magrations - you should use `docker-compose` to orchestrate this two containers.    


## PART 3 - LOCAL DEVELOPMENT - APP

### Chapter 6 - Developing the application

In this part your goal is to create and dockerize a Python application that will allow:
- __Create a new user__
- __Get the list of all users__
- __Get the list of all products__
- __Get the list of products bought by a specific user__

1. To create the Python application you use [FastAPI](https://fastapi.tiangolo.com/) - a framework to build APIs with Python.
2. Create at least one unit test. You should use [Pytest](https://docs.pytest.org/en/stable/) to run the test(s).


### Chapter 7 - Dockerize the application

1. Create the `Dockerfile` for the application.
2. Update the docker compose file in order to orchestarte: database, flyway and application.


## PART 3 - PIPELINE

### Chapter 8 - Defining and implmenting the pipeline (CI)

For defining the pipeline [GitHub Actions](https://github.com/features/actions) sould be used.

1. Create your GitHub Actions worflow file: `.github/workflows/pipeline.yml`
2. Define the application pipeline:
    - Test: run the unit tests (if the tests fail the pipeline should fail)
    - Build: build the Docker image
    - Publish (upload the image to Docker Hub)
3. If the pipeline succeeds the image should be uploaded to Docker Hub using the covention: `adventure-app:tag`.


## PART 4 - DEPLOY

### Chapter 9 - Closing the loop

1. Create a docker compose that will download the created image.
2. The goal is to execute locally the entire system using the image pulled from Docker Hub.


**CONGRATULATIONS YOU REACHED THE END OF THE ADVENTURE**




