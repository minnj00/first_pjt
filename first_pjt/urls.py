"""
URL configuration for first_pjt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from first_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('hello/', views.hello), # hello 라는 경로가 들어오면 view.hello 실행할 거야 
    path('lunch/', views.lunch),
    path('lotto/', views.lotto),
    # 어떤 변수가 들어오든 name이라는 views함수요소에 있는 변수에 담을 것
    path('greeting/<name>', views.greeting),
    path('cube/<int:num>/', views.cube), # int 를 적지 않으면 string 이라고 자동으로 인식함. 
    path('posts/', views.posts)
]
