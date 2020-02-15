from django.forms import ModelForm
from home.models import Todo


class TodoForm(ModelForm):
    class Meta:
        model = Todo
        include = '__all__'
