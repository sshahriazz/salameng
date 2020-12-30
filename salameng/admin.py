from django.contrib import admin
from .models import Institute, OurTeam,About,NewsLetter,ClientQuery
# Register your models here.
admin.site.register(Institute)
admin.site.register(OurTeam)
admin.site.register(About)
admin.site.register(NewsLetter)
admin.site.register(ClientQuery)