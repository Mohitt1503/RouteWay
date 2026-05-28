from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Operator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.company_name


class Bus(models.Model):
    BUS_TYPES = (
        ('sleeper', 'Sleeper'),
        ('semi_sleeper', 'Semi Sleeper'),
        ('seater', 'Seater'),
        ('ac', 'AC Seater'),
    )
    operator = models.ForeignKey(Operator, on_delete=models.SET_NULL, null=True, blank=True)
    bus_name = models.CharField(max_length=50)
    source = models.CharField(max_length=50)
    dest = models.CharField(max_length=50)
    nos = models.PositiveIntegerField(help_text="Total seats")
    rem = models.PositiveIntegerField(help_text="Remaining seats")
    base_price = models.DecimalField(decimal_places=2, max_digits=8)
    date = models.DateField()
    time = models.TimeField()
    bus_type = models.CharField(max_length=20, choices=BUS_TYPES, default='seater')
    amenities = models.CharField(max_length=200, blank=True)
    is_recurring = models.BooleanField(default=False)
    recur_days = models.CharField(max_length=50, blank=True)

    class Meta:
        ordering = ['date', 'time']

    def __str__(self):
        return f"{self.bus_name} ({self.source}→{self.dest})"

    def dynamic_price(self):
        if self.nos == 0:
            return float(self.base_price)
        occupancy = (self.nos - self.rem) / self.nos
        if occupancy >= 0.8:
            return round(float(self.base_price) * 1.3, 2)
        elif occupancy >= 0.5:
            return round(float(self.base_price) * 1.15, 2)
        return float(self.base_price)

    def average_rating(self):
        reviews = self.reviews.all()
        if reviews.exists():
            return round(sum(r.rating for r in reviews) / reviews.count(), 1)
        return None


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=15, blank=True)
    photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    wallet_balance = models.DecimalField(decimal_places=2, max_digits=10, default=0)

    def __str__(self):
        return f"{self.user.username}'s profile"


class PromoCode(models.Model):
    code = models.CharField(max_length=20, unique=True)
    discount_percent = models.PositiveIntegerField()
    max_uses = models.PositiveIntegerField(default=100)
    used_count = models.PositiveIntegerField(default=0)
    valid_until = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.code} ({self.discount_percent}% off)"

    def is_valid(self):
        return (self.is_active and
                self.used_count < self.max_uses and
                self.valid_until >= timezone.now().date())


class Book(models.Model):
    BOOKED = 'B'
    CANCELLED = 'C'
    COMPLETED = 'X'
    TICKET_STATUSES = (
        (BOOKED, 'Booked'),
        (CANCELLED, 'Cancelled'),
        (COMPLETED, 'Completed'),
    )
    REFUND_STATUSES = (
        ('none', 'No Refund'),
        ('pending', 'Pending'),
        ('done', 'Refunded'),
    )
    email = models.EmailField()
    name = models.CharField(max_length=50)
    userid = models.IntegerField()
    busid = models.IntegerField()
    bus_name = models.CharField(max_length=50)
    source = models.CharField(max_length=50)
    dest = models.CharField(max_length=50)
    nos = models.PositiveIntegerField()
    seat_numbers = models.CharField(max_length=200, blank=True, null=True)
    original_price = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    promo_code = models.CharField(max_length=20, blank=True, null=True)
    discount_amount = models.DecimalField(decimal_places=2, max_digits=8, default=0)
    date = models.DateField()
    time = models.TimeField()
    booked_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=TICKET_STATUSES, default=BOOKED, max_length=2)
    refund_status = models.CharField(choices=REFUND_STATUSES, default='none', max_length=10)
    refund_amount = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    is_round_trip = models.BooleanField(default=False)
    passenger_details = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['-booked_at']

    def __str__(self):
        return f"{self.name} - {self.bus_name} ({self.date})"


class Review(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking = models.ForeignKey(Book, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('bus', 'user')

    def __str__(self):
        return f"{self.user.username} - {self.bus.bus_name} ({self.rating}star)"


class FavouriteRoute(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favourite_routes')
    source = models.CharField(max_length=50)
    dest = models.CharField(max_length=50)
    saved_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'source', 'dest')

    def __str__(self):
        return f"{self.user.username}: {self.source} to {self.dest}"


class WalletTransaction(models.Model):
    TYPES = (('credit', 'Credit'), ('debit', 'Debit'))
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wallet_transactions')
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    transaction_type = models.CharField(max_length=10, choices=TYPES)
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} {self.transaction_type} Rs{self.amount}"
