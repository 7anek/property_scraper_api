# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

from itemadapter import ItemAdapter
from asgiref.sync import sync_to_async
from properties.models import Property

class ScraperPipeline:

    # async def process_item(self, item, spider):
    #     print('################################### TUUUUUUUUUUUUUUUUUUUUUU process_item')
    #     await sync_to_async(item.save)()
    #     # item.save()
    #     return item
    @sync_to_async
    def process_item(self, item, spider):
        print('################################### TUUUUUUUUUUUUUUUUUUUUUU process_item')
        print('88888888888', 'service_id', item["service_id"], 'type', type(item["service_id"]), 'job id', item["scrapyd_job_id"])
        try:
            existing_object = Property.objects.get(service_id=item["service_id"], service_name=item["service_name"])
        except Property.DoesNotExist:
            existing_object = False
        if item["service_id"] and not existing_object:
            print('9999999999999999999','new property')
            property = Property(
                scrape_job_id = item["scrapyd_job_id"],
                service_id = item["service_id"],
                service_name = item["service_name"],
                title = item["title"],
                price = item["price"],
                location = item["location"],
                description = item["description"],
                area = item["area"],
                floor = item["floor"],
                type_of_property = item["type_of_property"],
                type_of_building = item["type_of_building"],
                number_of_rooms = item["number_of_rooms"],
                create_date = item["create_date"],
                modify_date = item["modify_date"],

            )
            property.save()
        elif item["service_id"] and existing_object:
            print('9999999999999999999','modifying property', existing_object)
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
        return item