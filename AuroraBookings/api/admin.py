from django.contrib import admin
from .models import Booking, Hotel, Rating, User, Room, Revenue, Notification, HotelManagement, UserChat, Manager


admin.site.register(User)
admin.site.register(HotelManagement)
admin.site.register(Manager)
admin.site.register(Booking)
admin.site.register(Hotel)
admin.site.register(Rating)
admin.site.register(Room)
admin.site.register(Revenue)
admin.site.register(Notification)
admin.site.register(UserChat)


