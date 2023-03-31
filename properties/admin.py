from django.contrib import admin
from properties.models import Property

# Register your models here.
class PropertyAdmin(admin.ModelAdmin):
    pass
    # fieldsets = [
    #     (None,               {'fields': ['question_text']}),
    #     ('Date information', {'fields': ['pub_date']}),
    # ]
    # inlines = [ChoiceInline]
    # list_display = ('question_text', 'pub_date', 'was_published_recently')
    # list_filter = ['pub_date']
    # search_fields = ['question_text']

admin.site.register(Property, PropertyAdmin)