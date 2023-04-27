from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'onlinecourse'
urlpatterns = [
    # Add path here
    path(route='', view=views.popular_course_list, name='popular_course_list'),
    path(route='home/', view=views.home, name='home'),
    path('course/<int:course_id>/enroll/', views.enroll, name='enroll'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)\
 + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)