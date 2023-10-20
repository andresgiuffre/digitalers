from django.urls import path, include

urlpatterns = [
    path('myapp/', include("myapp.urls")),
    path('shop/', include("shop.urls"))
]
