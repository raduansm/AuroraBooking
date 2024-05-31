from rest_framework import generics
from .models import Booking, Hotel, HotelManagement, Notification, Rating, Revenue, Room, User, UserChat
from .serializers import BookingSerializer, HotelManagementSerializer, HotelSerializer, NotificationSerializer, RatingSerializer, RevenueSerializer, RoomSerializer, UserSerializer, UserChatSerializer


class HotelListCreate(generics.ListCreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

class HotelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    
  


class BookingListCreate(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class BookingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class HotelManagementListCreate(generics.ListCreateAPIView):
    queryset = HotelManagement.objects.all()
    serializer_class = HotelManagementSerializer

class HotelManagementDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = HotelManagement.objects.all()
    serializer_class = HotelManagementSerializer

class NotificationListCreate(generics.ListCreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

class NotificationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

class RatingListCreate(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

class RatingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

class RevenueListCreate(generics.ListCreateAPIView):
    queryset = Revenue.objects.all()
    serializer_class = RevenueSerializer

class RevenueDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Revenue.objects.all()
    serializer_class = RevenueSerializer

class RoomListCreate(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class RoomDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserChatListCreate(generics.ListCreateAPIView):
    queryset = UserChat.objects.all()
    serializer_class = UserChatSerializer

class UserChatDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserChat.objects.all()
    serializer_class = UserChatSerializer


