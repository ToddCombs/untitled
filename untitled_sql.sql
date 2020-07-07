INSERT INTO app_personinfo(`name`, `gender`, `delete`, `comment`,hbook_id) VALUES
('曹操',1,0,'字孟德',1),
('刘备',1,0,'字玄德',1),
('诸葛亮',1,0,'字孔明',1),
('孙权',1,0,'字仲谋',1),
('贾宝玉',1,0,'荣国府公子',2),
('林黛玉',0,0,'金陵十二钗之冠',2),
('薛宝钗',0,0,'薛姨妈之女',2),
('王熙凤',0,0,'贾琏之妻',2),
('贾母',0,0,'宝玉祖母',2),
('宋江',1,0,'呼保义',3),
('卢俊义',1,0,'玉麒麟',3),
('吴用',1,0,'智多星',3),
('公孙胜',1,0,'入云龙',3),
('孙悟空',1,0,'唐僧的大徒弟',4),
('唐僧',1,0,'玄奘',4),
('猪八戒',1,0,'悟能',4),
('沙僧',1,0,'沙悟净',4);

INSERT INTO app_typeinfo(tname) VALUES
('科技'),
('军事'),
('国际')


INSERT INTO app_newsinfo(ntitle, ncontent, npub_date) VALUES
('互联网科技','马云已退出阿里旗下5家公司：官方称没这个打算','2018-7-24'),
('数码产品','苹果官方科普来了：全面认识Apple ID','2018-6-23'),
('宇宙探索','平行时空、多元宇宙真的存在？令人细思极恐','2018-5-24'),
('国际军情','美国国会议员：前总统吉米·卡特请缨亲赴朝鲜','2017-11-24'),
('中国军情','中国海军万吨巨舰的起点 原型就是这艘民船','2016-5-24'),
('欧洲','欧盟高官警告：特朗普不要搞垮了世贸体系','2017-2-24'),
('美国','伊拉克北部发生汽车炸弹袭击致1死7伤','2016-5-24')

INSERT INTO app_newsinfo_ntype(newsinfo_id, typeinfo_id) VALUES
(1,1),
(3,1),
(5,1),
(4,2),
(6,2),
(2,3),
(4,3),
(6,3),
(7,3)

INSERT INTO app_areainfo VALUES
('210000', '辽宁省', NULL),
('210100', '沈阳市', '210000'),
('210102', '和平区', '210100'),
('210103', '沈河区', '210100'),
('210104', '大东区', '210100'),
('210105', '皇姑区', '210100'),
('210106', '铁西区', '210100'),
('210200', '大连市', '210000'),
('210202', '中山区', '210200'),
('210203', '西岗区', '210200'),
('210204', '沙河口区', '210200'),
('210211', '甘井子区', '210200'),
('210300', '鞍山市', '210000'),
('210302', '铁东区', '210300'),
('210303', '铁西区', '210300'),
('210304', '立山区', '210300'),
('210311', '千山区', '210300'),
('220000', '吉林省', NULL),
('220100', '长春市', '220000'),
('230000', '黑龙江省', NULL),
('230100', '哈尔滨市', '230000')

INSERT  INTO app_dept VALUES 
(10,'ACCOUNTING','NEW YORK'),
(20,'RESEARCH','DALLAS'),
(30,'SALES','CHICAGO'),
(40,'OPERATIONS','BOSTON');

INSERT INTO app_emp VALUES 
(7369,'SMITH','CLERK',7902,'1980-12-17','800.00',NULL,20),
(7499,'ALLEN','SALESMAN',7698,'1981-02-20','1600.00','300.00',30),
(7521,'WARD','SALESMAN',7698,'1981-02-22','1250.00','500.00',30),
(7566,'JONES','MANAGER',7839,'1981-04-02','2975.00',NULL,20),
(7654,'MARTIN','SALESMAN',7698,'1981-09-28','1250.00','1400.00',30),
(7698,'BLAKE','MANAGER',7839,'1981-05-01','2850.00',NULL,30),
(7782,'CLARK','MANAGER',7839,'1981-06-09','2450.00',NULL,10),
(7788,'SCOTT','ANALYST',7566,'1987-04-19','3000.00',NULL,20),
(7839,'KING','PRESIDENT',NULL,'1981-11-17','5000.00',NULL,10),
(7844,'TURNER','SALESMAN',7698,'1981-09-08','1500.00','0.00',30),
(7876,'ADAMS','CLERK',7788,'1987-05-23','1100.00',NULL,20),
(7900,'JAMES','CLERK',7698,'1981-12-03','950.00',NULL,30),
(7902,'FORD','ANALYST',7566,'1981-12-03','3000.00',NULL,20),
(7934,'MILLER','CLERK',7782,'1982-01-23','1300.00',NULL,10);

SELECT * FROM app_bookinfo WHERE title = '红楼梦'
-- 修改title字段名
UPDATE app_bookinfo SET title = '西游记' WHERE id = 4
-- 多表查询红楼梦书里有多少人物
SELECT * FROM app_bookinfo b, app_personinfo p WHERE b.id = p.hbook_id AND title = '红楼梦'
-- 多表查询名为孙悟空的人物在哪本书中
SELECT * FROM app_bookinfo b, app_personinfo p WHERE b.id = p.hbook_id AND p.name = '孙悟空'
-- 查询图书，要求图书中人物描述包含‘德’字
SELECT * FROM app_bookinfo b, app_personinfo p WHERE b.id = p.hbook_id AND p.comment LIKE ('%德%')
-- 多到多查询，3表查询
SELECT n.ntitle, n.ncontent, t.tname
FROM app_newsinfo n, app_typeinfo t, app_newsinfo_ntype nt WHERE n.id = nt.newsinfo_id AND t.id = nt.typeinfo_id
-- 自连接相关
-- 先查出所有省信息
SELECT * FROM app_areainfo WHERE aPaernt_id IS NULL
-- 查询所有市，区信息
SELECT * FROM app_areainfo WHERE aPaernt_id IS NOT NULL
-- 查询市的信息
-- 查询所有省的id
SELECT id FROM app_areainfo WHERE aPaernt_id IS NULL
-- 所有市的信息（子查询）
SELECT * FROM app_areainfo WHERE aPaernt_id IN(SELECT id FROM app_areainfo WHERE aPaernt_id IS NULL)
-- 查询所有区的信息（子查询,三层查询）
SELECT * FROM app_areainfo WHERE aPaernt_id IN
(SELECT id FROM app_areainfo WHERE aPaernt_id IN
(SELECT id FROM app_areainfo WHERE aPaernt_id IS NULL))
