from django.urls import path

from category.views import CategoriesView, CategoryView

urlpatterns = [
    path('', CategoriesView.as_view(), ),
    path('<int:cat_id>/', CategoryView.as_view(), )
]
