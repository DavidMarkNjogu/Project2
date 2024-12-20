# Generated by Django 4.2.16 on 2024-12-18 15:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PropertyListing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('location', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('property_type', models.CharField(choices=[('house', 'House'), ('apartment', 'Apartment'), ('condo', 'Condo'), ('townhouse', 'Townhouse'), ('villa', 'Villa'), ('studio', 'Studio'), ('loft', 'Loft'), ('duplex', 'Duplex'), ('penthouse', 'Penthouse'), ('bungalow', 'Bungalow'), ('cabin', 'Cabin'), ('farmhouse', 'Farmhouse'), ('ranch', 'Ranch'), ('mobile_home', 'Mobile Home'), ('commercial', 'Commercial'), ('other', 'Other')], max_length=100)),
                ('custom_property_type', models.CharField(blank=True, max_length=100)),
                ('amenities', models.CharField(default='Not specified', max_length=255)),
                ('num_bedrooms', models.IntegerField(default=1)),
                ('num_bathrooms', models.IntegerField(default=1)),
                ('square_footage', models.IntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='property_images/')),
                ('video', models.FileField(blank=True, null=True, upload_to='property_videos/')),
                ('virtual_tour_url', models.URLField(blank=True, null=True)),
                ('status', models.CharField(default='Available', max_length=50)),
                ('tags', models.CharField(blank=True, max_length=255, null=True)),
                ('sale_status', models.CharField(choices=[('sale', 'For Sale'), ('rent', 'For Rent')], default='sale', max_length=10)),
                ('realtor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
