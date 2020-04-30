from django import forms


class RegistrationForm(forms.Form):
    nom = forms.CharField(max_length=100)
    prenom = forms.CharField(widget=forms.Textarea)
    envoyeur = forms.EmailField(label="Votre adresse e-mail")
    renvoi = forms.BooleanField(help_text="Cochez si vous souhaitez obtenir une copie du mail envoyé.", required=False)