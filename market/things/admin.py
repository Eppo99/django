from django.contrib import admin
from .models import Thing
# Register your models here.
class PostModelAdmin(admin.ModelAdmin):
	list_display = ["title","updated","timestamp"]
	list_display_links = ["updated"]
	list_editable = ["title"]
	list_filter = ["updated","content"]
	search_fields = ["title","content"]
	class Meta:
		model = Thing

admin.site.register(Thing,PostModelAdmin)