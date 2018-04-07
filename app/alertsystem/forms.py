from django import forms
import random as rand

class AlertForm(forms.Form):

    validation_text = forms.CharField(
        label='',
        max_length=15,
    )

    def __init__(self, *args, **kwargs):
        self.send_text = kwargs.pop('send_text')
        super(AlertForm, self).__init__(*args, **kwargs)
        self.fields['validation_text'].widget = forms.TextInput(
            attrs = {
                'placeholder': self.send_text
            }
        )



