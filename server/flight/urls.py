from django.urls import path
from . import views
urlpatterns = [
       path('create-flight', views.AddFlightDetails, name='create-flight'),
       path('search-flight', views.SearchFlight, name='search-flight'),
       path('update-flight/<str:id>',views.UpdateFlightDetails,name='update-flight')
]