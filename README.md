# Data Modeling with Postgres

## The objective of this project is to build a Database and an ETL pipeline for a music application

## The Data Model used in this project is a Relational Model

### In order to install required packages type in your terminal: pip install -r requirements.txt

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
