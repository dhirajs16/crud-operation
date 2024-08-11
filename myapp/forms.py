from django import forms

from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description']
        labels = {'title': 'Title', 'description': 'Description'}
        widgets = {'title': forms.TextInput(attrs={'class':'rounded-lg w-full py-2 px-4 text-black'}),
                   'description': forms.Textarea(attrs={'class':'rounded-lg w-full text-black h-[150px] py-2 px-4'})
                   }