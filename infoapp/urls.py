from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.contact_view,name='home'),
    path('admin-page/', views.data_list, name='admin-page'),
    path('admin-login/', views.admin_page, name='login'),
    path('edit/<str:pk>/', views.edit_data, name='edit-data'),
    path('delete/<str:pk>/', views.delete_data, name='delete-data'),
    path('logout/',views.user_logout,name='logout'),


]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
