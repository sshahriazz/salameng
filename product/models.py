from django.contrib.auth.models import User
from django.db import models
from PIL import Image
from django_currentuser.db.models import CurrentUserField


class AcCategory(models.Model):
    ac_category_name = models.CharField(max_length=250, null=False)
    ac_category_details = models.TextField(max_length=250, null=False)
    ac_category_image = models.ImageField(default='de_ac_cat.png', upload_to='ac_cat_photo')
    uploaded_by = CurrentUserField()
    upload_date = models.DateTimeField(auto_now_add=True, blank=False)

    def __str__(self):
        return self.ac_category_name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save()
        img = Image.open(self.ac_category_image.path)  # opened current image instance
        # resizing
        if img.height > 600 or img.width > 600:
            output_size = (600, 600)
            img.thumbnail(output_size)
            img.save(self.ac_category_image.path)


class AC(models.Model):
    ac_name = models.CharField(max_length=250, null=False)
    ac_brand_name = models.CharField(max_length=50, null=False)
    ac_category = models.ForeignKey(AcCategory, on_delete=models.CASCADE)
    ac_model_number = models.CharField(max_length=30, null=False)
    ac_image = models.ImageField(default='de_ac.png', upload_to='ac_photo')
    ac_description = models.TextField(max_length=1000, null=True)
    ac_normal_price = models.IntegerField(default=0, null=False)
    ac_discounted_price = models.IntegerField(default=0, null=True)
    ac_discount_percent = models.IntegerField(default=0, null=True)
    uploaded_by = CurrentUserField()
    upload_date = models.DateTimeField(auto_now_add=True, blank=False)
    #
    # def __str__(self):
    #     return f'{self.nam} Profile'  # f string which return texts and support jinja

    # resizing photo by overriding save() method from django ORM
    class Meta:
        ordering = ('-upload_date',)

    def __str__(self):
        return self.ac_name + " - From - " + self.ac_category.ac_category_name + " Category"

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save()
        img = Image.open(self.ac_image.path)  # opened current image instance
        # resizing
        if img.height > 600 or img.width > 600:
            output_size = (600, 600)
            img.thumbnail(output_size)
            img.save(self.ac_image.path)
