# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

user_table_create = (""" CREATE TABLE IF NOT EXISTS users
(user_id int PRIMARY KEY,
first_name varchar,
last_name varchar,
gender varchar,
level varchar);
""")

song_table_create = (""" CREATE TABLE IF NOT EXISTS songs
(song_id varchar PRIMARY KEY,
title varchar,
artist_id varchar,
year int,
duration decimal);
""")

artist_table_create = (""" CREATE TABLE IF NOT EXISTS artists
(artist_id varchar PRIMARY KEY,
name varchar,
location varchar,
latitude decimal,
longitude decimal);
""")

time_table_create = (""" CREATE TABLE IF NOT EXISTS time
(start_time timestamp PRIMARY KEY,
hour int,
day int,
week int,
month int,
year int,
weekday int);
""")

songplay_table_create = (""" CREATE TABLE IF NOT EXISTS songplays
(songplay_id int PRIMARY KEY,
start_time timestamp,
user_id int,
level varchar,
song_id varchar,
artist_id varchar,
session_id int,
location varchar,
user_agent varchar,
FOREIGN KEY(start_time) REFERENCES time(start_time),
FOREIGN KEY(user_id) REFERENCES users(user_id),
FOREIGN KEY(song_id) REFERENCES songs(song_id),
FOREIGN KEY(artist_id) REFERENCES artists(artist_id));
""")

# INSERT RECORDS

songplay_table_insert = (""" INSERT INTO songplays (songplay_id,
                                                    start_time,
                                                    user_id,
                                                    level,
                                                    session_id,
                                                    location,
                                                    user_agent) \
                                                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
""")

user_table_insert = (""" INSERT INTO users (user_id, first_name, last_name, gender, level) \
    VALUES (%s, %s, %s, %s, %s)
""")

song_table_insert = (""" INSERT INTO songs (artist_id, song_id, title, duration, year) \
    VALUES (%s, %s, %s, %s, %s)
""")

artist_table_insert = (""" INSERT INTO artists (artist_id, latitude, longitude, location, name) \
    VALUES (%s, %s, %s, %s, %s)
""")


time_table_insert = (""" INSERT INTO time (start_time, hour, day, week, month, year, weekday) \
    VALUES (%s, %s, %s, %s, %s, %s, %s)
""")

# FIND SONGS

song_select = (""" SELECT * FROM songs
""")

# QUERY LISTS

create_table_queries = [
    user_table_create,
    song_table_create,
    artist_table_create,
    time_table_create,
    songplay_table_create]

drop_table_queries = [
    songplay_table_drop,
    user_table_drop,
    song_table_drop,
    artist_table_drop,
    time_table_drop]