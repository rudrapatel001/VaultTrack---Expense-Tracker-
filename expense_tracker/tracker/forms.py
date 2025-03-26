from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Expense  

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ExpenseForm(forms.ModelForm):
    date = forms.DateField(
        required=False, 
        widget=forms.DateInput(attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d']
    )

    class Meta:
        model = Expense
        fields = ['amount', 'category','note', 'date']
        widgets = {
            'note': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write something about this expense...'}),
        }
