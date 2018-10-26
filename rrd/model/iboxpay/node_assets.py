# -*- coding: utf-8 -*-


from .bean import Bean


class NodeAssets(Bean):

    @classmethod
    def query_with_project(cls, node_id):
        sql = (
            "select assets.id, assets.hostname, assets.ip, assets.public_ip, assets.port, assets.cpu_count, "
            "assets.memory, assets.location, assets.status, assets.labels, assest.comment, assets.creator, "
            "assets.created, projects.id, project.value from assets LEFT JOIN project_asset ON "
            "assets.id=project_asset.asset_id LEFT JOIN project ON project_asset.project_id=project.id "
            "LEFT JOIN node where node.id=`%s`" % node_id
        )

        return cls._db.query_all(sql)

    @classmethod
    def bind(cls, node_id, asset_id):
        pass

    @classmethod
    def unbind(cls, node_id, asset_id):
        pass




