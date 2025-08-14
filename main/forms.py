# from django import forms

# class ContactForm(forms.Form):
#     first_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={
#         'placeholder': 'First name *',
#         'class': 'form-control'
#     }))
#     email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
#         'placeholder': 'Email *',
#         'class': 'form-control'
#     }))
#     subject = forms.CharField(max_length=200, required=False, widget=forms.TextInput(attrs={
#         'placeholder': 'Subject',
#         'class': 'form-control'
#     }))
#     message = forms.CharField(widget=forms.Textarea(attrs={
#         'placeholder': 'Message',
#         'class': 'form-control',
#         'rows': 4
#     }))


from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'email', 'subject', 'message']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First name *', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email *', 'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Subject', 'class': 'form-control'}),
            'message': forms.Textarea(attrs={'placeholder': 'Message', 'class': 'form-control', 'rows': 4}),
        }
