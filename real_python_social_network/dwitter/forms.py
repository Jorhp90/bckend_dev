from django import forms
from dwitter.models import Dweet

class DweetForm(forms.ModelForm):
    """form to create a new dweet"""
    body = forms.CharField(
        required=True,
        #Textarea widget render an HTML <textarea> element, offers more space for users 2 enter text
        widget=forms.widgets.Textarea( 
        attrs={ 
            "placeholder":"Dweet smthng...", #ph will show up in the box and go away once the user clicks
            "class":"textarea is-success is-medium",}), #relates to textarea CSS rule defined by Bulma 
        label="", #removes Body text, Django default setting renders the name of a form field as its label
        )

    class Meta: #This options class allows to pass any information that isn’t a field to your form class
        model = Dweet 
        fields = ("body",)
        #exclude = ("email", ) #as touple
