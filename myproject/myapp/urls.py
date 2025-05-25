from django.urls import path
from .views import hello_world, hello_name, add , div, table, update_post, post_list, create_post, get_variable_view

#create_post, delete_post, post_list

urlpatterns = [
    path('project/', get_variable_view),
    path('hello/', hello_world),
    path('hello/<str:name>/', hello_name),
    path('add/<int:a>/<int:b>/', add),
    path('div/<int:a>/<int:b>/', div),
    path('table/', table),

    path('posts/',post_list, name="post_list"),
    path('posts/create/', create_post, name='create_post'),
    path('post/update/<int:post_id>', update_post, name='delete_post'),

]