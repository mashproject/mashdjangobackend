from django import forms


class SendMailForm(forms.Form):
    subject = forms.CharField()
    body = forms.CharField(widget=forms.Textarea)
