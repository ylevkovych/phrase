
'''
module to work with database
'''
import sys
import sqlite3

import exception_helper as excpt_hlp

def get_conn():
    '''
    get db connection
    '''
    
    conn = sqlite3.connect('/Users/yuriylevkovich/workspace/phrase/phrase.db')

    return conn


def read(query):
    '''
    read (select) db query
    '''

    conn = get_conn()
    
    try:
        cursor = conn.execute(query)
        return list(cursor.fetchall())
    except:
        excpt_hlp.prn (sys.exc_info())

    conn.close()


def write(query):
    '''
    write (insert,update) db query
    '''

    last_id = None

    conn = get_conn()
    
    try:
        cursor = conn.cursor()
        cursor.execute(query)

        last_id = cursor.lastrowid
        
        cursor.close()
        conn.commit()
    except:
        excpt_hlp.prn (sys.exc_info())

    conn.close()

    return last_id

def init_tables():
    '''
    Initialize (create) DB tables
    '''

    write ('''DROP TABLE user''')

    write ('''CREATE TABLE user (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username CHAR(50) NOT NULL UNIQUE,
        password TEXT NOT NULL,
        email TEXT NOT NULL)''')

    write ('''DROP TABLE language''')

    write ('''CREATE TABLE language (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name CHAR(50) NOT NULL UNIQUE)''')

    write ('''DROP TABLE folder''')

    write ('''CREATE TABLE folder (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name CHAR(50) NOT NULL UNIQUE)''')

    write ('''DROP TABLE translation''')

    write ('''CREATE TABLE translation (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        folder_id INTEGER,
        language_1_id INTEGER NOT NULL,
        language_2_id INTEGER NOT NULL,
        phrase_1 TEXT NOT NULL,
        phrase_2 TEXT NOT NULL)''')
