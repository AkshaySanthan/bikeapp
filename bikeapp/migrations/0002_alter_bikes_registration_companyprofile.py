# Generated by Django 4.0.4 on 2022-06-03 20:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bikeapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bikes',
            name='registration',
            field=models.CharField(max_length=150),
        ),
        migrations.CreateModel(
            name='CompanyProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=120)),
                ('location', models.CharField(max_length=120)),
                ('services', models.CharField(max_length=120)),
                ('logo', models.ImageField(null=True, upload_to='companyprofile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
