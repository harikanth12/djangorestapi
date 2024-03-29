"""withrestc4 URL Configuration

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
from testapp.views import EmployeeAPI
from testapp1.views import ExampleAPIVIEW
from rest_framework import routers
from testapp2.views import ExampleViewsets
router = routers.DefaultRouter()
router.register('test-viewset',ExampleViewsets,base_name='test-viewset')
# from testapp3.views import ExampleListapiView,ExampleCreateView,ExampleRetrieveView,ExampleupdateView,ExampledeleteView
from testapp3.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^api/',EmployeeAPI.as_view())
    # url(r'^api/',ExampleAPIVIEW.as_view())
    # url(r'^api/',include(router.urls))
    # url(r'^api/',ExampleListapiView.as_view())
    # url(r'^api/',ExampleCreateView.as_view())
    # url(r'^api/(?P<pk>\d)',ExampleRetrieveView.as_view())
    # url(r'^api/(?P<pk>\d+)',ExampleupdateView.as_view())
    # url(r'^api/(?P<pk>\d+)',ExampledeleteView.as_view())
    # url(r'^api/',ExampleListcreateView.as_view())
    # url(r'^api/(?P<pk>\d+)/$',ExampleRetrieveUpdateView.as_view())
    # url(r'^api/(?P<pk>\d+)/$',ExampleRetrieveDestoryView.as_view())
    url(r'^api/$',EmployeeListCreateView.as_view()),
    url(r'^api/(?P<pk>\d+)/$',EmployeeRetrieveDestroyView.as_view())



]
