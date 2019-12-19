
from django.contrib import admin
from django.urls import path, include

from scraper_app.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('scraper/', include('scraper_app.urls'))
]
