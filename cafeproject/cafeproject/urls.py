from django.contrib import admin
from django.urls import path
from cafeapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('detai/', views.detail, name="detail"),
    path('detail/', views.detail1, name="detail1"),
    path('detai2/', views.detail2, name="detail2"),
    path('detai3/', views.detail3, name="detail3"),
    path('detai4/', views.detail4, name="detail4"),
    path('detai5/', views.detail5, name="detail5"),
    path('detai6/', views.detail6, name="detail6"),
    path('detai7/', views.detail7, name="detail7"),
    path('detai8/', views.detail8, name="detail8"),
    path('detai9/', views.detail9, name="detail9"),
]