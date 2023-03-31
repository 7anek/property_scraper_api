from django import forms
from properties.models import Property
from django.conf import settings
from django.conf.urls.static import static
from datetime import date

class SearchFormOld(forms.ModelForm):
    # area = forms.FloatField()
    # price = forms.FloatField()
    # number_of_rooms = forms.IntegerField()
    # description = forms.CharField()
    # floor = forms.IntegerField()
    class Meta:
        model = Property
        fields = ['area', 'price', 'number_of_rooms', 'description', 'floor']


PROPERTY_TYPE_CHOICES = [
    ('flat', 'Mieszkanie'),
    ('house', 'Dom'),
    ('plot', 'Działka'),
    ('garage', 'Garaż'),
]

PLOT_TYPE_CHOICES = [
    ('agricultural', 'Rolna'),
    ('building', 'Budowlana'),
    ('recreational', 'Rekreacyjna'),
    ('forest', 'Leśna'),
]

OFFER_TYPE_CHOICES = [
    ('sell', 'Sprzedaż'),
    ('rent', 'Wynajem'),
]

HOUSE_TYPE_CHOICES = [
    ('detached_house', 'Dom wolnostojący'),
    ('semi_detached_house', 'Bliźniak'),
    ('terraced_house', 'Szeregowiec'),
]

FLAT_TYPE_CHOICES = [
    ('block_of_flats', 'Blok'),
    ('tenement', 'Kamienica'),
    ('apartament', 'Apartamentowiec')
]

class SearchForm(forms.Form):
    # area = forms.FloatField()
    # price = forms.FloatField()
    # number_of_rooms = forms.IntegerField()
    # description = forms.CharField()
    # floor = forms.IntegerField()
    # nazwa = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Wpisz coś"}))
    # opis = forms.CharField(widget=forms.Textarea(attrs={"class": "nowa-klasa","rows":20,"cols":50,"id":"moje-id-dla-polatekstowego","placeholder":"Wpisz coś" }))
    #główne pola
    localization = forms.CharField(initial="Grodzisk Mazowiecki")
    price_min = forms.IntegerField(min_value=0, max_value=10000000, required=False, initial=300000)
    price_max = forms.IntegerField(min_value=0, max_value=10000000, required=False, initial=400000)
    area_min = forms.IntegerField(min_value=0, max_value=1000, required=False)
    area_max = forms.IntegerField(min_value=0, max_value=1000, required=False)
    property_type = forms.ChoiceField(choices=PROPERTY_TYPE_CHOICES, required=False)
    offer_type = forms.ChoiceField(choices=OFFER_TYPE_CHOICES, required=False)
    #dodatkowe pola
    plot_type = forms.ChoiceField(choices=PLOT_TYPE_CHOICES, required=False)
    house_type = forms.ChoiceField(choices=HOUSE_TYPE_CHOICES, required=False)
    flat_type = forms.ChoiceField(choices=FLAT_TYPE_CHOICES, required=False)
    year_of_construction_from = forms.IntegerField(min_value=1800, max_value=date.today().year+20, required=False)
    year_of_construction_to = forms.IntegerField(min_value=1800, max_value=date.today().year+20, required=False)

    class Media:
        js = (settings.STATIC_URL+'properties/google-maps-places.js', settings.STATIC_URL+'properties/search-form.js')

