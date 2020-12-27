from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

app_name = 'salameng'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/', include('product.urls', namespace="product"))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

