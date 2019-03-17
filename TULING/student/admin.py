from django.contrib import admin
from .models import Publisher, Author, Book
# Register your models here.


# 定制管理后台的类
class AuthorAdmin(admin.ModelAdmin):
    # -----------关于列表修改的一些选项-------------
    # list_display: 管理后台修改界面显示的字段
    list_display = ("first_name", "last_name", "email") # 元组
    # 添加搜索框(不区分大小写,关键字匹配下面任何一个字段都将显示出来)
    search_fields = ("first_name", "last_name")
    # ------------自定义编辑表单--------------------


class BookAdmin(admin.ModelAdmin):
    # -----------关于列表修改的一些选项-------------
    # 注: 因为Book的authors和Author是多对多属性的,所以不能添加进list_display,会报错
    list_display = ("title", "publisher", "publication_date")
    # 添加搜索框(不区分大小写,关键字匹配下面任何一个字段都将显示出来)
    search_fields = ("title", "authors")
    # 日期过滤器
    list_filter = ("publication_date",)  # 元组
    # 另一种日期过滤器-->日期层级导航栏
    date_hierarchy = "publication_date"  # 字符串
    # 默认排序, 跟models中的class Mate的ordering作用一样
    # 可视化效果: 在Publication表头出现了小箭头
    ordering = ("-publication_date",)    # 元组
    # ------------自定义编辑表单--------------------
    # 定制字段的排序方式(默认情况下,编辑表单中的字段顺序与模型中的定义顺序一致)
    # fields = ("title", "authors", "publisher")
    filter_horizontal = ("authors",) # 元组


# 为Publisher,Author,Book三个模型在管理后台提供界面
admin.site.register(Publisher)
# 以AuthorAdmin中的选项注册Author模型.
# 注: admin.site.register()第二个参数可选,如果没有,Django使用默认选项注册模型
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)