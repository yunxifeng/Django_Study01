- views
1.视图就是普通的 Python 函数，它的第一个参数是 HttpRequest 对象，返回值是一个HttpResponse 实例。
- url
1.URL 配置相当于 Django 驱动的网站的目录。简单来说，URL 配置把 URL 映射到相应的视图函数上。
2.从 django.conf.urls 模块中导入两个函数：include，用于导入另一个 URL 配置模块；url，使
用正则表达式模式匹配浏览器中的 URL，把它映射到 Django 项目中的某个模块上。
3.从 django.contrib 模块中导入 admin 函数。这个函数传给 include 函数，加载 Django 管理后台
的 URL。
4.如果指定的 URL 模式要求有末尾的斜线，请求时没有斜线(应该是/hello/,却输入/hello),Django 会把它重定向到末尾带斜线的 URL。
（这个行为由 Django 的 APPEND_SLASH 设置管理.)
5. URL 配置，以对象的形式传入 hello 视图函数，而没有调用函数.Python（以及其他动态语言）的一个关键特性：
函数是一等对象，可以像其他变量那样传递
