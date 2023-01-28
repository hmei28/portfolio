# make sure this is at the top if it isn't already
from django import forms

# our new form
class ContactForm(forms.Form):
    required_css_class = 'block mb-4 font-medium  text-3xl'
    email = forms.EmailField(label="Email", required=True, max_length=64)
    subject = forms.CharField(label="Subject", required=True, max_length=64)
    message = forms.CharField(
        label="Message",
        required=True,
        widget=forms.Textarea,
        max_length=1024
    )

    def __init__(self, *args, **kwargs):

        super(ContactForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            data_attrs = {
                # "class": " bg-stone-900 text-3xl border-x-0 border-t-0 border-green-700 w-full p-2.5 placeholder-stone-600 text-stone-300 focus:border-none focus:outline-none focus:border-stone-300",
                "class": " bg-stone-900 text-3xl w-full p-2.5 placeholder-stone-600 text-stone-300 border-x-0 border-t-0 border-green-700 focus:ring-0 focus:border-stone-300",
                "placeholder" : str(field)
            }            
            self.fields[str(field)].widget.attrs.update(data_attrs)
            #visible.field.widget.TextInput(attrs={'class': ''})