from django.urls import path

from tours.views import main_view, departure_view, tour_view

urlpatterns = [
    path('', main_view, name='home'),
    path('departure/<str:departure_code>/', departure_view, name='departure'),
    path('tour/<int:tour_id>/', tour_view, name='tour'),
]
