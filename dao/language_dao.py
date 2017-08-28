
import db.db as db
import entity.language as language_entity

def fetchall(page=None, items=None):
    sql = "SELECT id,name FROM language"

    if (page is not None and items is not None):
        sql += " LIMIT {0},{1}".format(str((int(page)-1)*int(items)), str(items))

    result = db.read(sql)

    languages = []

    for r in result:
        languages.append(_entity_from_resultset(r))

    return languages

def fetchone(_id):
    result = db.read("SELECT id,name FROM language WHERE id={0}".format(_id))

    language = None

    for r in result:
        language = _entity_from_resultset(r)

        break

    return language

def fetchone_by_name(name):
    result = db.read("SELECT id,name FROM language WHERE name=\'{0}\'".format(name))

    language = None

    for r in result:
        language = _entity_from_resultset(r)
        break

    return language
        

def create(language):
    last_id = db.write("INSERT INTO language (name) VALUES (\'{0}\')".format(language.name))
    language._id = last_id
    return language

def update(language):
    db.write("UPDATE language SET name=\'{0}\' WHERE id={1}".format(language.name,language._id))

    return language

def delete(_id):
    db.write("DELETE FROM language WHERE id={0}".format(_id))

def _entity_from_resultset(r):
    if len(r) < 2:
        return None

    language = language_entity.Language()
    language._id=r[0]
    language.name=r[1]

    return language