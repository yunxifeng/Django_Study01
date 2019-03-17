from django.shortcuts import render
from django.http import HttpResponse, Http404
import datetime
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