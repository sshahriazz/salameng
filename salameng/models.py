from django.db import models
from PIL import Image


class Institute(models.Model):
    i_name = models.CharField(max_length=150, default='')
    i_phone_number_1 = models.IntegerField(default=0)
    i_phone_number_2 = models.IntegerField(default=0)
    i_email_address_1 = models.EmailField(null=False)
    i_email_address_2 = models.EmailField()
    i_address_Line_1 = models.TextField(max_length=150)
    i_address_Line_2 = models.TextField(max_length=150)
    i_motive_speech = models.TextField(max_length=350)
    i_basic_info = models.TextField(max_length=350)
    i_tag_line = models.TextField(max_length=350)
    i_why_chose_us = models.CharField(max_length=150)
    i_whats_app_group_join_link = models.CharField(max_length=200)


class ClientQuery(models.Model):
    client_name = models.CharField(max_length=150, default='')
    client_phone = models.IntegerField()
    query_subject = models.CharField(max_length=75)
    client_message = models.TextField(max_length=500)


class NewsLetter(models.Model):
    email = models.EmailField(max_length=100)


class OurTeam(models.Model):
    t_name = models.CharField(max_length=150, default='')
    t_image = models.ImageField(default='de_t.png', upload_to='team_photo')
    t_position = models.CharField(max_length=50)
    t_tag_line = models.CharField(max_length=150)
    t_facebook_link = models.CharField(max_length=150)
    t_instagram_link = models.CharField(max_length=150)
    t_whatsapp = models.IntegerField()

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save()
        img = Image.open(self.t_image.path)  # opened current image instance
        # resizing
        if img.height > 600 or img.width > 600:
            output_size = (600, 600)
            img.thumbnail(output_size)
            img.save(self.t_image.path)


class About(models.Model):
    a_Title = models.CharField(max_length=150)
    a_sub_title = models.CharField(max_length=200)
    a_short_description = models.TextField(max_length=600)
    a_feature_1 = models.CharField(max_length=250)
    a_feature_2 = models.CharField(max_length=250)
    a_feature_3 = models.CharField(max_length=250)
    a_anything_else = models.CharField(max_length=350)
