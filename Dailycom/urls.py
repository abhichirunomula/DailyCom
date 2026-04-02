from django.contrib import admin
from django.urls import path, include
from rides import views

# ADD THESE
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('create/', views.create_ride, name='create_ride'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'),
    path('book/<int:ride_id>/', views.book_ride, name='book_ride'),
    path("my-bookings/", views.my_bookings, name="my_bookings"),
    path('cancel/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
    path('delete/<int:ride_id>/', views.delete_ride, name='delete_ride'),
]

# ADD THIS
if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATICFILES_DIRS[0]
    )