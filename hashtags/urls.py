from django.urls import path
from. import views
from .views import AllHashtagsView, GrandListView, YoungListView, ChildrenListView


urlpatterns = [
    path('hashtags/', AllHashtagsView.as_view(), name='all_hashtags'),
    path('grand/', GrandListView.as_view(), name='grand_list'),
    path('young/', YoungListView.as_view(), name='young_list'),
    path('children/', ChildrenListView.as_view(), name='children_list'),
]

# urlpatterns = [
#     path('all_hashtags/', views.all_hashtags_view, name='all_hashtags_tags'),
#     path('grand/', views.grand_list_view, name='grand_tags'),
#     path('young/', views.young_list_view, name='young_tags'),
#     path('children/', views.children_list_view, name='children_tags'),
# ]