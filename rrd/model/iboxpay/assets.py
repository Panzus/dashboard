# -*- coding: utf-8 -*-


from .bean import Bean


class Assets(Bean):
    _tbl = "assets"
    _cols = "id, hostname, ip, public_ip, port, cpu_cpunt, memory, status, labels, comment, creator, created"




