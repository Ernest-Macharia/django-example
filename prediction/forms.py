from django import forms
from django.contrib.auth.models import User
from prediction.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')

    #name = forms.CharField()
    #email = forms.EmailField()
    #text = forms.CharField(widget=forms.Textarea)
   #botcatcher = forms.CharField(required = False, widget = forms.HiddenInput)

    #def clean_botcatcher(self):
        #botcatcher = self.cleaned_data["botcatcher"]
        #if len(botcatcher) > 0:
            #raise forms.ValidationError("Gotcha Bot")
        #return botcatcher
