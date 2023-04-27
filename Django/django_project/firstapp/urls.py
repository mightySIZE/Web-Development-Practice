from django.urls import path
from . import views

urlpatterns = [
    # Create a path object defining the URL pattern to the index view
    path(route='', view=views.index, name='index'),
    path(route='index2/', view=views.index2, name='index2'),
    # Add another path object defining the URL pattern using `/date` prefix
    path(route='date/', view=views.get_date, name='date'),
]