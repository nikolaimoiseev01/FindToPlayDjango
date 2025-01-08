from django.contrib import admin

# Register your models here.
from events.models import Event, Sport

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'scheduled_at', 'location', 'user_created', 'sport')
    search_fields = ('title', 'description', 'location')


admin.site.register(Event, EventAdmin)
admin.site.register(Sport)