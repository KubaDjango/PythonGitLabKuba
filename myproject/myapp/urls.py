from django.urls import path
from .views import get_variable_view


urlpatterns = [
    path('project/', get_variable_view),

]