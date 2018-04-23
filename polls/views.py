from django.shortcuts import render
from django.http import HttpResponse

from .models import Question

# Create your views here.

def index(request):
	latest_question_list = Question.objects.all
	context = {	'latest_question_list': latest_question_list}
	return render(request,'polls/index.html',context)


def detail(request,question_id):
	question = Question.objects.get(pk=question_id)
	return render(request,'polls/detail.html',{'question': question})