from django.shortcuts import render, redirect
from .models import Topic, Comment, Reply
from .forms import CreateTopic
from django.shortcuts import get_object_or_404

# Create your views here.

def welcome_screen(request):

    topics = Topic.objects.all()
    count = topics.count
    comments = Comment.objects.all()
    replies = Reply.objects.all()
 
    context = {
        'topics': topics,
        'count': count,
        'comments': comments,
        'replies': replies,
    }

    return render(request, 'discussion_forum/welcome.html', context)


def create_topic(request):

    form = CreateTopic()

    if request.method == 'POST':
        form = CreateTopic(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}

    return render(request, 'discussion_forum/create_topic.html', context)