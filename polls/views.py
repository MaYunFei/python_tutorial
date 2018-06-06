from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.template import loader

from polls.models import Question


def index(request):
    # 最近的五条数据
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    #################### 0 简单的回复文本

    ## 循环字符连接
    # output = ','.join(q.question_text for q in latest_question_list)
    # return HttpResponse(output)

    ##################### 1 回复模板

    # template = loader.get_template('polls/index.html')
    # # context 要返回的数据集
    # context = {
    #     'latest_question_list': latest_question_list,
    # }
    # return HttpResponse(template.render(context, request))

    ##################### 2 快捷函数返回模板
    context = {'latest_question_list':latest_question_list}
    return render(request,'polls/index.html',context)


def detail(request, question_id):
    # 0
    # return HttpResponse("You're loking at question %s." % question_id)
    # 1
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # render(request,'polls/detail.html',{'question':question})
    # 2
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/detail.html',{'question':question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
