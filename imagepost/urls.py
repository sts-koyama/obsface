from django.urls import path

from .views import signupview, loginview, listview, detailview, logoutview, likebtnview
from .views import CreateImagePost

urlpatterns = [
  path('', listview, name="list"),
  path('signup/', signupview, name='signup'),
  path('login/', loginview, name='login'),
  path('detail/<int:pk>/', detailview, name='detail'),
  path('upload/', CreateImagePost.as_view(), name='upload'),
  path('logout/', logoutview, name='logout'),
  path('likebtn/<int:pk>', likebtnview, name='likebtn'),
]