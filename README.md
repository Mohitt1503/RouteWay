# RouteWay – Bus Reservation System
### MCA Final Year Project | Django Web Application

---

## Features

### User Features
- Register, Login, Logout (Django Auth)
- Profile page with photo upload, phone, name
- Change password securely
- RouteWay Wallet (refunds credited, use balance for booking)
- Wallet transaction history

### Bus Search
- Search by source, destination, date
- Sort by price / departure time / available seats
- Round trip booking support
- Nearby city suggestion if no bus found
- Save & manage favourite routes

### Seat Selection
- Visual seat grid (window/aisle layout)
- Real-time dynamic pricing (price rises as seats fill)
- Live cost preview as seats are selected
- Double-booking prevention (atomic transactions)

### Booking & Payment
- Passenger details per seat (name, age, gender)
- Promo code / discount coupon system
- Wallet balance usage at payment
- AJAX promo validation
- Email confirmation on booking

### PDF Ticket
- Boarding-pass style PDF with ReportLab
- Embedded QR code with booking details
- Passenger list on ticket

### Cancellations & Refunds
- Refund policy: ≥2 days = 80%, 1 day = 50%, same day = 0%
- Refund auto-credited to wallet
- Cancellation confirmation email

### Reviews & Ratings
- Rate bus (1–5 stars) after journey
- Star hover UI
- Average rating shown on bus listing

### Travel History
- View all past completed journeys
- Rate from history page

### Admin Dashboard
- Revenue stats, booking counts, cancellations, user count
- Bar chart: bookings last 7 days (Chart.js)
- Line chart: revenue last 6 months
- Top 5 popular routes
- Recent bookings table
- Export all bookings to Excel (.xlsx)
- Download monthly report PDF
- Verify passenger ticket by ID

### Operator Management
- Bus operators can register their company
- Admin approves operators
- Operators linked to buses

### QR Ticket Verification
- Staff verify ticket by entering Booking ID
- Shows passenger, route, seat, status

---

## Setup

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py seed_buses
python manage.py runserver
```

### Add Sample Promo Code (via admin)
Go to `/admin/` → PromoCode → Add:
- Code: `SAVE10`, Discount: `10`, Valid Until: any future date

### Environment Variables (production)
```
DJANGO_SECRET_KEY=your-secret-key
EMAIL_HOST_USER=your@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

---

## Tech Stack
- **Backend:** Python 3, Django 4.x
- **Database:** SQLite3
- **Frontend:** HTML5, Bootstrap 5, JavaScript, Chart.js
- **Libraries:** ReportLab, qrcode, Pillow, openpyxl
- **Architecture:** MVT (Model-View-Template)
- **Auth:** Django built-in authentication

---

## Flow
1. Register / Login
2. Find Bus (search + filter + sort)
3. Select Seats (visual grid, live price)
4. Payment (passenger details, promo, wallet)
5. Booking Confirmed → Email + PDF Ticket
6. My Bookings → View / Cancel / Download / Review
7. Travel History → Rate past journeys
8. Admin Dashboard → Reports, exports, charts
