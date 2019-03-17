from django.db import models

# Create your models here.


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.EmailField()

    # 改动后,需要重启shell
    # 自定义输出内容(在shell中)(必须是字符串形式)
    # 在管理后台的修改界面显示的字段也可由此处控制
    def __str__(self):
        return self.name

    # 内嵌在Publisher类定实体中的Mate类
    # 好像没起作用...(在shell中学习models时用到的,用于排序)
    # 这里class Mate 排序的作用跟在ModelAdmin中的ordering作用是一样的
    class Mate:
        ordering = ["-name"]


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    # blank=True: 允许使用空字符串, 所有字段默认为blank=False
    # 可视化效果-->管理后台add author界面的email字段不再是粗体显示,且可选是否填充
    # 自定义管理后台界面显示的标注名称-->verbose_name="e-mail"
    email = models.EmailField(blank=True, verbose_name="e-mail")

    def __str__(self):
        return u'%s %s' %(self.first_name, self.last_name)


class Book(models.Model):
    title = models.CharField(max_length=50)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    # 对空字符串不是有效值的数据库列类型(如日期,时间和数字)[DateField,TimeField,DateTimeField,IntegerField,DecimalField,FloatField]
    # 来说,只使用blank=True留空字段(实质是插入空字符串,而数据库使用NULL表示留空),可能会报错, 所以对于这种情况需要添加null=True参数.
    # 注: 需要同时添加null=True和blank=True. 修改后执行迁移命令>>>python manage.py migrate
    publication_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title