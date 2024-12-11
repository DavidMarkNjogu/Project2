# Generated by Django 5.1.3 on 2024-12-07 14:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dashboardactivity',
            options={'verbose_name': 'Dashboard Activity', 'verbose_name_plural': 'Dashboard Activity'},
        ),
        migrations.AlterModelOptions(
            name='inquiry',
            options={'verbose_name': 'Inquiry', 'verbose_name_plural': 'Inquiries'},
        ),
        migrations.AlterModelOptions(
            name='property',
            options={'verbose_name': 'Property', 'verbose_name_plural': 'Properties'},
        ),
        migrations.AlterUniqueTogether(
            name='inquiry',
            unique_together={('property', 'user_email')},
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField()),
                ('profile_picture', models.ImageField(upload_to='profile_pics/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]