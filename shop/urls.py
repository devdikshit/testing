
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.index,name="shopHome"),
    path('accounts/login/', auth_views.LoginView.as_view()),
    path('register/', views.register,name="register"),
    path('thnku/', views.thnku,name="thnku"),
    path('login/', views.login,name="login"),
    path('tracker/', views.search,name="track"),
    path('logout/', views.logout,name="logout"),
    # path('contact/', views.contact,name="contact"),
    path('productview/', views.productview,name="productview"),
    path('checkout/', views.checkout,name="checkout"),
    path('additem/', views.additem,name="additem"),
    path('edit/<int:id>',views.additem),
    path('delete/<int:id>/',views.delete_view)

]


