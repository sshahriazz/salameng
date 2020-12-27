from django.urls import path
from product.views import *
app_name = 'product'
urlpatterns = [
    path('productcategory/', product_category_view, name='category'),
    path('productcategory/<str:category_name>/', product_ifo_form_category, name='category_to_info'),
    path('productdetails/<str:product_name>/', product_details_bosc, name='product_details'),
    path('productlists/', all_product_view, name='all_products')
]