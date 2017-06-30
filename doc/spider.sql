/*
Navicat MySQL Data Transfer

Source Server         : top
Source Server Version : 50556
Source Database       : spider

Target Server Type    : MYSQL
Target Server Version : 50556
File Encoding         : 65001

Date: 2017-06-30 14:34:39
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `dyLiveRoom`
-- ----------------------------
DROP TABLE IF EXISTS `dyLiveRoom`;
CREATE TABLE `dyLiveRoom` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `roomId` int(11) DEFAULT NULL,
  `alias` varchar(3000) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `roomId` (`roomId`) USING HASH,
  KEY `alias` (`alias`(255)) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of dyLiveRoom
-- ----------------------------
INSERT INTO `dyLiveRoom` VALUES ('1', 'yyf', '58428', '鱼鱼风,歪歪爱抚,yyf,yyfyyf,胖头鱼,y,小僵尸,rua,huh,,yyfyyfyyf,ruarua,66666,200斤,姜计就计');
INSERT INTO `dyLiveRoom` VALUES ('2', '8', '64609', '8,绿帽8,下面八,八师傅,下面师傅,下面,八路军');
INSERT INTO `dyLiveRoom` VALUES ('3', 'pis', '532152', 'p,绿帽p,小树人,报警,绿色保护着妮,pis');
INSERT INTO `dyLiveRoom` VALUES ('4', '单车', '339610', '毒奶,车长老,单车武士');
INSERT INTO `dyLiveRoom` VALUES ('5', '威海', '491416', '威海大叔');
INSERT INTO `dyLiveRoom` VALUES ('7', '820', '507882', '乌鲁鲁,820,566,八老板,小乌贼,噜噜噜,乌露露，呜呜呜，露露,倚天');
INSERT INTO `dyLiveRoom` VALUES ('25', 'zsmj', '52876', '方丈,马甲,zsmj');
INSERT INTO `dyLiveRoom` VALUES ('26', '这是哪位啊', '980511', '美女');
INSERT INTO `dyLiveRoom` VALUES ('27', '绅士', '45662', '破嘴,魔兽');
INSERT INTO `dyLiveRoom` VALUES ('28', '红叶动漫', '326183', '红叶动漫');
INSERT INTO `dyLiveRoom` VALUES ('29', '随机', '664795', '随机1');
INSERT INTO `dyLiveRoom` VALUES ('30', '随机', '66475', '随机2');
INSERT INTO `dyLiveRoom` VALUES ('31', '天使焦', '97376', '猪皇,猪,天使焦,天使宝宝,猪仔');
INSERT INTO `dyLiveRoom` VALUES ('32', '岁月', '58674', '疯了,碧霞祠,阿西吧,我都醉了');
INSERT INTO `dyLiveRoom` VALUES ('33', '岁月', '58624', 'logout,开机,关机');
INSERT INTO `dyLiveRoom` VALUES ('34', '卡卡', '55353', '卡露露,卡露露，卡卡，卡师傅,噜噜噜噜噜,良智');
INSERT INTO `dyLiveRoom` VALUES ('35', '冷冷', '20360', '喝冷水，冷冷，冷了个冷');
INSERT INTO `dyLiveRoom` VALUES ('36', '主播', '36548', 'ruyrty,bhbj');

-- ----------------------------
-- Table structure for `subscribe`
-- ----------------------------
DROP TABLE IF EXISTS `subscribe`;
CREATE TABLE `subscribe` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `status` tinyint(4) NOT NULL DEFAULT '1',
  `desc` varchar(3000) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of subscribe
-- ----------------------------
INSERT INTO `subscribe` VALUES ('1', '斗鱼直播', '1', null);

-- ----------------------------
-- Table structure for `user`
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `nick_name` varchar(300) DEFAULT NULL,
  `user_name` varchar(3000) DEFAULT NULL,
  `puid` varchar(30) DEFAULT NULL,
  `add_time` int(11) DEFAULT NULL,
  `update_time` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=128 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for `user_sub`
-- ----------------------------
DROP TABLE IF EXISTS `user_sub`;
CREATE TABLE `user_sub` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `uid` int(11) DEFAULT NULL,
  `subscribe_id` int(11) DEFAULT NULL,
  `status` tinyint(4) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;