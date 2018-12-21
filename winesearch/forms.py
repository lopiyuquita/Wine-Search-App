from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from winesearch.models import Wine
from winesearch.models import Winery

#  I want to create a WineForm, which is based on Wine model. By using .ModelForm,
# I can "borrow" components from the Wine model to avoid redundancy.

class WineForm(forms.ModelForm):
    class Meta:
        model = Wine
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'submit'))


class WineryForm(forms.ModelForm):
    class Meta:
        model = Winery
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'submit'))
