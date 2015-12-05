from django import forms


class SendMailForm(forms.Form):
    subject = forms.CharField(required=False)
