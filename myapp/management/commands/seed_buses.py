from django.core.management.base import BaseCommand
from myapp.models import Bus
from datetime import date, timedelta
import random

ROUTES = [
    ("Mumbai", "Pune"), ("Pune", "Mumbai"),
    ("Mumbai", "Goa"), ("Goa", "Mumbai"),
    ("Mumbai", "Nagpur"), ("Nagpur", "Mumbai"),
    ("Pune", "Goa"), ("Goa", "Pune"),
    ("Pune", "Nagpur"), ("Nagpur", "Pune"),
    ("Pune", "Hyderabad"), ("Hyderabad", "Pune"),
    ("Pune", "Bangalore"), ("Bangalore", "Pune"),
    ("Mumbai", "Bangalore"), ("Bangalore", "Mumbai"),
    ("Mumbai", "Hyderabad"), ("Hyderabad", "Mumbai"),
    ("Delhi", "Jaipur"), ("Jaipur", "Delhi"),
    ("Delhi", "Agra"), ("Agra", "Delhi"),
    ("Delhi", "Lucknow"), ("Lucknow", "Delhi"),
    ("Delhi", "Chandigarh"), ("Chandigarh", "Delhi"),
    ("Delhi", "Manali"), ("Manali", "Delhi"),
    ("Delhi", "Shimla"), ("Shimla", "Delhi"),
    ("Delhi", "Haridwar"), ("Haridwar", "Delhi"),
    ("Delhi", "Dehradun"), ("Dehradun", "Delhi"),
    ("Bangalore", "Chennai"), ("Chennai", "Bangalore"),
    ("Bangalore", "Hyderabad"), ("Hyderabad", "Bangalore"),
    ("Bangalore", "Mysore"), ("Mysore", "Bangalore"),
    ("Bangalore", "Coimbatore"), ("Coimbatore", "Bangalore"),
    ("Chennai", "Madurai"), ("Madurai", "Chennai"),
    ("Chennai", "Coimbatore"), ("Coimbatore", "Chennai"),
    ("Chennai", "Pondicherry"), ("Pondicherry", "Chennai"),
    ("Hyderabad", "Visakhapatnam"), ("Visakhapatnam", "Hyderabad"),
    ("Hyderabad", "Vijayawada"), ("Vijayawada", "Hyderabad"),
    ("Kolkata", "Siliguri"), ("Siliguri", "Kolkata"),
    ("Kolkata", "Bhubaneswar"), ("Bhubaneswar", "Kolkata"),
    ("Ahmedabad", "Surat"), ("Surat", "Ahmedabad"),
    ("Ahmedabad", "Vadodara"), ("Vadodara", "Ahmedabad"),
    ("Jaipur", "Jodhpur"), ("Jodhpur", "Jaipur"),
    ("Jaipur", "Udaipur"), ("Udaipur", "Jaipur"),
    ("Lucknow", "Varanasi"), ("Varanasi", "Lucknow"),
    ("Lucknow", "Kanpur"), ("Kanpur", "Lucknow"),
]

BUS_NAMES = [
    "Shivneri Express", "Asiad Volvo", "Mumbai Darshan",
    "Deccan Queen", "Orange City Express", "Rajdhani Travels",
    "MSRTC Shivai", "SRS Travels", "VRL Express",
    "National Travels", "Parveen Travels", "KPN Travels",
    "Orange Travels", "Chartered Bus", "Greenline Travels",
    "Paulo Travels", "Kadamba Express", "Neeta Tours",
]

BUS_TYPES = ['sleeper', 'semi_sleeper', 'seater', 'ac']
TIMES = ['06:00', '07:30', '09:00', '10:30', '13:00', '15:30', '18:00', '20:00', '21:30', '23:00']
PRICES = {'sleeper': (500, 900), 'semi_sleeper': (350, 650), 'seater': (200, 450), 'ac': (400, 800)}

class Command(BaseCommand):
    help = 'Seed database with sample buses for next 7 days'

    def handle(self, *args, **kwargs):
        created = 0
        today = date.today()
        for days_ahead in range(0, 8):
            journey_date = today + timedelta(days=days_ahead)
            for (src, dst) in ROUTES:
                # 2-4 buses per route per day
                for _ in range(random.randint(2, 4)):
                    btype = random.choice(BUS_TYPES)
                    pmin, pmax = PRICES[btype]
                    price = random.randint(pmin, pmax)
                    seats = random.choice([30, 36, 40, 45, 50])
                    rem = random.randint(int(seats * 0.3), seats)
                    Bus.objects.create(
                        bus_name=random.choice(BUS_NAMES),
                        source=src, dest=dst,
                        nos=seats, rem=rem,
                        base_price=price,
                        date=journey_date,
                        time=random.choice(TIMES),
                        bus_type=btype,
                        amenities=random.choice(['WiFi, Charging', 'AC, Water', 'Charging, Blanket', 'WiFi, AC', '']),
                    )
                    created += 1

        self.stdout.write(self.style.SUCCESS(f'Successfully created {created} buses!'))
