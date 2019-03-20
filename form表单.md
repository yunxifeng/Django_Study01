# 关于url
HttpRequest 对象的方法和属性
属性/方法                   说明                                          示例
request.path                完整的路径，不含域名，但是包含前导斜线     “/hello/”
request.get_host()          主机名（即通常所说的“域名”）             “127.0.0.1:8000”或“www.example.com”
request.get_full_path()     包含查询字符串（如果有的话）的路径         “/hello/?print=true”
request.is_secure()         通过 HTTPS 访问时为 True，否则为 False      True 或 False
request.META                dict类,包含请求的所有HTTP首部,访问具体键时最好使用try...except
request.GET                 获取GET数据(GET数据可以来自表单,也可以来自查询字符串),数据类型:类似字典,但不是字典
request.POST                获取POST数据(POST数据一般由HTML表单提交),数据类型:类似字典,但不是字典
GET方式: 只是为了"获取数据"
POST方式:"获取数据"+"操作数据(修改,发送数据或着说显示数据之外的操作)"
# django.forms-->Django自带的表单库
主要用法:为要处理的每个HTML表单定义一个Form类
规范: 将Form放在单独的form.py文件中
- forms类的功能:
1.显示为HTML
>>> from student.forms import ContactForm
>>> f = ContactForm()
>>> print(f) # 其他输出格式: f.as_ul(), f.as.p(), f.as_table
<tr><th><label for="id_subject">Subject:</label></th><td><input id="id_subject" name="subject" type="text" /></td></tr>
<tr><th><label for="id_email">Email:</label></th><td><input id="id_email" name="email" type="email" /></td></tr>
<tr><th><label for="id_message">Message:</label></th><td><input id="id_message" name="message" type="text" /></td></tr>
>>>f['字段名'] 显示单个字段的HTML
2.验证数据
>>> f = ContactForm({"subject":"hello", "email": "xiaosuiyuan@qq.com", "message":"Nice!"}) # 关联数据
>>> f.is_bound # 验证表单是否受约束
True
>>> f.is_valid() # 验证表单数据是否有效,此案例中因设置email为选填,所以不输入email也为True,但是其他字段一旦空缺,则为False,即此表单对象无效
True
>>>f["字段名"].errors # 查看某字段的错误消息,dict类型
>>>f.cleaned_data # 有效表单的cleaned_data属性,值是dict类型,存放着"清理过的"已提交的数据,"清理",即将值转换为合适的Python类型

- 在views中使用forms对象

