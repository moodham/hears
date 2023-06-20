from django import forms


class searchform(forms.Form):
    agent = forms.CharField(label="" , max_length=100,widget=forms.TextInput(attrs={'class':"email_bt" ,'placeholder':"Search", 'name':"11"  ,'value':""}))


