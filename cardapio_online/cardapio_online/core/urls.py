from django.urls import path
from . import views
urlpatterns = [
    # Nossa rotas
    path('', views.Index, name="index")
]