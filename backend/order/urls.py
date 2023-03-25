from django.urls import path

from order import views

urlpatterns = [
    path("orders/<int:id>/", views.OrderDetail.as_view()),
]
