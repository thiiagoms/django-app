from django.urls import path
from .views import read_all_users
# Custom urls here
urlpatterns = [
  path('', read_all_users, name="index")
]