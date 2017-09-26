"""djangogirls URL Configuration

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
from django.conf.urls import url
from django.contrib import admin

from blog.views import post_list, post_detail

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', post_list),
    # 숫자 1개 이상을 검색하게 하는 정규표현식
    # 정규표현식 그룹화해서 이름을 주게 되면 뒤의 함수에 인자로 그룹의 이름을 전달한다
    url(r'^post/(?P<pk>\d+)/', post_detail)
]
