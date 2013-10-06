from django.contrib import admin
from codecamp.ember.models import Session, Speaker, Rating, Tag,Location

admin.site.register(Tag)
admin.site.register(Location)
admin.site.register(Session)
admin.site.register(Speaker)
admin.site.register(Rating)
