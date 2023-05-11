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
from django.db.models.fields import FieldDoesNotExist


class FieldValidationPipeline:

    # def validate_data(data, model):
    #     model_fields = [field.name for field in model._meta.get_fields()]
    #     for key, value in data.items():
    #         if key not in model_fields:
    #             raise KeyError(f"{key} is not a valid field for {model.__name__}")
    #         try:
    #             field_type = model._meta.get_field(key).get_internal_type()
    #             if field_type == 'IntegerField':
    #                 int(value)  # check if value can be cast to int
    #             elif field_type == 'FloatField':
    #                 float(value)  # check if value can be cast to float
    #             # add more field types as needed
    #         except FieldDoesNotExist:
    #             pass  # this field is not a database field, skip it

    def process_item(self, item, spider):
        print('///////////////////process_item',item)
        model_fields = [field.name for field in Property._meta.get_fields()]
        for key, value in item:
            if key in ["price","area"] and value is None:
                print('wymagane pole jest puste')
                raise DropItem("Missing title field")
        # Check that the 'title' field is not empty
        if not item.get("title"):
            raise DropItem("Missing title field")
        if not item.get("service_name"):
            raise DropItem("Missing service_name field")
        # Check that the 'price' field is a number
        if not item.get("price"):
            raise DropItem("Missing price field")
        if type(item.get("price")) != float:
            raise DropItem("Invalid type of price field")
        if not item.get("area"):
            raise DropItem("Missing area field")
        if type(item.get("area")) != float:
            raise DropItem("Invalid type of area field")
        if item.get("floor"):
            if type(item.get("floor")) != int:
                raise DropItem("Invalid type of floor field")
        if item.get("number_of_rooms"):
            if type(item.get("number_of_rooms")) != int:
                raise DropItem("Invalid type of number_of_rooms field")

        return item


class ScraperPipeline:
    @sync_to_async
    def process_item(self, item, spider):      
        if item["service_id"]:
            existing_objects = Property.objects.filter(
                service_id=item["service_id"], service_name=item["service_name"]
            )
            if existing_objects:
                existing_object = existing_objects.first()
            else:
                existing_object = False
        else:
            existing_object = False
        if existing_object:
            existing_object.scrape_job_id = item["scrapyd_job_id"]
            existing_object.service_id = item["service_id"]
            existing_object.service_name = item["service_name"]
            existing_object.service_url = item["service_url"]
            existing_object.title = item["title"]
            existing_object.price = item["price"]
            existing_object.address = item["address"]
            existing_object.province = item["province"]
            existing_object.city = item["city"]
            existing_object.district = item["district"]
            existing_object.district_neighbourhood = item["district_neighbourhood"]
            existing_object.street = item["street"]
            existing_object.description = item["description"]
            existing_object.area = item["area"]
            existing_object.floor = item["floor"]
            existing_object.flat_type = item["flat_type"]
            existing_object.house_type = item["house_type"]
            existing_object.number_of_rooms = item["number_of_rooms"]
            existing_object.create_date = item["create_date"]
            existing_object.modify_date = item["modify_date"]
            existing_object.save()

        else:
            property = Property(
                scrape_job_id=item["scrapyd_job_id"],
                service_id=item["service_id"],
                service_name=item["service_name"],
                service_url=item["service_url"],
                title=item["title"],
                price=item["price"],
                address=item["address"],
                province=item["province"],
                city=item["city"],
                district=item["district"],
                district_neighbourhood=item["district_neighbourhood"],
                street=item["street"],
                description=item["description"],
                area=item["area"],
                floor=item["floor"],
                flat_type=item["flat_type"],
                house_type=item["house_type"],
                number_of_rooms=item["number_of_rooms"],
                create_date=item["create_date"],
                modify_date=item["modify_date"],
            )
            if property:
                property.save()
            else:
                print("++++++++++++++ item sie niezapisał", item)
        return item
    
