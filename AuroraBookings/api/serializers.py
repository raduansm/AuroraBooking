from logging import Manager
from rest_framework.serializers import ModelSerializer
from .models import Booking, Hotel, HotelManagement, Notification, Rating, Revenue, Room, User, UserChat

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class BookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
        
class HotelSerializer(ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'
        
class RatingSerializer(ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'
        
class UserChatSerializer(ModelSerializer):
    class Meta:
        model = UserChat
        fields = '__all__'

class NotificationSerializer(ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'
        
        
class ManagerSerializer(ModelSerializer):
    class Meta:
        model = Manager
        fields = '__all__'
        
class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'
        
        
class RevenueSerializer(ModelSerializer):
    class Meta:
        model = Revenue
        fields = '__all__'


class HotelManagementSerializer(ModelSerializer):
    class Meta:
        model = HotelManagement
        fields = '__all__'