from django.db import models
from django.contrib import admin
from django.utils import timezone

# Create your models here.
class Property(models.Model):
    class Meta:
        app_label = "properties"


    class TypesOfOffer(models.TextChoices):
        SELL = 'sell', 'Sprzedaż'
        RENT = 'rent', 'Wynajem'
    
    class TypesOfProperties(models.TextChoices):
        FLAT = 'flat', 'Mieszkanie'
        PLOT = 'plot', 'Działka'
        HOUSE = 'house', 'Dom'
        GARAGE = 'garage', 'Garaż'

    #flat choices

    class TypesOfFlats(models.TextChoices):
        TENEMENT = 'tenement', 'Kamienica'
        BLOCK_OF_FLATS = 'block_of_flats', 'Blok'
        APARTMENT = 'apartment', 'Apartamentowiec'

    class TypesOfBuildingMaterials(models.TextChoices):
        BRICK = 'brick', 'Cegła'

    class TypesOfFlatOwnership(models.TextChoices):
        FULL_OWNERSHIP = 'full_ownership', 'Pełna własność'

    class TypesOfHeating(models.TextChoices):
        URBAN = 'urban', 'Miejskie'

    class TypesOfMarket(models.TextChoices):
        PRIMARY = 'primary', 'Pierwotny'
        SECONDARY = 'secondary', 'Wtórny'
    
    class TypesOfConstructionStatus(models.TextChoices):
        TO_COMPLETION = 'to_completion', 'do wykończenia'

    # plot choices

    class TypesOfPlots(models.TextChoices):
        AGRICULTURAL='agricultural', 'Rolna',
        BUILDING='building', 'Budowlana',
        RECREATIONAL='recreational', 'Rekreacyjna',
        FOREST='forest', 'Leśna',

    # house choices

    class TypesOfBuilding(models.TextChoices):
        DETACHED_HOUSE='detached_house', 'Wolnostojący',
        SEMI_DETACHED_HOUSE='semi_detached_house', 'Bliźniak',
        TERRACED_HOUSE='terraced_house', 'Szeregowiec',

    # garage choices

    class TypesOfGarageLocalizations(models.TextChoices):
        IN_BUILDING = 'in_building', 'w budynku'
        SEPARATE = "separate", 'samodzielny'

    service_id = models.PositiveIntegerField(default=None, null=True)
    service_name = models.CharField(max_length=255, null=False, default=None)
    service_url = models.CharField(max_length=255, null=False, default=None)
    scrape_job_id = models.UUIDField(primary_key=False, default=None, editable=True, null=True)
    create_date = models.DateTimeField(default=timezone.now, null=True)
    modify_date = models.DateTimeField(default=timezone.now, null=True)
    #main common fields
    title = models.CharField(max_length=255, null=False, default=None)
    price = models.FloatField(default=None, null=False)
    description = models.TextField(null=True)
    area = models.FloatField(default=None, null=False)
    type_of_property = models.CharField(max_length=100, choices = TypesOfProperties.choices, default=TypesOfProperties.FLAT, null=False)
    type_of_offer = models.CharField(max_length=100, choices = TypesOfOffer.choices, default=TypesOfOffer.SELL, null=False)
    regular_user = models.BooleanField(default=None, null=True)#czy zamieszczone przez agenta czy przezz osobę prywatną
    #localization fields
    formatted_address = models.CharField(max_length=255, null=True)
    province = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)
    district = models.CharField(max_length=255, null=True)
    district_neighbourhood = models.CharField(max_length=255, null=True)#poddzielnica np Muranów
    street = models.CharField(max_length=255, null=True)
    #flat fields
    floor = models.SmallIntegerField(default=None, null=True)
    building_floors_num = models.SmallIntegerField(default=None, null=True)
    rent = models.FloatField(default=None, null=True)#czynsz
    type_of_flat = models.CharField(max_length=100, choices = TypesOfFlats.choices, default=None, null=True)
    flat_ownership = models.CharField(max_length=100, choices = TypesOfFlatOwnership.choices, default=None, null=True)
    heating = models.CharField(max_length=100, choices = TypesOfHeating.choices, default=None, null=True)
    market_type = models.CharField(max_length=100, choices = TypesOfMarket.choices, default=None, null=True)
    construction_status = models.CharField(max_length=100, choices = TypesOfConstructionStatus.choices, default=None, null=True)
    number_of_rooms = models.PositiveSmallIntegerField(default=None, null=True)
    year_of_construction = models.PositiveSmallIntegerField(default=None, null=True)
    # plot fileds
    type_of_plot = models.CharField(max_length=100, choices = TypesOfPlots.choices, default=None, null=True)
    # house fields
    type_of_building = models.CharField(max_length=100, choices = TypesOfPlots.choices, default=None, null=True)
    plot_area = models.FloatField(default=None, null=True)
    #garage fields
    garage_heating = models.BooleanField(default=None, null=True)
    garage_lighted = models.BooleanField(default=None, null=True)
    garage_localization = models.CharField(max_length=100, choices = TypesOfGarageLocalizations.choices, default=None, null=True)
    # house and plot fileds
    forest_vicinity = models.BooleanField(default=None, null=True)#vicinity - rodzaj sąsiedztwa, sąsiedztwo lasu
    open_terrain_vicinity = models.BooleanField(default=None, null=True)#sąsiedztwo otwartego terenu
    lake_vicinity = models.BooleanField(default=None, null=True)#sąsiedztwo jeziora
    electricity = models.BooleanField(default=None, null=True)
    gas = models.BooleanField(default=None, null=True)
    sewerage = models.BooleanField(default=None, null=True)#kanalizacja
    water = models.BooleanField(default=None, null=True)
    fence = models.BooleanField(default=None, null=True)
    # house and flat fields
    building_material = models.CharField(max_length=100, choices = TypesOfBuildingMaterials.choices, default=None, null=True)
    

    def __str__(self):
        return f"{self.service_id} - {self.price} - {self.area} - {self.title}"

class ServiceFilterIds(models.Model):
    service_name = models.CharField(max_length=255, null=False, default=None)
    field_name = models.CharField(max_length=255, null=False, default=None)
    service_id = models.CharField(max_length=255, null=False, default=None)

class MissingValues(models.Model):
    service_name = models.CharField(max_length=255, null=False, default=None)
    field_name = models.CharField(max_length=255, null=False, default=None)
    value = models.CharField(max_length=255, null=False, default=None)