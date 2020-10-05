from django.urls import path

from .views import signupview, loginview, listview, detailview, logoutview, likebtnview
from .views import CreateClass

urlpatterns = [
  path('', listview, name="list"),
  path('signup/', signupview, name='signup'),
  path('login/', loginview, name='login'),
  path('detail/<int:pk>/', detailview, name='detail'),
  path('create/', CreateClass.as_view(), name='create'),
  path('logout/', logoutview, name='logout'),
  path('likebtn/<int:pk>', likebtnview, name='likebtn'),
]