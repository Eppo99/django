from django.contrib import admin

# Register your models here.
from .models import item


class PostModelAdmin(admin.ModelAdmin):
	list_display=["name","timestamp","updated"]
	list_display_links=["updated"]
	lit_editable=["name"]
	list_filter=["timestamp","updated"]
	search_fields = ["name","div"]
	class Meta:
		model=item

admin.site.register(item)