from django.shortcuts import render
from django.http import HttpResponse

from .models import Question

# Create your views here.

def index(request):
	latest_question_list = Question.objects.all
	context = {	'latest_question_list': latest_question_list}
	return render(request,'polls/index.html',context)


def detail(request,question_id):
	return HttpResponse("You are looking at question %s." % question_id)