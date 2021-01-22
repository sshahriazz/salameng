# Generated by Django 3.1.4 on 2021-01-22 05:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_currentuser.db.models.fields
import django_currentuser.middleware


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0002_auto_20201225_2022'),
    ]

    operations = [
        migrations.CreateModel(
            name='FridgeCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fr_category_name', models.CharField(max_length=250)),
                ('fr_category_details', models.TextField(max_length=250)),
                ('fr_category_image', models.ImageField(default='de_ac_cat.png', upload_to='ac_cat_photo')),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('uploaded_by', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FridgeC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fr_name', models.CharField(max_length=250)),
                ('fr_brand_name', models.CharField(max_length=50)),
                ('fr_model_number', models.CharField(max_length=30)),
                ('fr_image', models.ImageField(default='de_ac.png', upload_to='ac_photo')),
                ('fr_description', models.TextField(max_length=1000, null=True)),
                ('fr_normal_price', models.IntegerField(default=0)),
                ('fr_discounted_price', models.IntegerField(default=0, null=True)),
                ('fr_discount_percent', models.IntegerField(default=0, null=True)),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('fr_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.accategory')),
                ('uploaded_by', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-upload_date',),
            },
        ),
    ]