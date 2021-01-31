from django.contrib import admin
from .models import Institute, OurTeam, About, ContactUs, Numbers, NewsLetter, ClientQuery, HeroPicture

# Register your models here.
admin.site.register(Institute)
admin.site.register(OurTeam)
admin.site.register(About)
admin.site.register(NewsLetter)
admin.site.register(ClientQuery)
admin.site.register(HeroPicture)
admin.site.register(Numbers)
admin.site.register(ContactUs)
