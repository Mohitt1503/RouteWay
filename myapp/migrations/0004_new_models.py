from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_book_booked_at_alter_book_busid_alter_book_nos_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        # Operator
        migrations.CreateModel(
            name='Operator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True)),
                ('company_name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('is_approved', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        # Bus changes
        migrations.AddField(model_name='bus', name='operator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.operator')),
        migrations.AddField(model_name='bus', name='bus_type', field=models.CharField(choices=[('sleeper','Sleeper'),('semi_sleeper','Semi Sleeper'),('seater','Seater'),('ac','AC Seater')], default='seater', max_length=20)),
        migrations.AddField(model_name='bus', name='amenities', field=models.CharField(blank=True, max_length=200)),
        migrations.AddField(model_name='bus', name='is_recurring', field=models.BooleanField(default=False)),
        migrations.AddField(model_name='bus', name='recur_days', field=models.CharField(blank=True, max_length=50)),
        migrations.RenameField(model_name='bus', old_name='price', new_name='base_price'),
        # Book changes
        migrations.AddField(model_name='book', name='original_price', field=models.DecimalField(decimal_places=2, default=0, max_digits=10)),
        migrations.AddField(model_name='book', name='promo_code', field=models.CharField(blank=True, max_length=20, null=True)),
        migrations.AddField(model_name='book', name='discount_amount', field=models.DecimalField(decimal_places=2, default=0, max_digits=8)),
        migrations.AddField(model_name='book', name='refund_status', field=models.CharField(choices=[('none','No Refund'),('pending','Pending'),('done','Refunded')], default='none', max_length=10)),
        migrations.AddField(model_name='book', name='refund_amount', field=models.DecimalField(decimal_places=2, default=0, max_digits=10)),
        migrations.AddField(model_name='book', name='is_round_trip', field=models.BooleanField(default=False)),
        migrations.AddField(model_name='book', name='passenger_details', field=models.TextField(blank=True, null=True)),
        migrations.AlterField(model_name='book', name='status', field=models.CharField(choices=[('B','Booked'),('C','Cancelled'),('X','Completed')], default='B', max_length=2)),
        # UserProfile
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True)),
                ('phone', models.CharField(blank=True, max_length=15)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='profile_photos/')),
                ('wallet_balance', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        # PromoCode
        migrations.CreateModel(
            name='PromoCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=20, unique=True)),
                ('discount_percent', models.PositiveIntegerField()),
                ('max_uses', models.PositiveIntegerField(default=100)),
                ('used_count', models.PositiveIntegerField(default=0)),
                ('valid_until', models.DateField()),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        # Review
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True)),
                ('rating', models.PositiveIntegerField()),
                ('comment', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('bus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='myapp.bus')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.book')),
            ],
            options={'unique_together': {('bus', 'user')}},
        ),
        # FavouriteRoute
        migrations.CreateModel(
            name='FavouriteRoute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True)),
                ('source', models.CharField(max_length=50)),
                ('dest', models.CharField(max_length=50)),
                ('saved_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favourite_routes', to=settings.AUTH_USER_MODEL)),
            ],
            options={'unique_together': {('user', 'source', 'dest')}},
        ),
        # WalletTransaction
        migrations.CreateModel(
            name='WalletTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('transaction_type', models.CharField(choices=[('credit','Credit'),('debit','Debit')], max_length=10)),
                ('description', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wallet_transactions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
