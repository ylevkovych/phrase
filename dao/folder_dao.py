
import db.db as db
import entity.folder as folder_entity

def fetchall(page=None, items=None):
    sql = " SELECT id,name FROM folder "

    if (page is not None and items is not None):
        sql += " LIMIT {0},{1}".format(str((int(page)-1)*int(items)), str(items))

    result = db.read(sql)

    folders = []

    for r in result:
        folder=_entity_from_resultset(r)

        folders.append(folder)

    return folders

def fetchone(_id):
    result = db.read("SELECT id,name FROM folder WHERE id={0}".format(_id))

    folder = None

    for r in result:
        folder=_entity_from_resultset(r)

        break

    return folder

def fetchone_by_name(name):
    result = db.read("SELECT id,name FROM folder WHERE name=\'{0}\'".format(name))

    folder = None

    for r in result:
        folder=_entity_from_resultset(r)

        break

    return folder

def create(folder):
    last_id=db.write("INSERT INTO folder (name) VALUES (\'{0}\')".format(folder.name))
    folder._id=last_id
    return folder

def update(folder):
    db.write("UPDATE folder SET name=\'{0}\' WHERE id={1}".format(folder.name, folder._id))

    return folder

def delete(_id):
    db.write("DELETE FROM folder WHERE id={0}".format(_id))

def _entity_from_resultset(r):
    if len(r) < 2:
        return None

    folder=folder_entity.Folder()
    folder._id=r[0]
    folder.name=r[1]

    return folder