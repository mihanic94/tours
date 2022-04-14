from django.urls import path, include

from tours.views import page_not_found, server_error

urlpatterns = [
    path('', include('tours.urls')),
]

handler404 = page_not_found
handler500 = server_error
