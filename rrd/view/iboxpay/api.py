# -*- coding: utf-8 -*-


from rrd import app
from flask import request, jsonify, render_template
from rrd.store import db
from rrd.model.iboxpay.assets import Assets
from rrd import corelib, config


@app.route("/api/iboxpay/assets/<int:asset_id>")
def api_assets_get(asset_id):
    asset_id = int(asset_id)
    asset = Assets.get(asset_id)
    if not asset:
        return jsonify(msg='no such asset')

    return jsonify(msg='', data=asset.to_json())


@app.route("/api/iboxpay/nodes/<int:node_id>")
def api_assets_get(node_id):
    node_id = int(node_id)
    node = Assets.get(node_id)
    if not node:
        return jsonify(msg='no such asset')

    return jsonify(msg='', data=node.to_json())


@app.route("/api/iboxpay/projects/<int:project_id>")
def api_assets_get(project_id):
    project_id = int(project_id)
    project= Assets.get(project_id)
    if not project:
        return jsonify(msg='no such project')

    return jsonify(msg='', data=project.to_json())