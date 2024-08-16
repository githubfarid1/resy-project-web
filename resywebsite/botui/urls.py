from django.urls import path
from botui import views
# print(__package__)
prefix = __package__ + "_"
urlpatterns = [
    path(route='reservations', view=views.show_reservations, name=prefix + "show_reservations"),
    path(route='reservation_list', view=views.reservation_list, name=prefix + "reservation_list"),
]