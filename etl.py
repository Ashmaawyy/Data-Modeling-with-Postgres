import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *


def get_songs_data_from_json(filepath: str) -> pd.DataFrame:
    """
    Opens song json files and stores their data in a dataframe
    """
    # open song file
    songs_df = pd.read_json(filepath, orient = 'index')
    songs_df = songs_df.transpose()
    
    return songs_df

def load_songs_data_to_db(cur, filepath):
    
    """
    Loads logs data into two tables in the database:
    - songs table -> dimention table
    - artists table -> dimention table

    *For more details about the tables and their relations please visit the schema*
    """
    
    songs_df = get_songs_data_from_json(filepath)
    # insert song record
    song_data = songs_df.iloc[:, [1, 6, 7, 8, 9]].values.tolist()
    song_data = song_data[0]

    cur.execute(song_table_insert, song_data)
    
    # insert artist record
    artist_data = songs_df.iloc[:, [1, 2, 3, 4, 5]].values.tolist()
    artist_data = artist_data[0]
    
    cur.execute(artist_table_insert, artist_data)


def get_logs_data_from_json(filepath: str) -> pd.DataFrame:
    
    """
    Extracts the data of the logs json files and stores it in a dataframe
    """
    # open log file
    logs_df = pd.read_json(filepath, lines = True) # lines = True for trailing data Error

    return logs_df

def load_logs_data_to_db(cur, filepath):

    """
    Loads logs data into three tables in the database:
    - songplay table -> fact table
    - user table -> dimention table
    - time table -> dimention table

    *For more details about the tables and their relations please visit the schema*
    """

    logs_df = get_logs_data_from_json(filepath)
    # filter by NextSong action
    next_song_filter_df = logs_df[logs_df['page'] == 'NextSong']

    # convert timestamp column to datetime
    next_song_filter_df['ts'] = pd.to_datetime(next_song_filter_df['ts'])
    
    # insert time data records
    start_time = next_song_filter_df['ts']
    hour = next_song_filter_df['ts'].dt.hour
    day = next_song_filter_df['ts'].dt.day
    week_of_year = next_song_filter_df['ts'].dt.weekofyear
    month = next_song_filter_df['ts'].dt.month
    year = next_song_filter_df['ts'].dt.year
    weekday = next_song_filter_df['ts'].dt.weekday

    time_data = [start_time, hour, day, week_of_year, month, year, weekday]
    column_labels = ('start_time', 'hour', 'day', 'week of year', 'month', 'year', 'weekday')

    time_dict = {column_labels[i]: time_data[i] for i in range(len(column_labels))}
    time_df = pd.DataFrame.from_dict(time_dict)

    for _, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    user_df = next_song_filter_df.iloc[:, [17, 2, 5, 3, 7]]
    user_df = user_df.drop_duplicates()

    # insert user records
    for _, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    for _, row in next_song_filter_df.iterrows():
        cur.execute(song_select)
        results = cur.fetchone()
        
        if results:
            song_id, artist_id = results
        else:
            song_id, artist_id = None, None
        
        songplay_data = (row.ts, row.userId, row.level, row.sessionId, row.location, row.userAgent, song_id, artist_id)

        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):

    """
    Gets all the files in a directory and passes them to the func parameter.
    """
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        print('{}/{} files processed.'.format(i, num_files))


def main():
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()
    conn.set_session(autocommit = True)

    process_data(cur, conn, filepath = 'data/song_data', func = load_songs_data_to_db)
    process_data(cur, conn, filepath = 'data/log_data', func = load_logs_data_to_db)

    conn.close()


if __name__ == "__main__":
    main()