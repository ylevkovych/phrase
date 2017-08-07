
'''
User DAO
'''

import entity.user as user_entity
import db.db as db


def fetchall(page=None, items=None):
    sql = "SELECT id,username,password,email FROM user"

    if (page is not None and items is not None):
        sql += " limit {0}, {1}".format(str((int(page)-1)*int(items)), str(items))

    result = db.read(sql)
    
    users = []

    for r in result:
        user = _entity_from_resultset(r)

        users.append(user)
    
    return users


def fetchone(id):
    result = db.read("SELECT id,username,password,email FROM user WHERE id="+str(id))

    user = None

    for r in result:
        user=_entity_from_resultset(r)
        
        break

    return user


def fetchone_by_username(username):
    return db.read("SELECT id,username,password,email FROM user WHERE username={0}".format(username))


def create(user):
    last_id = db.write("INSERT INTO user (username,password,email) VALUES(\'{0}\',\'{1}\',\'{2}\')".format(user.username,user.password,user.email))

    user._id = last_id

    return user


def update(user):
    db.write("UPDATE user SET username=\'{0}\', password=\'{1}\', email=\'{2}\' WHERE id={3}".format(user.username,user.password,user.email,user._id))

    return user


def delete(_id):
    db.write("DELETE FROM user WHERE id={0}".format(str(_id)))

def _entity_from_resultset(r):
    user=user_entity.User()
    user._id=r[0]
    user.username=r[1]
    user.password=r[2]
    user.email=r[3]

    return user