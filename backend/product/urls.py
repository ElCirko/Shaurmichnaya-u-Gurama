from django.urls import include, path

from product import views

urlpatterns = [
    path('latest-dishes/', views.LatestDishesList.as_view()),
]