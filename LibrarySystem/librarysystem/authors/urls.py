from django.urls import path
from . import views

urlpatterns = [
    path('', views.author_view, name='authors'), 
    path('<int:author_id>/', views.author_detail, name='author_detail'),  
]
