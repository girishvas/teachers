from .models import *
from django.forms import ModelForm
from django import forms


class TeacherForm(ModelForm):

    class Meta:
        model = Teacher
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(TeacherForm, self).__init__(*args, **kwargs)
        for key, field in self.fields.items():
            if isinstance(field.widget, forms.TextInput) or \
                isinstance(field.widget, forms.Textarea) or \
                isinstance(field.widget, forms.EmailInput) or \
                isinstance(field.widget, forms.DateInput) or \
                isinstance(field.widget, forms.DateTimeInput) or \
                isinstance(field.widget, forms.TimeInput):
                field.widget.attrs.update({'placeholder': field.label})
    