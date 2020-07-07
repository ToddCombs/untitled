from datetime import date

from django.db.models import F, Q, Sum, Avg
from django.http import HttpResponse
from django.shortcuts import render
from app.models import BookInfo, PersonInfo


# Create your views here.
def index(request):
    """入口函数"""
    # return HttpResponse('<h1>Hellooooooooo World!</h1>')
    # 查询函数：get。查询图书类中的第一条记录
    # # ORM会转换下面语句发给数据库，相当于select * from XXX where id=1
    # book = BookInfo.bookm.get(id=1)
    # print(type(book))
    # print(book.id, book.btitle, book.bpub_date, book.bread, book.bcomment)
    # # str转换字符串类型
    # ret = str(book.id)+', '+book.btitle+', '+str(book.bpub_date)+', '+str(book.bread)+', '+str(book.bcomment)
    # # 返回数据库查询结果到页面，工作中不常用该方法


    # 查询人物类中的第四条记录，python现成的东西很多，查询数据库不用写sql语句，直接ORM去数据库里完成，JAVA则需要写sql语句
    # person = PersonInfo.bookm.get(id=4)
    # ret = str(person.id)+', '+str(person.pname)+', '+str(person.pgender)+', '+str(person.pcomment)

    # 查询函数all,以“查询集”形式返回所有数据表中的记录，该操作不会立即执行
    # 只有使用了查询集中的数据时才会被执行，想访问数据则需要循环
    # books = BookInfo.bookm.all()
    # print(type(books[0]))  # 查看查询集中的第一个元素
    # # 循环输出查询集中的数据
    # ret = ''
    # for book in books:
    #     ret += str(book.id)+', '+book.btitle+', '+str(book.bpub_date)+', '+str(book.bread)+', '+str(book.bcomment)
    #     ret += '<br>'

    # 查询书名为红楼梦的记录,filter方法返回数据库的查询集，get方法返回单个结果
    # book = BookInfo.bookm.filter(btitle__exact='红楼梦')

    # 查询书名中包含“传”的记录
    # book = BookInfo.bookm.filter(btitle__contains='传')  # 映射为 like (%传%)

    # 查询书名以“梦”结尾的记录
    # book = BookInfo.bookm.filter(btitle__endswith='梦')  # 映射为 like (%梦%)

    # 查询阅读量不为空的记录
    # book = BookInfo.bookm.filter(bread__isnull=False)

    # 查询图书编号为1，3的记录，映射为id in(1,3)
    # book = BookInfo.bookm.filter(id__in=[1, 3])

    # 查询图书编号大于3的记录
    # book = BookInfo.bookm.filter(id__gt=3)  # 映射为id>3

    # 查询1985年1月1日后出版的书
    # book = BookInfo.bookm.filter(bpub_date__gt=date(1985, 1, 1))  # 映射为bpub_date>1985-01-01

    # 查询1980年出版的书
    # book = BookInfo.bookm.filter(bpub_date__year=1980)

    # ret = str(book[0].id) + ', ' + book[0].btitle + ', ' + str(book[0].bpub_date) + ', ' + str(book[0].bread) + ', ' + str(
    #     book[0].bcomment)

    # F对象
    # 比较数据库中两个字段的值，使用F方法来比较两个字段，得到的结果集需要for循环输出
    # books = BookInfo.bookm.filter(bread__gte=F('bcomment'))
    # 比较阅读数大于评论数2倍的条目
    # books = BookInfo.bookm.filter(bread__gt=F('bcomment') * 2)

    # Q对象
    # 查询阅读量大于20，并且编号小于3的图书方法1：
    # books = BookInfo.bookm.filter(bread__gt=20, id__lt=3)
    # 查询阅读量大于20，并且编号小于3的图书方法2： &表示‘与’的关系
    # books = BookInfo.bookm.filter(Q(bread__gt=20) & Q(id__lt=3))
    # 查询阅读量大于20，或者编号小于3的图书方法： | 表示‘或’的关系
    # books = BookInfo.bookm.filter(Q(bread__gt=20) | Q(id__lt=3))
    # ret = ''
    # for book in books:
    #     ret += str(book.id) + ', ' + book.btitle + ', ' + str(book.bpub_date) + ', ' + str(book.bread) + ', ' + str(
    #     book.bcomment)
    #     ret += '<br>'

    # 查询阅读总量，使用聚合函数
    # num = BookInfo.bookm.aggregate(Sum('bread'))
    # ret = num['bread__sum']

    # 查询评论数的平均值
    # num = BookInfo.bookm.aggregate(Avg('bcomment'))
    # ret = num['bcomment__avg']

    # 查询图书表中总共有多少图书
    # ret = BookInfo.bookm.count()

    # 通过对象多表查询需要两步：第一步获得图书类对象，第二步根据图书类对象调用集合查询所有函数
    # 查询书名为三国演义的图书对象，又称作：一到多查询
    # book = BookInfo.bookm.get(btitle='红楼梦')
    # # 通过获得图书对象来获得人物对象
    # person = book.personinfo_set.all()
    # ret = ''
    # for p in person:
    #     ret += str(p.pname) + ', ' + p.pcomment + ', ' + str(p.hbook_id)
    #     ret += '<br>'
    
    # 通过对象多表查询名称叫孙悟空的人物在哪本书里：获得名字为孙悟空的人物对象，然后通过获得的人物对象id，去查询对应的图书
    # person = PersonInfo.bookm.get(pname='曹操')
    # book = person.hbook
    # ret = book.btitle

    # 查询图书，要求图书中人物名包含‘吴’字
    # person = PersonInfo.bookm.get(pname__contains='吴')
    # book = person.hbook
    # ret = book.btitle

    # 使用模型类查询：一类模型类名.bookm.filter(小写多类模型类名__属性名__条件运算符 = 值）
    # books = BookInfo.bookm.filter(personinfo__pcomment__contains='德')
    # ret = ''
    # for book in books:
    #     ret += str(book.id) + ', ' + book.btitle + ', ' + str(book.bpub_date) + ', ' + str(book.bread)
    #     ret += '<br>'

    # 通过模型类多表查询，查询西游记中所有人物
    # person = PersonInfo.bookm.filter(hbook__btitle__exact='西游记')
    # ret = ''
    # for p in person:
    #     ret += str(p.pname) + ', ' + str(p.pcomment) + ', ' + str(p.hbook_id)
    #     ret += '<br>'

    # 查询出所有人物，重写all方法相关
    # book = BookInfo.bookm.all()
    book = BookInfo.bookm.all()  # 默认查询会使用bookm,定义了管理器类后，要使用管理器对象来查询

    ret = ''
    for b in book:
        ret += b.btitle + ', '

    return HttpResponse(ret)


    # return render(request, 'app/index.html')  # 路径从templates下一层开始写

