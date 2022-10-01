from django.contrib import admin
from django.urls import path

from book.views.records import index_view, add_record_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index'),
    path('records/', index_view, name='index'),
    # path('products/<int:pk>', product_view, name='product_detail'),
    path('records/add/', add_record_view, name='record_add'),
    # path('products/<int:pk>/edit/', edit_product_view, name='product_edit'),
    # path('task/<int:pk>/delete/', delete_view, name='product_delete'),
    # path('task/<int:pk>/confirm-delete/', confirm_delete, name='confirm_delete'),
]
