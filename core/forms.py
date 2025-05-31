from django import forms
from django.utils.translation import gettext_lazy as _
from .models import User

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label=_('Password'), widget=forms.PasswordInput)
    password2 = forms.CharField(label=_('Repeat password'), widget=forms.PasswordInput)
    role = forms.ChoiceField(label=_('Role'), choices=User.Roles.choices)
    department = forms.ModelChoiceField(
        queryset=None, label=_('Department'), required=False
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'role', 'department')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        from .models import Department
        self.fields['department'].queryset = Department.objects.all()

    def clean_password2(self):
        cd = self.cleaned_data
        if cd.get('password') != cd.get('password2'):
            raise forms.ValidationError(_('Passwords do not match.'))
        return cd.get('password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user