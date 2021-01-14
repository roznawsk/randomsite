from django import forms


class PersonForm(forms.Form):
    name = forms.CharField(label='Name', max_length=30)

    def clean_name(self):
        data = self.cleaned_data['name']

        return data
