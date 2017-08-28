'''
User settings dao
'''

import db.db as db
import entity.user_settings as user_settings_entity

def fetch_one_by_user_id(userId):

    user_settings = None

    sql = "SELECT id,user_id,role_id,language_1_id,language_2_id FROM user_settings WHERE user_id={0}".format(userId)
    
    result = db.read(sql)
    print (result)
    for r in result:
        user_settings = _entity_from_resultset(r)

        break

    return user_settings


def create(user_settings):
    
    sql = "INSERT INTO user_settings (user_id,role_id,language_1_id,language_2_id) VALUES (\'{0}\',\'{1}\',\'{2}\',\'{3}\') ".format(user_settings.userId, user_settings.roleId, user_settings.language1Id, user_settings.language2Id)

    last_id = db.write(sql)

    user_settings._id = last_id
    
    return user_settings


def update(user_settings):
    sql = "UPDATE user_settings SET user_id=\'{0}\', role_id=\'{1}\', language_1_id=\'{2}\', language_2_id\'{3}\' ".format(user_settings.userId, user_settings.roleId, user_settings.language1Id, user_settings.language2Id)

    db.write(sql)

    return user_settings


def delete(userSettingsId):
    sql = "DELETE FROM user_settings WHERE id={0}".format(userSettingsId)

    db.write(sql)

    return True


def _entity_from_resultset(r):
    
    if len(r) < 5:
        return None

    user_settings = user_settings_entity.UserSettings()
    user_settings._id = r[0]
    user_settings.userId = r[1]
    user_settings.roleId = r[2]
    user_settings.language1Id = r[3]
    user_settings.language2Id = r[4]

    return user_settings