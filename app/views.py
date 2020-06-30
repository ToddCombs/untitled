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
    # book = BookInfo.objects.get(id=1)
    # print(type(book))
    # print(book.id, book.btitle, book.bpub_date, book.bread, book.bcomment)
    # # str转换字符串类型
    # ret = str(book.id)+', '+book.btitle+', '+str(book.bpub_date)+', '+str(book.bread)+', '+str(book.bcomment)
    # # 返回数据库查询结果到页面，工作中不常用该方法


    # 查询人物类中的第四条记录，python现成的东西很多，查询数据库不用写sql语句，直接ORM去数据库里完成，JAVA则需要写sql语句
    # person = PersonInfo.objects.get(id=4)
    # ret = str(person.id)+', '+str(person.pname)+', '+str(person.pgender)+', '+str(person.pcomment)

    # 查询函数all,以“查询集”形式返回所有数据表中的记录，该操作不会立即执行
    # 只有使用了查询集中的数据时才会被执行，想访问数据则需要循环
    # books = BookInfo.objects.all()
    # print(type(books[0]))  # 查看查询集中的第一个元素
    # # 循环输出查询集中的数据
    # ret = ''
    # for book in books:
    #     ret += str(book.id)+', '+book.btitle+', '+str(book.bpub_date)+', '+str(book.bread)+', '+str(book.bcomment)
    #     ret += '<br>'

    # 查询书名为红楼梦的记录,filter方法返回数据库的查询集，get方法返回单个结果
    # book = BookInfo.objects.filter(btitle__exact='红楼梦')

    # 查询书名中包含“传”的记录
    # book = BookInfo.objects.filter(btitle__contains='传')  # 映射为 like (%传%)

    # 查询书名以“梦”结尾的记录
    # book = BookInfo.objects.filter(btitle__endswith='梦')  # 映射为 like (%梦%)

    # 查询阅读量不为空的记录
    # book = BookInfo.objects.filter(bread__isnull=False)

    # 查询图书编号为1，3的记录，映射为id in(1,3)
    # book = BookInfo.objects.filter(id__in=[1, 3])

    # 查询图书编号大于3的记录
    # book = BookInfo.objects.filter(id__gt=3)  # 映射为id>3

    # 查询1985年1月1日后出版的书
    # book = BookInfo.objects.filter(bpub_date__gt=date(1985, 1, 1))  # 映射为bpub_date>1985-01-01

    # 查询1980年出版的书
    # book = BookInfo.objects.filter(bpub_date__year=1980)

    # ret = str(book[0].id) + ', ' + book[0].btitle + ', ' + str(book[0].bpub_date) + ', ' + str(book[0].bread) + ', ' + str(
    #     book[0].bcomment)

    # F对象
    # 比较数据库中两个字段的值，使用F方法来比较两个字段，得到的结果集需要for循环输出
    # books = BookInfo.objects.filter(bread__gte=F('bcomment'))
    # 比较阅读数大于评论数2倍的条目
    # books = BookInfo.objects.filter(bread__gt=F('bcomment') * 2)

    # Q对象
    # 查询阅读量大于20，并且编号小于3的图书方法1：
    # books = BookInfo.objects.filter(bread__gt=20, id__lt=3)
    # 查询阅读量大于20，并且编号小于3的图书方法2： &表示‘与’的关系
    # books = BookInfo.objects.filter(Q(bread__gt=20) & Q(id__lt=3))
    # 查询阅读量大于20，或者编号小于3的图书方法： | 表示‘或’的关系
    # books = BookInfo.objects.filter(Q(bread__gt=20) | Q(id__lt=3))
    # ret = ''
    # for book in books:
    #     ret += str(book.id) + ', ' + book.btitle + ', ' + str(book.bpub_date) + ', ' + str(book.bread) + ', ' + str(
    #     book.bcomment)
    #     ret += '<br>'

    # 查询阅读总量，使用聚合函数
    # num = BookInfo.objects.aggregate(Sum('bread'))
    # ret = num['bread__sum']

    # 查询评论数的平均值
    # num = BookInfo.objects.aggregate(Avg('bcomment'))
    # ret = num['bcomment__avg']

    # 查询图书表中总共有多少图书
    ret = BookInfo.objects.count()

    return HttpResponse(ret)


    # return render(request, 'app/index1.html')  # 路径从templates下一层开始写

def personal(request):
    """个人页面"""
    return HttpResponse('<h1>This is my personal page</h1>')

def login(request):
    """扒了简书的登录页，未包含css内容"""
    return render(request, 'app/login.html')