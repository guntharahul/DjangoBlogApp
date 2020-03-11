from django.shortcuts import render
from personal.models import Question
# Create your views here.
def home_screen_view(request):
    context={   }
    # context['some_string']='this is some string passing to view.'
    questions= Question.objects.all()
    context['questions']=questions
    return render(request,"personal/home.html",context)
