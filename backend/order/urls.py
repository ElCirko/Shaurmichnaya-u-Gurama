from django.urls import include, path

from order import views

urlpatterns = [
    path("orders/<int:id>/", views.OrderDetail.as_view()),
]
