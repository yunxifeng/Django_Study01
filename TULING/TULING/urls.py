from django.conf.urls import include, url
from django.contrib import admin
from student import views as v

# url() 实例列表: 负责定义 URL 与处理URL 的代码之间的映射
urlpatterns = [
    # Examples:
    # url(r'^$', 'TULING.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', v.my_homepage_view),
    url(r'^hello/$', v.hello),
    url(r'^time/$', v.current_time),
    url(r'^time/plus/(\d{1,2})/$', v.hours_ahead),

    url(r'^one/$', v.one),
    url(r'^two/$', v.two),
    url(r'^three/$', v.three),
    url(r'^four/$', v.four),
    url(r'^five/$', v.five_get),
    url(r'^five_post/$', v.five_post),
    url(r'^request_meta/$', v.display_meta),
    # 版本二中,不需要search_form,直接访问search
    # url(r'^search_form$', v.search_form),
    url(r'^search/$', v.search),

    url(r'^contact/$', v.contact),
    url(r'^contact/thanks/$', v.contact_thanks),
]
