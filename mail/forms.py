from django import forms


class SendMailForm(forms.Form):
    sender = forms.CharField(required=False)
    subject = forms.CharField()
    body = forms.CharField(widget=forms.Textarea)
    format = forms.ChoiceField(choices=[('html', 'html'), ('text', 'text')])
