from django.urls import path

from . import views

app_name = 'login'
urlpatterns = [
    # ex:polls/
    # name 属性可以让你在模板 中用 {% url %} 引用避免写死
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),

]
