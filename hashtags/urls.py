from django.urls import path
from. import views


urlpatterns = [
    path('all_hashtags/', views.all_hashtags_view, name='all_hashtags_tags'),
    path('grand/', views.grand_list_view, name='grand_tags'),
    path('young/', views.young_list_view, name='young_tags'),
    path('children/', views.children_list_view, name='children_tags'),
]