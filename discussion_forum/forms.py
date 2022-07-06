from django.forms import ModelForm
from .models import Topic, Comment, Reply


class TopicForm(ModelForm):

    class Meta:
        model = Topic
        fields = (
            'title',)


class CommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = ('content',
                  )


class ReplyForm(ModelForm):

    class Meta:
        model = Reply
        fields = ('content',
                  )
