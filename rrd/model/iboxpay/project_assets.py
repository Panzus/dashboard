# -*- coding: utf-8 -*-


from .bean import Bean


class ProjectAssets(Bean):
    _tbl = "assets"
    _cols = "id, hostname, ip, public_ip, port, cpu_cpunt, memory, status, labels, comment, creator, created"

    @classmethod
    def query_with_node(cls, project_id):
        sql = (
            "select assets.id, assets.hostname, assets.ip, assets.public_ip, assets.port, assets.cpu_count, "
            "assets.memory, assets.location, assets.status, assets.labels, assest.comment, assets.creator, "
            "assets.created, nodes.id, nodes.value from assets LEFT JOIN node_asset ON assets.id=node_asset.asset_id "
            "LEFT JOIN nodes ON node_asset.node_id=nodes.id LEFT JOIN projects where project_id=`%s`" % project_id
        )

        return cls._db.query_all(sql)

    @classmethod
    def bind(cls, project_id, asset_id):
        pass

    @classmethod
    def unbind(cls, project_id, asset_id):
        pass

