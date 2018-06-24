from django.urls import path

from . import views

app_name = 'snippets'
urlpatterns = [
    # ex:snippets/
    # name 属性可以让你在模板 中用 {% url %} 引用避免写死
    path('', views.snippet_list, name='index'),
    # ex:snippets/5/
    path('<int:pk>/', views.snippet_detail, name='detail'),

]
