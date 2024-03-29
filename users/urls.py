from django.urls import path
from . import views


urlpatterns = [
    path('index/', views.index, name='users_main_view'),
#     path('signup/', views.signup, name='signup'),
#     path('login/', views.login, name='login'),
#     path('logout/', views.logout, name='logout'),
#     path('profile/', views.profile, name='profile'),
#     path('edit_profile/', views.edit_profile, name='edit_profile'),
#     path('change_password/', views.change_password, name='change_password'),
#     path('forgot_password/', views.forgot_password, name='forgot_password'),
#     path('reset_password/', views.reset_password, name='reset_password'),
#     path('delete_account/', views.delete_account, name='delete_account'),
#     path('deactivate_account/', views.deactivate_account, name='deactivate_account'),
#     path('activate_account/', views.activate_account, name='activate_account'),
#     path('follow/', views.follow, name='follow'),
#     path('unfollow/', views.unfollow, name='unfollow'),
#     path('followers/', views.followers, name='followers'),
#     path('following/', views.following, name='following'),
#     path('search/', views.search, name='search'),
#     path('notifications/', views.notifications, name='notifications'),
#     path('notifications/<int:notification_id>/', views.notification, name='notification'),
#     path('notifications/<int:notification_id>/delete/', views.delete_notification, name='delete_notification'),
#     path('notifications/delete_all/', views.delete_all_notifications, name='delete_all_notifications'),
#     path('messages/', views.messages, name='messages'),
#     path('messages/<int:conversation_id>/', views.conversation, name='conversation'),
#     path('messages/<int:conversation_id>/delete/', views.delete_conversation, name='delete_conversation'),
#     path('messages/delete_all/', views.delete_all_conversations, name='delete_all_conversations'),
#     path('messages/send_message/', views.send_message, name='send_message'),
#     path('messages/<int:conversation_id>/send_message/', views.send_message, name='send_message'),
#     path('messages/<int:conversation_id>/delete_message/', views.delete_message, name='delete_message'),
#     path('messages/<int:conversation_id>/delete_all_messages/', views.delete_all_messages, name='delete_all_messages'),
#     path('messages/<int:conversation_id>/block/', views.block_conversation, name='block_conversation'),
#     path('messages/<int:conversation_id>/unblock/', views.unblock_conversation, name='unblock_conversation'),
#     path
]