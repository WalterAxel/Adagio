# Dev-environment

This documents a brief explanaiton of the technology used and a step-by-step guide for setting up the dev-environment and database.

## Technology

The technology stack is stripped to the bear bones, there is no frontend framework in use and we are using minimal JavaScript libraries for the calendar view only.

Front end:
- Flask
- Python
- JavaScript
- Html
- CSS

Back end:
- Python
- SQLite

## Setting up the environment
First copy the schema.sql to database.db:
`sqlite3 database.db < schema.sql`
We are using Flask for the development environment, so starting the development environment is done with the command `flask run`
