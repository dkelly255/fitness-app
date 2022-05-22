from django.forms import ModelForm
from .models import Topic, Comment, Reply


class CreateTopic(ModelForm):
    
    class Meta:
        model = Topic
        fields = "__all__"