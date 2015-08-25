CREATE TABLE `todo` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `title` char(20) NOT NULL DEFAULT '' COMMENT '主题',
  `remind` tinyint(2) unsigned NOT NULL DEFAULT '0' COMMENT '是否提醒',
  `priority` tinyint(3) NOT NULL DEFAULT '0' COMMENT '优先级',
  `deadline` datetime NOT NULL DEFAULT '1991-01-01 00:00:00',
  `status` enum('unuse', 'used', 'expired') DEFAULT 'unuse' COMMENT '验证码状态',
  `create_time` datetime NOT NULL DEFAULT '1991-01-01 00:00:00',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT='待办事项';


