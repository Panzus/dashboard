CREATE  DATABASE IF NOT EXISTS iboxpay
  DEFAULT CHARACTER SET utf8
  DEFAULT COLLATE utf8_general_ci;
USE iboxpay;


DROP TABLE IF exists assets;
CREATE TABLE `assets` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `hostname` VARCHAR (32) NOT NULL UNIQUE,
  `ip` varchar(64) NOT NULL,
  `public_ip` VARCHAR(32),
  `port` int(5) default 22,
  `cpu_count` int(4),
  `memory` int(8),
  `status` VARCHAR(32),
  `labels` VARCHAR(256),
  `comment` VARCHAR(256),
  `creator` VARCHAR(64) NOT NULL,
  `created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS nodes;
CREATE TABLE `nodes` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `key` VARCHAR(32) NOT NULL UNIQUE,
  `value` VARCHAR(256) NOT NULL,
  `child_mark` int(10) NOT NULL DEFAULT 0,
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS node_asset;
CREATE TABLE 'node_asset' (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `node_id` int(10) NOT NULL,
  `asset_id` int(10) NOT NULL UNIQUE,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS projects;
CREATE TABLE `projects` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `key` VARCHAR(32) NOT NULL UNIQUE,
  `value` VARCHAR(256) NOT NULL,
  `child_mark` int(10) NOT NULL DEFAULT 0,
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS project_asset;
CREATE TABLE 'project_asset' (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `project_id` int(10) NOT NULL,
  `asset_id` int(10) NOT NULL UNIQUE,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
