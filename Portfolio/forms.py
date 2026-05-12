import re
from django import forms


class ContactForm(forms.Form):
    nom = forms.CharField(label='Nom', max_length=100)
    prenom = forms.CharField(label='Prenom', max_length=100)
    email = forms.EmailField(label='Email')
    message = forms.CharField(label='Message', widget=forms.Textarea)

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        nom = cleaned_data.get('nom')
        prenom = cleaned_data.get('prenom')
        email = cleaned_data.get('email')
        message = cleaned_data.get('message')


        if re.search('[0-9]', nom):
            raise forms.ValidationError("Le nom ou le prenom ne peuvent contenir des caracteres numeriques.")

        if "@" not in email:
            raise forms.ValidationError("Le format du mail n'est pas correcte.")

        if message == "":
            raise forms.ValidationError("Le message ne peut être vide.")

        return cleaned_data