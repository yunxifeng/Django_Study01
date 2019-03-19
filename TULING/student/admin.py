from django.contrib import admin
from .models import Publisher, Author, Book
# Register your models here.


# 定制管理后台的类
class AuthorAdmin(admin.ModelAdmin):
    # -----------关于列表修改的一些选项-------------
    # 1.list_display: 管理后台修改界面显示的字段
    list_display = ("first_name", "last_name", "email") # 元组
    # 2.添加搜索框(不区分大小写,关键字匹配下面任何一个字段都将显示出来)
    search_fields = ("first_name", "last_name")


class BookAdmin(admin.ModelAdmin):
    # -----------关于列表修改的一些选项-------------
    # 1.注: 因为Book的authors和Author是多对多属性的,所以不能添加进list_display,会报错
    list_display = ("title", "publisher", "publication_date")
    # 2.添加搜索框(不区分大小写,关键字匹配下面任何一个字段都将显示出来)
    search_fields = ("title", "authors")
    # 3.日期过滤器
    list_filter = ("publication_date",)  # 元组
    # 4.另一种日期过滤器-->日期层级导航栏
    date_hierarchy = "publication_date"  # 字符串
    # 5.默认排序, 跟models中的class Mate的ordering作用一样
    # 可视化效果: 在Publication表头出现了小箭头
    ordering = ("-publication_date",)    # 元组
    # ------------自定义编辑表单--------------------
    # 1.定制字段的排序方式(默认情况下,编辑表单中的字段顺序与模型中的定义顺序一致)
    # fields的另一个作用: 隐藏特定字段,只需要去掉特定字段即可;隐藏后编辑界面无法编辑隐藏字段,而且该字段要指定null=true
    # fields = ("title", "authors", "publisher") # 元组
    # 2.多对多关系字段->编辑界面->(由多项选择框改为JavaScript过滤器)
    # filter_vertical(纵向)的作用跟filter_horizontal(横向)一样
    filter_horizontal = ("authors",) # 元组
    # 3.外键字段(由下拉列表->文本输入框[输入id],但不便记忆,可使用放大镜图标选择)
    raw_id_fields = ("publisher",) # 元组





# 为Publisher,Author,Book三个模型在管理后台提供界面
admin.site.register(Publisher)
# 以AuthorAdmin中的选项注册Author模型.
# 注: admin.site.register()第二个参数可选,如果没有,Django使用默认选项注册模型
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)