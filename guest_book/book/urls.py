from django.contrib import admin
from django.urls import path

from book.views.records import index_view, add_record_view, edit_record_view, delete_view, confirm_delete, find_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index'),
    path('records/', index_view, name='index'),
    path('records/add/', add_record_view, name='record_add'),
    path('records/<int:pk>/edit/', edit_record_view, name='record_edit'),
    path('task/<int:pk>/delete/', delete_view, name='record_delete'),
    path('task/<int:pk>/confirm_delete/', confirm_delete, name='confirm_delete'),
    path('records/find/', find_view, name='find_record'),
]
