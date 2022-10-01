from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets


class RecordForm(forms.Form):
    author_name = forms.CharField(max_length=200, required=True, label='Автор',
                                   widget=forms.TextInput({'class': 'form-input'}))
    text = forms.CharField(max_length=2000, required=True, label='Текст',
                                          widget=widgets.Textarea(attrs={'rows': 3, 'cols': 24}))
    author_email = forms.EmailField(max_length=2000, required=True, label='Email')

    def clean_author_name(self):
        author_name = self.cleaned_data.get('author_name')
        if len(author_name) < 2:
            raise ValidationError('Поле должно быть заполнено более чем одним символом')
        return author_name


class FindForm(forms.Form):
    author_name = forms.CharField(max_length=200, required=True, label='Автор',
                                  widget=forms.TextInput({'class': 'form-input'}))

    def clean_author_name(self):
        author_name = self.cleaned_data.get('author_name')
        if len(author_name) < 2:
            raise ValidationError('Поле должно быть заполнено более чем одним символом')
        return author_name