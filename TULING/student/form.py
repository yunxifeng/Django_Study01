from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField()
    email = forms.EmailField(required=False) # 设置选填
    message = forms.CharField()
