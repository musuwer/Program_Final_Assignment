/*
 Navicat Premium Data Transfer

 Source Server         : MyDataBase
 Source Server Type    : MySQL
 Source Server Version : 50610
 Source Host           : localhost:3306
 Source Schema         : book

 Target Server Type    : MySQL
 Target Server Version : 50610
 File Encoding         : 65001

 Date: 15/06/2021 21:39:12
*/

USE dbchai1;  -- 指定数据库名称

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for annoucement
-- ----------------------------
DROP TABLE IF EXISTS `annoucement`;
CREATE TABLE `annoucement`  (
  `id` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `annouce_title` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `annouce_content` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `annouce_time` datetime(0) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of annoucement
-- ----------------------------
INSERT INTO `annoucement` VALUES ('f2a3e61ecd9a11eb9e909c304ef0449f', '端午节祝福', '亲爱的同学们，端午节即将到来，祝大家端午节快乐。', '2021-06-10 13:31:34');
INSERT INTO `annoucement` VALUES ('f443fbcacdde11ebbdd19c304ef0449f', '补办借书卡事宜', '需要补办借书卡的同学请于周一至周五到图书馆一楼大厅补办。', '2021-06-15 21:38:22');

-- ----------------------------
-- Table structure for book
-- ----------------------------
DROP TABLE IF EXISTS `book`;
CREATE TABLE `book`  (
  `id` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `book_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `author` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `publish_company` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `store_number` int(11) NULL DEFAULT NULL,
  `borrow_number` int(11) NULL DEFAULT NULL,
  `create_time` datetime(0) NULL DEFAULT NULL,
  `publish_date` date NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of book
-- ----------------------------
INSERT INTO `book` VALUES ('0286cb1acdb311ebbf9e9c304ef0449f', '自在独行', '贾平凹', '长江文艺出版社', 4, 1, '2021-06-15 16:23:49', '2016-06-01');
INSERT INTO `book` VALUES ('235c31a1cdb211eb968d9c304ef0449f', '老狐狸经', '山阴慧人', '延边人民出版社', 0, 1, '2021-06-15 16:17:34', '1998-11-01');
INSERT INTO `book` VALUES ('4965624dcdb211eba8099c304ef0449f', '尘埃落定', '阿来', '人民文学出版社', 4, 2, '2021-06-15 16:18:38', '1998-03-01');
INSERT INTO `book` VALUES ('9623fe85cdb111ebb9df9c304ef0449f', '海边的卡夫卡', '村上春树', '上海译文出版社', 4, 1, '2021-06-15 16:13:37', '2007-07-01');
INSERT INTO `book` VALUES ('9cdbf8e1cdb211ebb2259c304ef0449f', '万历十五年', '黄仁宇', '中华书局', 8, 0, '2021-06-15 16:20:58', '1982-05-01');
INSERT INTO `book` VALUES ('d19b6f68cdb211eb884f9c304ef0449f', '指弹吉他独奏曲集', '董宏峰', '安徽文艺出版社', 2, 0, '2021-06-15 16:22:26', '2018-07-01');
INSERT INTO `book` VALUES ('f93b3676cdb111eba9df9c304ef0449f', '计算机基础教程', '贾长隆', '大连理工大学出版社', 0, 1, '2021-06-15 16:16:23', '1994-06-01');

-- ----------------------------
-- Table structure for borrow_info
-- ----------------------------
DROP TABLE IF EXISTS `borrow_info`;
CREATE TABLE `borrow_info`  (
  `id` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `book_id` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `book_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `borrow_user` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `borrow_num` int(11) NULL DEFAULT NULL,
  `borrow_days` int(11) NULL DEFAULT NULL,
  `borrow_time` datetime(0) NULL DEFAULT NULL,
  `return_time` datetime(0) NULL DEFAULT NULL,
  `return_flag` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of borrow_info
-- ----------------------------
INSERT INTO `borrow_info` VALUES ('090eb31ccdb811ebb6659c304ef0449f', '9623fe85cdb111ebb9df9c304ef0449f', '海边的卡夫卡', '张一', 1, 30, '2021-06-15 16:59:47', '2021-07-15 16:59:47', 0);
INSERT INTO `borrow_info` VALUES ('13118868cdde11ebbbbb9c304ef0449f', '235c31a1cdb211eb968d9c304ef0449f', '老狐狸经', '张二', 1, 5, '2021-06-15 21:32:05', '2021-06-20 21:32:05', 0);
INSERT INTO `borrow_info` VALUES ('182ba4d5cdde11eb89149c304ef0449f', 'f93b3676cdb111eba9df9c304ef0449f', '计算机基础教程', '张二', 1, 5, '2021-06-15 21:32:13', '2021-06-20 21:32:13', 1);
INSERT INTO `borrow_info` VALUES ('1f2560b6cdb811ebb6a49c304ef0449f', '4965624dcdb211eba8099c304ef0449f', '尘埃落定', '张一', 1, 20, '2021-05-01 17:00:24', '2021-05-21 17:00:24', 0);
INSERT INTO `borrow_info` VALUES ('7222993fcdde11eba0c69c304ef0449f', '0286cb1acdb311ebbf9e9c304ef0449f', '自在独行', '李四', 1, 10, '2021-06-15 21:34:44', '2021-06-25 21:34:44', 0);
INSERT INTO `borrow_info` VALUES ('a0bbcaf6cdde11ebb0c99c304ef0449f', '4965624dcdb211eba8099c304ef0449f', '尘埃落定', '李四', 1, 20, '2021-06-15 21:36:02', '2021-07-05 21:36:02', 0);

-- ----------------------------
-- Table structure for douban_book
-- ----------------------------
DROP TABLE IF EXISTS `douban_book`;
CREATE TABLE `douban_book`  (
  `img_href` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `title` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `author` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `pub` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `pub_year` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `price` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `grade` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `remark_num` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `quote` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of douban_book
-- ----------------------------

INSERT INTO `douban_book` VALUES ('https://img1.doubanio.com/view/subject/s/public/s1070959.jpg', '红楼梦', '[清] 曹雪芹 著', '人民文学出版社', '1996-12', '59.70元', '9.6', ' 335837人评价              ', '都云作者痴，谁解其中味？');
INSERT INTO `douban_book` VALUES ('https://img3.doubanio.com/view/subject/s/public/s29053580.jpg', '活着', '余华', '作家出版社', '2012-8-1', '20.00元', '9.4', ' 599086人评价              ', '生的苦难与伟大');
INSERT INTO `douban_book` VALUES ('https://img3.doubanio.com/view/subject/s/public/s27237850.jpg', '百年孤独', '[哥伦比亚] 加西亚·马尔克斯/范晔', '南海出版公司', '2011-6', '39.50元', '9.3', ' 336763人评价              ', '魔幻现实主义文学代表作');
INSERT INTO `douban_book` VALUES ('https://img1.doubanio.com/view/subject/s/public/s4371408.jpg', '1984', '[英] 乔治·奥威尔/刘绍铭', '北京十月文艺出版社', '2010-4-1', '28.00', '9.4', ' 183329人评价              ', '栗树荫下，我出卖你，你出卖我');
INSERT INTO `douban_book` VALUES ('https://img1.doubanio.com/view/subject/s/public/s1078958.jpg', '飘', '[美国] 玛格丽特·米切尔/李美华', '译林出版社', '2000-9', '40.00元', '9.3', ' 178196人评价              ', '革命时期的爱情，随风而逝');
INSERT INTO `douban_book` VALUES ('https://img9.doubanio.com/view/subject/s/public/s28357056.jpg', '三体全集', '刘慈欣', '重庆出版社', '2012-1-1', '168.00元', '9.4', ' 94966人评价              ', '地球往事三部曲');
INSERT INTO `douban_book` VALUES ('https://img2.doubanio.com/view/subject/s/public/s1076932.jpg', '三国演义（全二册）', '[明] 罗贯中', '人民文学出版社', '1998-05', '39.50元', '9.3', ' 137522人评价              ', '是非成败转头空');

-- ----------------------------
-- Table structure for message
-- ----------------------------
DROP TABLE IF EXISTS `message`;
CREATE TABLE `message`  (
  `id` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `sender_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `receiver_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `send_content` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `send_time` datetime(0) NULL DEFAULT NULL,
  `is_replied` int(11) NULL DEFAULT NULL,
  `reply_content` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `reply_time` datetime(0) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of message
-- ----------------------------
INSERT INTO `message` VALUES ('328485fccdde11eb99e59c304ef0449f', 'admin', '张一', '亲爱的张一同学，你借的书籍《张一》未还。请尽快还书，如逾期未还你的账号可能被冻结。', '2021-06-15 21:32:57', 2, NULL, NULL);
INSERT INTO `message` VALUES ('53bffc86cdb811ebbabd9c304ef0449f', '张一', 'admin', '希望能增加计算机相关藏书', '2021-06-15 17:01:52', 1, '已记录，下次采购。', '2021-06-15 21:33:23');
INSERT INTO `message` VALUES ('7e95ee12cdde11eba61c9c304ef0449f', '李四', 'admin', '我的借书卡掉了，去哪里补办呢？', '2021-06-15 21:35:05', 0, NULL, NULL);
INSERT INTO `message` VALUES ('8b9e3ab7cdde11eb9d0f9c304ef0449f', '李四', 'admin', '能不能采购《枕草子》', '2021-06-15 21:35:27', 0, NULL, NULL);

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `id` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `username` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `password` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `role` int(11) NULL DEFAULT NULL,
  `create_time` datetime(0) NULL DEFAULT NULL,
  `delete_flag` int(11) NULL DEFAULT NULL,
  `current_login_time` datetime(0) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('12644064935811ea9063d8c497639e37', 'admin', '21232f297a57a5a743894a0e4a801fc3', 0, '2020-05-11 15:23:12', 0, '2020-05-11 15:24:23');
INSERT INTO `user` VALUES ('272e7d7bc73511eba19cd7bd2780f224', '张二', 'c81e728d9d4c2f636f067f89cc14862c', 1, '2021-06-07 10:07:46', 0, '2021-06-07 10:07:46');
INSERT INTO `user` VALUES ('2b0da9f7c73911eb85dbd7bd2780f224', '李四', 'eccbc87e4b5ce2fe28308fd9f2a7baf3', 1, '2021-06-07 10:36:31', 0, '2021-06-07 10:36:31');
INSERT INTO `user` VALUES ('99477a9e935811ea8171d8c497639e37', 'zhangsan', 'e10adc3949ba59abbe56e057f20f883e', 1, '2020-05-11 15:23:12', 0, '2020-05-11 15:24:23');
INSERT INTO `user` VALUES ('c10dcd40c73411ebb832d7bd2780f224', '张一', 'c4ca4238a0b923820dcc509a6f75849b', 1, '2021-06-07 10:04:55', 0, '2021-06-07 10:04:55');

SET FOREIGN_KEY_CHECKS = 1;
