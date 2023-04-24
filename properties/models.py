from django.db import models
from django.contrib import admin
from django.utils import timezone

# Create your models here.
class Property(models.Model):
    class Meta:
        app_label = "properties"


    class TypesOfProperties(models.TextChoices):
        FLAT = 'flat', 'Mieszkanie'
        PLOT = 'plot', 'Działka'

    class TypesOfFlats(models.TextChoices):
        TENEMENT = 'tenement', 'Kamienica'
        BLOCK_OF_FLATS = 'block_of_flats', 'Blok'
        APARTMENT = 'apartment', 'Apartamentowiec'

    class TypesOfPlots(models.TextChoices):
        AGRICULTURAL='agricultural', 'Rolna',
        BUILDING='building', 'Budowlana',
        RECREATIONAL='recreational', 'Rekreacyjna',
        FOREST='forest', 'Leśna',


    service_id = models.PositiveIntegerField(default=None, null=True)
    service_name = models.CharField(max_length=255, null=False, default=None)
    title = models.CharField(max_length=255, null=False, default=None)
    price = models.FloatField(default=None, null=False)
    location = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    area = models.FloatField(default=None)
    floor = models.SmallIntegerField(default=None, null=True)
    type_of_property = models.CharField(max_length=100, choices = TypesOfProperties.choices, default=TypesOfProperties.FLAT, null=False)
    type_of_building = models.CharField(max_length=100, choices = TypesOfFlats.choices, default=None, null=True)
    type_of_plot = models.CharField(max_length=100, choices = TypesOfPlots.choices, default=None, null=True)
    number_of_rooms = models.PositiveSmallIntegerField(default=None, null=True)
    create_date = models.DateTimeField(default=timezone.now, null=True)
    modify_date = models.DateTimeField(default=timezone.now, null=True)
    scrape_job_id = models.UUIDField(primary_key=False, default=None, editable=True, null=True)

    # @admin.display(
    #     boolean=True,
    # )

    def __str__(self):
        return f"{self.service_id} - {self.title}"