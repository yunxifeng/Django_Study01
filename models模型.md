python manage.py check  --验证django项目的一系列静态检查
python manage.py sqlmigrate student 0001    --输出django即将执行的sql
python manage.py shell  --创建模型之后,Django自动创建了操作模型的高层Python API.
python manage.py makemigrations  --准备进行数据库迁移及迁移内容
python manage.py migrate  --执行数据库迁移
-  实例化模型及保存到数据库
     >>>from student.models import Publisher // 导入Publisher模型类,以便与保存出版社的数据表交互
     >>>p = Publisher(...) // 实例化
     >>>p.save() // 此种方式必须保存(实例化模型不会接触数据库,所以调用save()保存到数据库);Publisher模型还有个自增量主键id,所以调用save()方法后,会自动计算Publisher实例的主键值,
                 // 并把它赋值给实例的id属性. 后续再调用save()将就地保存记录(即update),而不新建记录
                 // 当更改实例属性再次保存后会更新所有字段,而不是只更新变化的字段   
     // 下面这种实例化的方式不需要保存
     p = Publisher.objects.create(...)
     >>>publisher_list = Publisher.objects.all() //将所有实例放入publisher_list列表中
     >>>publisher_list[0].id
     1
- 查询及检索
     >>> Publisher.objects.all() // 检索指定模型中每个记录  
                                  // objects: 管理器(负责所有"表层"数据操作,包括数据查询)
                                  // all(): 管理器的一个方法(create()也是),返回数据库中所有行,返回一个"list",实际是
                                  // 一个查询集合(QuerySet)--表示数据库中一系列行的对象
     >>>Publisher.objects.get(name="Apress") // 检索单个对象(多个对象报错, 无对象也报错),返回单个对象, 不是查询集合
                                             // DoesNotExist异常属性是模型类的属性(Publisher.DoesNotExist),可用try...except捕获
                                             // 区分大小写   
- 过滤数据
     >>> Publisher.objects.filter(name='Apress',country='U.S.A') // 可传入多个参数, 返回查询集合   
     >>> Publisher.objects.filter(name__contains='pre') // __contains: "魔法"方法,相当于sql like语句(实际上是django把pyhton
        // 语句部分转化为sql语句,操作数据库)
        // 类似方法: __icontains(不区分大小写的like), __startswith, __endswith, __range(sql between语句)
        // 上述方法好像都不区分大小写
- 排序数据
     >>> Publisher.objects.order_by("name") // 按字母表排序
                                             // ("-name"): 反向
                                             //("name", "address"): 根据多个字段排序,第一个字段排不出时使用第二个字段
                                             // 此法繁琐,可在模型models中指定默认排序   
- 链式查找--->同时执行多种操作(过滤操作和排序操作)进行查找
     >>> Publisher.objects.filter(country__contains="u").order_by("-name")     
- 切片操作--->查找固定数量的行数据
     >>> Publisher.objects.order_by("name")[0]
                                            // [0:2]
                                            // 跟列表的切片操作一样,不过不支持负数索引,可通过order_by实现相同操作
- 更新一个或多个对象的同一列数据[好像不支持这个方法了]
     // 同时解决save()方法的不足,即当只更改一列或几列数据进行保存时,会更新所有列的数据
     >>> Publisher.objects.filter(id=1).update(name="death")
                                            // id唯一确定单个实例(一行)
     >>> Publisher.objects.all().update(country="U.S.A")
                                            // 批量更改
- 删除对象
     >>> Publisher.objects.get(id=2).delete() 
                                            // 也可以批量更改
                                            // 如果要删除所有数据,必须显式调用all()方法,删除部分不用调用all()方法