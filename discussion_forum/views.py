from django.shortcuts import render, redirect
from .models import Topic, Comment, Reply
from .forms import TopicForm, CommentForm
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

    form = TopicForm()

    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('discussion_forum')

    context = {'form': form}

    return render(request, 'discussion_forum/create_topic.html', context)


def edit_topic(request, topic_id):
    
    topic = get_object_or_404(Topic, id=topic_id)
    
    if request.method == 'POST':
        form = TopicForm(request.POST, instance=topic)
        if form.is_valid():
            form.save()
            return redirect('discussion_forum')
    
    form = TopicForm(instance=topic)
    
    context = {
        'form': form
    }
    
    return render(request, 'discussion_forum/edit_topic.html', context)    


def delete_topic(request, topic_id):

    topic = get_object_or_404(Topic, id=topic_id)
    topic.delete()
    
    return redirect('discussion_forum')


def add_comment(request, topic_id):

    form = CommentForm()
    topic = Topic.objects.get(pk=topic_id)
    

    if request.method == 'POST':
        
        
        form = CommentForm(request.POST)
        form.instance.topic = topic
        if form.is_valid():
            form.save()
            return redirect('discussion_forum')

    context = {
        'form': form,
        'topic': topic,
        }

    return render(request, 'discussion_forum/add_comment.html', context)