def personal(request):
    """个人页面"""
    return HttpResponse('<h1>This is my personal page</h1>')

def login(request):
    """扒了简书的登录页，未包含css内容"""
    return render(request, 'app/login.html')


def cure(request):
    """将天龙八部插入到图书表中"""
    book = BookInfo()
    book.btitle = '天龙八部'
    book.bpub_date = '2020-07-06'
    book.save()  # ORM框架会将save()函数映射insert到数据库

    return HttpResponse('创建完成')

def alter(request):
    """修改红楼梦的日期到今天"""
    book = BookInfo.bookm.get(btitle='红楼梦')  # get方法找出数据库中记录
    book.bpub_date = '2020-07-06'
    book.save()  # ORM会将save映射为update
    return HttpResponse('修改完成')

def update(request):
    """在PersonInfo表中加入新对象，django需要已对象形式插入外键表数据"""
    p = PersonInfo()
    p.pname = '郭靖'
    p.pcomment = '降龙十八掌'
    p.pgender = True
    b = BookInfo.bookm.get(btitle='天龙八部')
    p.hbook = b  # 对于多表中的外键不能直接赋值id，需要赋值为对象
    p.save()
    return HttpResponse('插入完成')

def delete(request):
    """删除对象"""
    p = PersonInfo.bookm.get(pname='公孙胜')
    p.delete()
    return HttpResponse('删除完成')

def addb(request):
    """调用添加书籍功能"""
    BookInfo.bookm.add_book('人工智能', '2020-07-07')
    return HttpResponse('添加完成')
