from django.shortcuts import render
from .models import Topic, Comment
from django.shortcuts import get_object_or_404

# Create your views here.

def welcome_screen(request):

    topics = Topic.objects.all()
    # topic = get_object_or_404(Topic)
    count = topics.count
    comments = Comment.objects.all()
 
    context = {
        'topics': topics,
        'count': count,
        'comments': comments,
    }

    return render(request, 'discussion_forum/welcome.html', context)