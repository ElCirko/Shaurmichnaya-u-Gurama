from django.urls import include, path

from product import views

urlpatterns = [
    path('latest-dishes/', views.LatestDishesList.as_view()),
    path('dish/<int:id>/', views.DishDetail.as_view()),
    path('dishes/', views.DishList.as_view()),
    path('dish/<slug:slug>/', views.DishDetailBySlug.as_view()),
    path('dish/<int:id>/ingredients/', views.DishIngredients.as_view())
]