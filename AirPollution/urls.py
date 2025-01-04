from unicodedata import name
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('upload_csv/',views.upload_csv,name="upload_csv"),
    path('display_district_data/',views.display_district_data,name="display_district_data"),
    path('get_district_data/',views.get_district_data,name="get_district_data"),
    path('overallval/',views.overyears,name="overyears"),
    path('airQualityIndex/',views.airQualityIndex,name="airQualityIndex"),
    path('bcm/',views.bcm,name="bcm"),
    path('ov/',views.ov,name="ov"),
    path('mp/',views.mp,name="mp"),
    path('pred/',views.district_data_pridict,name="pred"),
    path('display_air_pollution_data/',views.display_air_pollution_data,name="display_air_pollution_data"),
    

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
