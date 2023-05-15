from app import views
from django.urls import path
urlpatterns = [
   path('',views.loginpage,name="login"),
   path('signin/',views.signinpage,name="signin"),
   path('logout/',views.logoutpage,name="logout"),
   path('content/',views.content,name='content'),
   path('show/',views.show,name='show'),
   path('edit/<int:id>/',views.edit,name='edit'),
   path('delete/<int:id>/',views.delete,name='delete'),
]
