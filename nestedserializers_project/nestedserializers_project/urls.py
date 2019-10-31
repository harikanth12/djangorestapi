"""nestedserializers_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from testapp.views import *
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='This is swagger first application')

router = routers.DefaultRouter()
router.register('authorviewset',AuthorViewset)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^author-view/$',AuthorListView.as_view()),
    url(r'^author-view/(?P<pk>\d+)/$',AuthorView.as_view()),
    url(r'^book-view/$',BookListView.as_view()),
    url(r'^book-view/(?P<pk>\d+)/$',BookView.as_view()),
    url(r'^api/',authorlist.as_view()),
    url(r'^accounts/',include('django.contrib.auth.urls')),
    url(r'^thirdapi/',index),
    url(r'^',include(router.urls)),
    url(r'^doc/$',schema_view)

]
