from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Topic, Comment, Reply
from .forms import TopicForm, CommentForm, ReplyForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required()
def welcome_screen(request):

    topics = Topic.objects.all()
    topic_count = topics.count
    comments = Comment.objects.all()
    replies = Reply.objects.all()
    total_comments = comments.count
    total_replies = replies.count
    topics = topics.order_by('date_created')    
 
    context = {
        'topics': topics,
        'topic_count': topic_count,
        'comments': comments,
        'replies': replies,
        'total_comments': total_comments,
        'total_replies': total_replies,
    }

    return render(request, 'discussion_forum/welcome.html', context)

@login_required()
def topic_detail(request, topic_id):

    current_topic = get_object_or_404(Topic, id=topic_id)
    comments = Comment.objects.filter(topic=current_topic)
    replies = Reply.objects.all()
       
 
    context = {
        'topic': current_topic,        
        'comments': comments,   
        'replies': replies,     
    }

    return render(request, 'discussion_forum/topic_detail.html', context)

def create_topic(request):

    form = TopicForm()
    user = request.user


    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.author = user
            topic.save()
            return redirect('discussion_forum')

    context = {
        'form': form,
        'user': user,
        }

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
        'form': form,
        'topic': topic,
    }
    
    return render(request, 'discussion_forum/edit_topic.html', context)    


def delete_topic(request, topic_id):

    topic = get_object_or_404(Topic, id=topic_id)
    topic.delete()
    
    return redirect('discussion_forum')


def add_comment(request, topic_id):

    form = CommentForm()
    topic = Topic.objects.get(pk=topic_id)
    user = request.user
    

    if request.method == 'POST':                
        form = CommentForm(request.POST)
        form.instance.topic = topic
        form.instance.author = user
        if form.is_valid():
            form.save()
            return redirect('discussion_forum')

    context = {
        'form': form,
        'topic': topic,
        }

    return render(request, 'discussion_forum/add_comment.html', context)


def delete_comment(request, comment_id):

    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    
    return redirect('discussion_forum')


def edit_comment(request, comment_id):
    
    comment = get_object_or_404(Comment, id=comment_id)
    
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('discussion_forum')
    
    form = CommentForm(instance=comment)
    
    context = {
        'form': form
    }
    
    return render(request, 'discussion_forum/edit_topic.html', context)


def reply_to_comment(request, comment_id):

    form = ReplyForm()
    comment = Comment.objects.get(pk=comment_id)
    user = request.user

    if request.method == 'POST':
        form = ReplyForm(request.POST)
        form.instance.comment = comment
        form.instance.author = user
        if form.is_valid():
            form.save()
            return redirect('discussion_forum')
        
    context = {
        'form': form,
        'comment': comment,
    }

    return render(request, 'discussion_forum/reply.html', context)


def delete_reply(request, reply_id):

    reply = get_object_or_404(Reply, id=reply_id)
    reply.delete()
    
    return redirect('discussion_forum')


def edit_reply(request, reply_id):
    
    reply = get_object_or_404(Reply, id=reply_id)
    
    if request.method == 'POST':
        form = ReplyForm(request.POST, instance=reply)
        if form.is_valid():
            form.save()
            return redirect('discussion_forum')
    
    form = ReplyForm(instance=reply)
    
    context = {
        'form': form
    }
    
    return render(request, 'discussion_forum/edit_topic.html', context)


def user_activity(request, author):

    profile = get_object_or_404(User, username=author)
    topics = Topic.objects.filter(author=profile)
    comments = Comment.objects.filter(author=profile)
    replies = Reply.objects.filter(author=profile) 

    context = {
        'topics': topics,
        'comments': comments,
        'replies': replies,
        'author': profile,
    }

    return render(request, 'discussion_forum/user_activity.html', context)
