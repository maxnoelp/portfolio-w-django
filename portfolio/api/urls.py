# urls.py
from django.urls import path
from .views import guestbook_entries, delete_guestbook_entry

urlpatterns = [
    path('guestbook/', guestbook_entries, name='guestbook_entries'),
    path('guestbook/<int:entry_id>/', delete_guestbook_entry, name='delete_guestbook_entry'),
]
