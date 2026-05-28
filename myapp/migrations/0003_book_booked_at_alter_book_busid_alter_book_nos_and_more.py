from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_book_seat_numbers_alter_book_busid_alter_book_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='booked_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='busid',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='book',
            name='nos',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='book',
            name='userid',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='bus',
            name='nos',
            field=models.PositiveIntegerField(help_text='Total number of seats'),
        ),
        migrations.AlterField(
            model_name='bus',
            name='rem',
            field=models.PositiveIntegerField(help_text='Remaining seats'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
