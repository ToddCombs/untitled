from django.db import models

# Create your models here.每一个模型类只能有一个主键，django自动设定
# class Demo(models.Model):
#     name = models.CharField(max_length=20)
#     age = models.IntegerField()
class BookInfoManager(models.Manager):
    def all(self):
        """注意：自定义管理器和系统提供的object管理器只允许留一个。
        重写all方法，返回所有没有删除标记的记录。
        定义图书类的管理器,super是调用父类的方法，在父类查询的结果集上进行修改"""
        return super().all().filter(isDelete=False)

    def add_book(self, bookname, pubdate):
        """封装添加书籍功能"""
        book = BookInfo()
        book.btitle = bookname
        book.bpub_date = pubdate
        book.save()

class BookInfo(models.Model):
    # db_column是指定列名，如不指定则在数据库中创建出的表字段名就等于变量名
    btitle = models.CharField(max_length=20, db_column='title')

    bpub_date = models.DateField(db_column='pub_date')  # 图书发布日期
    bread = models.IntegerField(default=0, db_column='read')  # 阅读量
    bcomment = models.IntegerField(default=0, db_column='comment')   # 评论量
    # 逻辑删除，相当于要删除一条记录，删错了，需要恢复，先做个标志，代表该数据有可能删除，如果反悔了，只要去掉标志就行
    isDelete = models.BooleanField(default=False, db_column='delete')
    # 重写all方法相关，创建管理器类的对象
    bookm = BookInfoManager()  # 自定义了管理器，系统将不再产生objects管理器

class PersonInfo(models.Model):

    pname = models.CharField(max_length=20, db_column='name')   # 人物姓名
    pgender = models.BooleanField(default=True, db_column='gender')  # 人物性别
    isDelete = models.BooleanField(default=False, db_column='delete')  # 逻辑删除
    # 人物描述，null=True是非空约束，代表数据库中字段可为空。blank=True表示你的表单填写该字段的时候可以不填，反之为False则表示后台管理页面的输入框不能为空
    pcomment = models.CharField(max_length=200, null=True, blank=False, db_column='comment')
    # 关联图书类的外键， 由于BookInfo里只有一个主键则会自动关联

    hbook = models.ForeignKey('BookInfo', on_delete=models.CASCADE)

# 多对多查询新闻类型
class TypeInfo(models.Model):
    tname = models.CharField(max_length=20)  # 新闻类别

# 新闻
class NewsInfo(models.Model):
    ntitle = models.CharField(max_length=60)  # 新闻标题
    ncontent = models.TextField()  # 新闻内容
    npub_date = models.DateTimeField(auto_created=True)  # 新闻发布的时间
    # 通过ManyToManyField建立TypeInfo类和NewsInfo类之间多对多的关系
    # 定义多对多关系可以写在任何一个类中
    ntype = models.ManyToManyField('TypeInfo')

# 自连接相关
class AreaInfo(models.Model):
    atitle = models.CharField(max_length=30)  # 地区名称
    # 上级地区
    aPaernt = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

class Emp(models.Model):
    # primary_key 设置主键
    empno = models.IntegerField(max_length=4, primary_key=True)
    ename = models.CharField(max_length=10)
    job = models.CharField(max_length=9)
    mgr = models.IntegerField(max_length=4, null=True)
    hiredate = models.DateField()
    # DecimalField 浮点数，一般用于金额，max_digits是总位数，decimal_places是小数位
    sal = models.DecimalField(max_digits=7, decimal_places=2)
    comm = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    # 设置外键
    deptno = models.ForeignKey('Dept', on_delete=models.CASCADE)

class Dept(models.Model):
    deptno = models.IntegerField(max_length=2, primary_key=True)
    dname = models.CharField(max_length=14)
    loc = models.CharField(max_length=13)