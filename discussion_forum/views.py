from django.shortcuts import render
from .models import Topic

# Create your views here.

def welcome_screen(request):

    topics = Topic.objects.all()
    count = topics.count
    comments=[]
 
    context = {
        'topics': topics,
        'count': count,
        'comments': comments,
    }

    return render(request, 'discussion_forum/welcome.html', context)