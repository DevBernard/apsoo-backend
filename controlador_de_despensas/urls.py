from django.contrib import admin
from django.urls import path, include

from api import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('restframework/',include('rest_framework.urls')),
    path('api/', include('api.urls'))
]
