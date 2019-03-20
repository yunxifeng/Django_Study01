from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
import datetime
# 用于form简单案例
from .models import Book
# 导入forms类
from .forms import ContactForm
from django.core.mail import send_mail
# Create your views here.


def my_homepage_view(request):
    return HttpResponse()


def hello(request):
    return HttpResponse("Hello, world")

# mypage.html -- include标签
# def current_time(request):
#     ct = {
#         "title": "云汐风",
#         "current_section": "导航栏",
#     }
#     return render(request, r'mypage.html', context=ct)


# base.html --模板继承
def current_time(request):
    dt = datetime.datetime.now()
    ct = {
        "current_section": "导航栏",
        "current_date": dt,
    }
    return render(request, r'current_time.html', context=ct)


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "In {0} hours, it will be {1}".format(offset, dt)
    return HttpResponse(html)


def one(request):
    return render(request, r'one.html')


def two(request):
    ct = {"name1": "Python",
          "name2": "Java",
          }
    return render(request, r'two.html', context= ct)


def three(request):
    ct = {
        "scores": [21, 3, 4, 5, 6, 6],
    }
    return render(request, r'three.html', context=ct)


def four(request):
    ct = {
        "name": "Java",
    }
    return render(request, r'four.html', context=ct)


def five_get(request):
    return render(request, r'five.html')
def five_post(request):
    return HttpResponse("注册成功")


# request.META
def display_meta(request):
    html = []
    for k, v in request.META.items():
        html.append("<tr><td>{0}</td><td>{1}</td></tr>".format(k, v))
    return HttpResponse("<table>{0}</table>".format("\n".join(html)))


# form处理示例
# 版本一
# def search_form(request):
    # return render(request, r'search_form.html')
# def search(request):
#     if "q" in request.GET and request.GET["q"]: # 最好判断一下,不要相信用户输入的任何数据
#         q = request.GET["q"]
#         books = Book.objects.filter(title__icontains=q)
#         ct = {
#             "books": books,
#             "query": q,
#         }
#         return render(request, r'search_results.html', context=ct)
#     else:
#         return HttpResponse("Please submit a search term.")

# 版本二
def search(request):
    # error = False # 第二版
    errors = []
    if "q" in request.GET:
        q = request.GET["q"]
        if not q:
            # error = True # 第二版
            errors.append("Please enter a search term.")
        elif len(q) > 20:
            # error = True # 第二版
            errors.append("Please enter at most 20 characters.")
        else:
            books = Book.objects.filter(title__icontains=q)
            ct = {
                "books": books,
                "query": q,
            }
            return render(request, r'search_results.html', context=ct)
    return render(request, r'search_form.html', {"errors": errors})


# 第一个表单类-->Django自带的表单库django.forms
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail = (
                cd["subject"],
                cd["message"],
                cd.get("email", "noreply@example.com"),
                ["siteowner@example.com"],
            )
            return HttpResponseRedirect(r'/contact/thanks/')
    else:
        form = ContactForm(
            initial={"subject": "I love your site !"} # 设定表单中特定字段的初始值[该初始值不受任何约束]
        )
    return render(request, "contact_form.html", context={"form": form})

def contact_thanks(request):
    return HttpResponse("恭喜您,提交成功")