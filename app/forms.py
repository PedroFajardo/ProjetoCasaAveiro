from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

class thingInsert(forms.Form):
    name = forms.CharField(label="Nome:", max_length=30)
    quantity = forms.CharField(label="Quantidade:", max_length="2")
    categorias = (
        ("Fruta","Fruta"),
        ("Frigorifico","Frigorifico"),
        ("Arca", "Arca"),
        ("Dispensa","Dispensa"),
        ("WC", "Casa de Banho")
    ) 
    category = forms.ChoiceField(label="Categoria:", choices=categorias)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-6 col-sm-6 col-xs-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('quantity', css_class='form-group col-md-6 col-sm-6 col-xs-6 mb-0'),
                css_class='form-row'
            ),
            'category',
            Submit('submit', 'Adicionar')
        )