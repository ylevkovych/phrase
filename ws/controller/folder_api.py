
'''
Folder REST API
'''

import ws.controller.api_helper as api_helper
import ws.controller.controller_decorators as controller_decorators
import app as app
import dao.folder_dao as folder_dao
import entity.folder as folder_entity
import ws.service.folder as folder_service
from flask import request

@app.app.route("/rest/api/v1.0/folder", methods=["GET"])
@controller_decorators.check_auth_api
def get_folders():
    page = request.args.get("page")
    items = request.args.get("items")
    
    folders = folder_dao.fetchall(page=page, items=items)

    return api_helper.get_json_resp(folders)


@app.app.route("/rest/api/v1.0/folder/<folderId>", methods=["GET"])
@controller_decorators.check_auth_api
def get_fodler(folderId):
    folder = folder_dao.fetchone(folderId)

    if (folder is None):
        return api_helper.get_404_resp("folder not found")

    return api_helper.get_json_resp(folder)


@app.app.route("/rest/api/v1.0/folder/name/<name>", methods=["GET"])
@controller_decorators.check_auth_api
def get_fodler_by_name(name):
    folder = folder_dao.fetchone_by_name(name)

    if (folder is None):
        return api_helper.get_404_resp("folder not found")

    return api_helper.get_json_resp(folder)


@app.app.route("/rest/api/v1.0/folder", methods=["POST"])
@controller_decorators.check_auth_api
def add_folder():
    folder = folder_service.get_folder_from_data(request.data)

    if (folder == None):
        return api_helper.get_412_resp()

    if (folder_dao.fetchone_by_name(folder.name) is not None):
        return api_helper.get_412_resp("Item already exist")

    folder_dao.create(folder)

    return api_helper.get_json_resp(folder)

@app.app.route("/rest/api/v1.0/folder/<folderId>", methods=["PUT"])
@controller_decorators.check_auth_api
def update_folder(folderId):
    folder = folder_service.get_folder_from_data(request.data)

    if (folder == None):
        return api_helper.get_412_resp()

    if (folder_dao.fetchone(folderId) is None):
        return api_helper.get_404_resp("folder not found")

    folder._id = folderId

    folder_dao.update(folder)

    return api_helper.get_json_resp(folder)


@app.app.route("/rest/api/v1.0/folder/<folderId>", methods=["DELETE"])
@controller_decorators.check_auth_api
def delete_folder(folderId):
    
    if (folder_dao.fetchone(folderId) is None):
       return api_helper.get_404_resp("folder not found")

    folder_dao.delete(folderId)

    if (folder_dao.fetchone(folderId) is not None):
           return api_helper.get_412_resp("folder has not been removed")

    return api_helper.get_json_resp(True)
