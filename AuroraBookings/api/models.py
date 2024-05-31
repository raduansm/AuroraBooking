from django.db import models



class User(models.Model):
    customer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    cell = models.CharField(max_length=20)
    password = models.CharField(max_length=255)
    visited_u = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    nid = models.CharField(max_length=20, unique=True)
    image = models.ImageField(upload_to='user_images/')

    def __str__(self):
        return self.name
    



class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    hotel = models.ForeignKey('Hotel', on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    room_id = models.IntegerField()
    room_type = models.CharField(max_length=255)
    member = models.BooleanField(default=False)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    booking_status = models.CharField(max_length=50)
    payment_status = models.CharField(max_length=50)
    special_request = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Booking {self.id} for Customer {self.customer_id} at Hotel {self.hotel_id}"
    
    
    

class Hotel(models.Model):
    hotel_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    room_id = models.IntegerField()
    room_number = models.IntegerField()
    number_of_rooms = models.IntegerField()
    images = models.JSONField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    facilities = models.TextField()
    promo = models.TextField(blank=True, null=True)
    area_or_location = models.CharField(max_length=255)
    manager_id = models.IntegerField()
    room_type = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Rating(models.Model):
    rating_id = models.AutoField(primary_key=True)
    rating = models.IntegerField()
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='ratings')
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    comments = models.TextField()
    posting_date = models.DateTimeField(auto_now_add=True)
    reply = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Rating by {self.customer} for {self.hotel}'
    
    
    
class UserChat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chats')
    ticket_id = models.AutoField(primary_key=True)
    query_type = models.CharField(max_length=255)
    status = models.CharField(max_length=50)
    creation_date = models.DateTimeField(auto_now_add=True)
    resolution_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'Chat Ticket {self.ticket_id} for User {self.user}'


class Notification(models.Model):
    notification_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    manager_id = models.IntegerField()
    notification_type = models.CharField(max_length=255)
    content = models.TextField()
    status = models.CharField(max_length=50)
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Notification {self.notification_id} for User {self.user}'


class Manager(models.Model):
    manager_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    contact_number = models.CharField(max_length=20)
    password = models.CharField(max_length=255)
    profile_picture = models.ImageField(upload_to='manager_images/')
    hotel_ownership_documents = models.TextField()
    address_proof = models.TextField()
    room_type = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Room(models.Model):
    room_id = models.AutoField(primary_key=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='rooms')
    room_type = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    facilities = models.TextField()
    availability = models.BooleanField(default=True)

    def __str__(self):
        return f'Room {self.room_id} in Hotel {self.hotel}'


class Revenue(models.Model):
    revenue_id = models.AutoField(primary_key=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='revenues')
    room_type = models.CharField(max_length=50)
    available_rooms = models.IntegerField()
    booked_rooms = models.IntegerField()
    revenue = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f'Revenue Report for {self.hotel} - Room Type {self.room_type}'


class HotelManagement(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='management')
    owner = models.ForeignKey(Manager, on_delete=models.CASCADE, related_name='managed_hotels')
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    facilities = models.TextField()
    images = models.JSONField()
    description = models.TextField()
    approval_status = models.CharField(max_length=50)

    def __str__(self):
        return f'Management for {self.hotel}'




