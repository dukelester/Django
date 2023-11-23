from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Question

def index(request):
    # Get all the Questions from the databases
    questions = Question.objects.order_by('-pub_date')
    result = ' , '.join([q.question_text for q in questions])
    context = {
        'result': result,
    }
    return render(request, 'index.html', context)

def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     return Http404('The question does not exist!')
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'detail.html', { 'question': question })

def results(request, question_id):
    return HttpResponse(f'The results for the question with id : {question_id}')

def vote(request, question_id):
    return HttpResponse(f'You are voting on the question : {question_id}')
