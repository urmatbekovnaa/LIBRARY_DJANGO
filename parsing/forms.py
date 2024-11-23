from django import forms
from . import models, parser_litnet


class ParsingForm(forms.Form):
    MEDIA_CHOICES = (
        ('litnet', 'litnet'),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)

    class Meta:
        fields = ('media_type',)

    def parser_data(self):
        if self.data['media_type'] == 'litnet':
            litnet_pars = parser_litnet.parsing()
            for i in litnet_pars:
                models.Parser.objects.create(**i)
