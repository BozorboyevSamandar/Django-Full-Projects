from django.contrib import admin
from .models import Room, Topic, Message


# Register your models here.

class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'participants', 'updated', 'created', 'views')


admin.site.register(Room, RoomAdmin)


class TopicAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Topic, TopicAdmin)


class MessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'room', 'updated', 'created')


admin.site.register(Message, MessageAdmin)
