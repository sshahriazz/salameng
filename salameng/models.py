from django.db import models
from PIL import Image


class Institute(models.Model):
    i_name = models.CharField(max_length=150, default='')
    i_phone_number_1 = models.CharField(max_length=11)
    i_phone_number_2 = models.CharField(max_length=11)
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
    client_phone = models.CharField(max_length=11)
    query_subject = models.CharField(max_length=75)
    client_message = models.TextField(max_length=500)

    def __str__(self):
        return "Name: " + self.client_name + " Subject: " + self.query_subject


class NewsLetter(models.Model):
    email = models.EmailField(max_length=100)


# pending
class ClientReview(models.Model):
    profile_image = models.ImageField(default='de_t.png', upload_to='team_photo')
    client_title = models.CharField(max_length=250, null=False)
    client_designation = models.CharField(max_length=250, null=False)
    client_quote = models.CharField(max_length=350)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save()
        img = Image.open(self.profile_image.path)  # opened current image instance
        # resizing
        if img.height > 600 or img.width > 600:
            output_size = (600, 600)
            img.thumbnail(output_size)
            img.save(self.profile_image.path)


class OurTeam(models.Model):
    t_name = models.CharField(max_length=150, default='')
    t_image = models.ImageField(default='de_t.png', upload_to='team_photo')
    t_position = models.CharField(max_length=50)
    t_tag_line = models.CharField(max_length=150)
    t_facebook_link = models.CharField(max_length=150)
    t_instagram_link = models.CharField(max_length=150)
    t_whatsapp = models.CharField(max_length=11)

    def __str__(self):
        return "Name: " + self.t_name + " Position: " + self.t_position

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save()
        img = Image.open(self.t_image.path)  # opened current image instance
        # resizing
        if img.height > 600 or img.width > 600:
            output_size = (600, 600)
            img.thumbnail(output_size)
            img.save(self.t_image.path)


# Done
class About(models.Model):
    a_title = models.CharField(max_length=150)
    a_sub_title = models.CharField(max_length=200)
    a_short_description = models.TextField(max_length=600)
    a_feature_1 = models.CharField(max_length=250)
    a_feature_2 = models.CharField(max_length=250)
    a_feature_3 = models.CharField(max_length=250)
    a_anything_else = models.CharField(max_length=350)


# Done
class HeroPicture(models.Model):
    h_image = models.ImageField(default='de_h_p.png', upload_to='Hero')
    upload_date = models.DateTimeField(auto_now_add=True, blank=False)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save()
        img = Image.open(self.h_image.path)  # opened current image instance
        # resizing
        if img.height > 600 or img.width > 600:
            output_size = (1920, 1080)
            img.thumbnail(output_size)
            img.save(self.h_image.path)


class ContactUs(models.Model):
    location = models.CharField(max_length=80)
    email = models.EmailField(max_length=300)
    Phone1 = models.CharField(max_length=11)
    phone2 = models.CharField(max_length=11)


# Done
class Numbers(models.Model):
    clients = models.IntegerField()
    projects = models.IntegerField()
    support_hour = models.IntegerField()
    hard_Workers = models.IntegerField()


class Services(models.Model):
    quote = models.CharField(max_length=200)
    service_name = models.CharField(max_length=15)
    service_description = models.CharField(max_length=50)
