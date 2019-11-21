from django.conf.urls import url
from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^add/blog', views.add_blog, name='add_blog'),
    url(r'^edit/blog/(?P<id>\d+)/$', views.edit_blog, name='edit_blog'),
    url(r'^blog/(?P<id>\d+)/$', views.blog, name='blog'),  # < 1
    path('image_upload', views.profilepic, name = 'image_upload'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)