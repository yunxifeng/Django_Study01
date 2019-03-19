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