from django.contrib import admin

# Register your models here.
from app.models import BookInfo, PersonInfo

# 自定义管理类，以字段方式显示数据表
class BookInfoAdmin(admin.ModelAdmin):
    # 字段名虽然在models.py中重命名，但这里参数依然要写models里定义的字段名
    list_display = ['id', 'btitle', 'bpub_date', 'bread', 'bcomment', 'isDelete']

class PersonInfoAdmin(admin.ModelAdmin):
    # 字段名虽然在models.py中重命名，但这里参数依然要写models里定义的字段名
    list_display = ['id', 'pname', 'pgender', 'isDelete', 'pcomment']

admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(PersonInfo, PersonInfoAdmin)