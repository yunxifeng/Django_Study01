from django.conf.urls import include, url
from django.contrib import admin
from student import views as v

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
]
