# Data Modeling with Postgres

<img src = 'https://www.postgresql.org/media/img/about/press/elephant.png' height = 300 width = 300 />

## The objective of this project is to build a Database and an ETL pipeline for a music application

## The Data Model used in this project is a Relational Model

### In order to install required packages type the following command in your terminal

> pip install -r requirements.txt

#### ***Note: You should first the run create.py script at least once before other scipts as they depend on the created Database***

### The steps taken to build this project

- Creating schema for the Database tables.

- Writing CREATE statements in regards to the schema created above.

- Writing INSERT statements to write data into the Database.

### Database Tables in the project

- songplay table -> Fact table (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)

- users table -> Dimention Table (user_id, first_name, last_name, gender, level)

- time table -> Dimention Table (start_time, hour, day, week, month, year, weekday)

- artists table -> Dimention Table (artist_id, name, location, latitude, longitude)

- songs table -> Dimention Table (song_id, title, artist_id, year, duration)

### Files of the project

- create_tables.py -> Creates tables of database, drops tables of database if they exist.

- sql_queries.py -> Contains all SQL queries to CREATE, INSERT or SELECT.

- etl.py -> Extracts data from json files, Transforms data to fit Database schema, and Loads the data to its location in the Database.
