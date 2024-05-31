from django.urls import path
from . import views

urlpatterns = [
   path('hotels/', views.HotelListCreate.as_view(), name='hotel-list-create'),
    path('bookings/', views.BookingListCreate.as_view(), name='booking-list-create'),
    path('bookings/<int:pk>/', views.BookingDetail.as_view(), name='booking-detail'),
    path('hotel-managements/', views.HotelManagementListCreate.as_view(), name='hotel-management-list-create'),
    path('hotel-managements/<int:pk>/', views.HotelManagementDetail.as_view(), name='hotel-management-detail'),
    path('notifications/', views.NotificationListCreate.as_view(), name='notification-list-create'),
    path('notifications/<int:pk>/', views.NotificationDetail.as_view(), name='notification-detail'),
    path('ratings/', views.RatingListCreate.as_view(), name='rating-list-create'),
    path('ratings/<int:pk>/', views.RatingDetail.as_view(), name='rating-detail'),
    path('revenues/', views.RevenueListCreate.as_view(), name='revenue-list-create'),
    path('revenues/<int:pk>/', views.RevenueDetail.as_view(), name='revenue-detail'),
    path('rooms/', views.RoomListCreate.as_view(), name='room-list-create'),
    path('rooms/<int:pk>/', views.RoomDetail.as_view(), name='room-detail'),
    path('users/', views.UserListCreate.as_view(), name='user-list-create'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('user-chats/', views.UserChatListCreate.as_view(), name='user-chat-list-create'),
    path('user-chats/<int:pk>/', views.UserChatDetail.as_view(), name='user-chat-detail'),
]