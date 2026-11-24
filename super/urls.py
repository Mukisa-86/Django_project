from django.urls import path
from . import views

urlpatterns = [
    # Frontend pages
    path("super/", views.food_page, name="food-page"),
    path("super/add/", views.food_create_page, name="food-create"),
    path("super/<int:pk>/edit/", views.food_update_page, name="food-update"),
    path("super/<int:pk>/delete/", views.food_delete_page, name="food-delete"),

    # REST API
    path("", views.home_view, name="home-view"),
    path("food/", views.food_view, name="food-view"),
    path("food/<int:pk>/", views.food_detail_view, name="food-detail-view"),
]
