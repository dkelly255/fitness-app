from django.forms import ModelForm
from .models import Topic, Comment, Reply


class TopicForm(ModelForm):
    
    class Meta:
        model = Topic
        fields = "__all__"

class CommentForm(ModelForm):
    
    class Meta:
        model = Comment
        fields = ( 'content',
                  'author', )

class ReplyForm(ModelForm):
    
    class Meta:
        model = Reply
        fields = ( 'content',
                  'author', )

