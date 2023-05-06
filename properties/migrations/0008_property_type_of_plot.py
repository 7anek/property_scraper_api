# Generated by Django 4.1.4 on 2023-04-20 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0007_alter_property_type_of_building'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='type_of_plot',
            field=models.CharField(choices=[('agricultural', 'Rolna'), ('building', 'Budowlana'), ('recreational', 'Rekreacyjna'), ('forest', 'Leśna')], default=None, max_length=100, null=True),
        ),
    ]