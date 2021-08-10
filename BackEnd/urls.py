from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.create_test_subject, name='create-test-subject'),
    path('save-sleep-level/', views.set_sleep_level, name='save-sleep-level'),
    path('handle-emotion-data/', views.handle_emotion_data, name='handle-emotion-data'),
    path('does-user-exist/<str:userid>/', views.does_user_exist, name='does_user_exist')
]