from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/', include("myapp.urls")),
    path('shop/', include("shop.urls"))
]
