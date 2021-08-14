from django.urls import path
from . import views


urlpatterns = [
    path('api/register/', views.create_test_subject, name='create-test-subject'),
    path('api/save-sleep-level/', views.set_sleep_level, name='save-sleep-level'),
    path('api/handle-emotion-data/', views.handle_emotion_data, name='handle-emotion-data'),
    path('api/does-user-exist/<str:userid>/', views.does_user_exist, name='does_user_exist')
]