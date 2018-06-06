from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    # ex:polls/
    # name 属性可以让你在模板 中用 {% url %} 引用避免写死
    path('', views.index, name='index'),
    # ex:polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),

]
