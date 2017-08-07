
import db.db as db
import entity.translation as translation_entity

def fetchall():
    result = db.read("SELECT id,user_id,folder_id,language_1_id,language_2_id,phrase_1,phrase_2")

    translations = []

    for r in result:
        translation = _entity_from_resultset(r)

        translations.append(translation)

    return translations

def fetchall_by_user(user_id):
    result = db.read("SELECT id,user_id,folder_id,language_1_id,language_2_id,phrase_1,phrase_2 WHERE user_id={0}".format(_id))

    translations = []

    for r in result:
        translation = _entity_from_resultset(r)

        translations.append(translation)

    return translations

def fetchall_by_user_by_language_1(user_id, language_1_id):
    result = db.read("SELECT id,user_id,folder_id,language_1_id,language_2_id,phrase_1,phrase_2 WHERE user_id={0} AND language_1_id={1}".format(_id,language_1_id))

    translation = None

    for r in result:
        translation = _entity_from_resultset(r)

        break

    return translation

def fetchall_by_user_by_language_2(user_id, language_2_id):
    result = db.read("SELECT id,user_id,folder_id,language_1_id,language_2_id,phrase_1,phrase_2 WHERE user_id={0} AND language_2_id={1}".format(_id,language_2_id))

    translation = None

    for r in result:
        translation = _entity_from_resultset(r)

        break

    return translation

def fetchone(_id):
    result = db.read("SELECT id,user_id,folder_id,language_1_id,language_2_id,phrase_1,phrase_2 WHERE id={0}".format(_id))

    translation = None

    for r in result:
        translation = _entity_from_resultset(r)

        break

    return translation



def create(translation):
    last_id=db.write("INSERT INTO translation (user_id,folder_id,language_1_id,language_2_id,phrase_1,phrase_2) VALUES ({0}, {1}, {2}, {3}, \'{4}\', \'{5}\')".format(translation._id, translation.user, translation.folder, translation.language_1, translation.language_2, translation.phrase_1, translation.phrase_2))
    translation._id=last_id
    return translation

def update(translation):
    db.write("UPDATE translation SET user_id={0}, folder_id={1}, language_1_id={2}, language_2_id={3}, phrase_1=\'{4}\', phrase_2=\'{5}\' WHERE id={6}".format(translation._id, translation.user, translation.folder, translation.language_1, translation.language_2, translation.phrase_1, translation.phrase_2, translation._id))

    return translation

def delete(_id):
    db.write("DELETE FROM translation WHERE id={0}".format(_id))

def _entity_from_resultset(r):
    translation = translation_entity.Translation()
    translation._id=r[0]
    translation.user=r[1]
    translation.folder=r[2]
    translation.language_1=r[3]
    translation.language_2=r[4]
    translation.phrase_1=r[5]
    translation.phrase_2=r[6]

    return translation