from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Question, Choice
from .forms import UserRegisterForm


# Create your views here.
def index(request):
    latest_question_list = Question.objects.all()

    return render(request, 'polls/index.html',
                  {'latest_question_list':latest_question_list
                   })

def detail(request, question_id_i):
    question = get_object_or_404(Question, pk=question_id_i)
    choices_list = question.choice_set.all()

    return render(request, 'polls/detail.html', {
        'question':question,
        'choices_list':choices_list
    })

def vote(request, question_id_i):
    question = get_object_or_404(Question, pk=question_id_i)
    selected_choice = question.choice_set.get(pk=request.POST['choice'])
    selected_choice.votes += 1
    selected_choice.save()

    return HttpResponseRedirect(reverse('the_polls:results_v', args=(question.id, selected_choice.id)))

def results(request, question_id_i, choice_id_i):
    question = get_object_or_404(Question, pk=question_id_i)
    choice = get_object_or_404(Choice, pk=choice_id_i)

    return render(request, 'polls/results.html', {
        'question':question,
        'choice':choice,
    })

def summary(request):
    questions = Question.objects.all()
    return render(request, 'polls/summary.html', {
        'questions':questions
    })

def register_form(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            
            return redirect('/polls_i/')
    else:
        form = UserRegisterForm()

    return render(request, 'polls/register.html', {'form':form})
