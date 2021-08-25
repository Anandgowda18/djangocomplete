from django import forms
from django.core.exceptions import ValidationError
from django.forms.widgets import PasswordInput, Select

class UserRegistrationForm(forms.Form):
    GENDER = [('male','MALE'),('female','FEMALE')]
    firstname=forms.CharField()
    lastname=forms.CharField(required=False)
    email=forms.CharField()
    gender = forms.CharField(widget=Select(choices=GENDER))
    password = forms.CharField(widget=PasswordInput)
    ssn = forms.IntegerField()
    
    '''def clean_firstname(self):
        inputfirstname = self.cleaned_data['firstname']
        if len(inputfirstname)>20:
            raise forms.ValidationError(f'The maximum length for sirst name allowed is 20 char but you entered {len(inputfirstname)}')
        return inputfirstname

    def clean_email(self):
        inputemail = self.cleaned_data['email']
        if inputemail.find('@') == -1:
            raise forms.ValidationError('you entered wrong email')
        return inputemail'''
    
    def clean(self):
        user_data = super().clean()
        inputfirstname = user_data['firstname']
        if len(inputfirstname) > 20:
            raise forms.ValidationError(f'The maximum length for sirst name allowed is 20 char but you entered {len(inputfirstname)}')

        inputemail = user_data['email']
        if inputemail.find('@') == -1:
            raise forms.ValidationError('you entered wrong email')
        
        inputlastname = user_data['lastname']
        if len(inputlastname) == 0:
            raise forms.ValidationError('your last name is so good, dont skip it')