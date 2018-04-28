from django import forms
from .models import AmberAlertModel


class AlertForm(forms.Form):

    validation_text = forms.CharField(
        label='',
        max_length=50,
    )

    def __init__(self, *args, **kwargs):
        self.send_text = kwargs.pop('send_text')
        super(AlertForm, self).__init__(*args, **kwargs)
        self.fields['validation_text'].widget = forms.TextInput(
            attrs = {
                'placeholder': self.send_text
            }
        )

    def clean_validation_text(self):
        validation_text = self.cleaned_data['validation_text']
        # print(self.send_text)
        if validation_text != self.send_text:
            raise forms.ValidationError("Incorrect verification message!")
        return validation_text


class AmberAlertForm(forms.ModelForm):

    validation_text = forms.CharField(
        label='',
        max_length=50,
    )
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    age = forms.IntegerField(min_value=0, required=True)

    class Meta:
        model = AmberAlertModel
        fields = [
            'validation_text',
            'first_name',
            'last_name',
            'age'
        ]


    def __init__(self, *args, **kwargs):
        self.send_text = kwargs.pop('send_text')
        super(AmberAlertForm, self).__init__(*args, **kwargs)
        self.fields['validation_text'].widget = forms.TextInput(
            attrs = {
                'placeholder': self.send_text
            }
        )
        self.fields['first_name'].widget = forms.TextInput(
            attrs = {
                'placeholder': 'John'
            }
        )
        self.fields['last_name'].widget = forms.TextInput(
            attrs={
                'placeholder': 'Smith'
            }
        )
        self.fields['age'].widget = forms.TextInput(
            attrs={
                'placeholder': 25
            }
        )

    def clean_validation_text(self):
        validation_text = self.cleaned_data['validation_text']
         # print(self.send_text)
        if validation_text != self.send_text:
            raise forms.ValidationError("Incorrect verification message!")
        return validation_text



