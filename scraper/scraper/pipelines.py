# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

from itemadapter import ItemAdapter
from asgiref.sync import sync_to_async
from properties.models import Property
from scrapy.exceptions import DropItem
from scrapy.utils.project import get_project_settings

class FieldValidationPipeline:

    def process_item(self, item, spider):
        # Check that the 'title' field is not empty
        if not item.get('title'):
            raise DropItem('Missing title field')       
        if not item.get('service_name'):
            raise DropItem('Missing service_name field')
        # Check that the 'price' field is a number
        if not item.get('price'):
            raise DropItem('Missing price field')
        if type(item.get('price')) != float:
            raise DropItem('Invalid type of price field')
        if not item.get('area'):
            raise DropItem('Missing area field')
        if type(item.get('area')) != float:
            raise DropItem('Invalid type of area field')
        if item.get('floor'):
            if type(item.get('floor')) != int:
                raise DropItem('Invalid type of floor field')
        if item.get('number_of_rooms'):
            if type(item.get('number_of_rooms')) != int:
                raise DropItem('Invalid type of number_of_rooms field')

        return item

class ScraperPipeline:
    @sync_to_async
    def process_item(self, item, spider):
        # item.save()
        # return item
        # settings=get_project_settings()
        # print('******* scrapy pipeline WSGI_APPLICATION', settings.WSGI_APPLICATION)
        # print('******* scrapy pipeline DATABASES', settings.DATABASES)
        # print('******* scrapy pipeline PGSERVICEFILE', settings.PGSERVICEFILE)
        # print('******* scrapy pipeline PGPASSFILE', settings.PGPASSFILE)
        print(Property.objects.all())
        if item["service_id"]:
            existing_objects = Property.objects.filter(
                service_id=item["service_id"], service_name=item["service_name"]
            )
            if existing_objects:
                existing_object=existing_objects.first()
            else:
                existing_object = False
        else:
            existing_object = False
        if existing_object:
            existing_object.scrape_job_id = item["scrapyd_job_id"]
            existing_object.service_id = item["service_id"]
            existing_object.service_name = item["service_name"]
            existing_object.title = item["title"]
            existing_object.price = item["price"]
            existing_object.location = item["location"]
            existing_object.description = item["description"]
            existing_object.area = item["area"]
            existing_object.floor = item["floor"]
            existing_object.type_of_property = item["type_of_property"]
            existing_object.type_of_building = item["type_of_building"]
            existing_object.number_of_rooms = item["number_of_rooms"]
            existing_object.create_date = item["create_date"]
            existing_object.modify_date = item["modify_date"]
            existing_object.save()

        else:
            property = Property(
                scrape_job_id=item["scrapyd_job_id"],
                service_id=item["service_id"],
                service_name=item["service_name"],
                title=item["title"],
                price=item["price"],
                location=item["location"],
                description=item["description"],
                area=item["area"],
                floor=item["floor"],
                type_of_property=item["type_of_property"],
                type_of_building=item["type_of_building"],
                number_of_rooms=item["number_of_rooms"],
                create_date=item["create_date"],
                modify_date=item["modify_date"],
            )
            property.save()
        return item
