from django.urls import path, include
from . import views
urlpatterns = [
    path('posts/',views.post_list),
    path('posts/<int:pk>',views.post_detail),
]