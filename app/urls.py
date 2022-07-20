from django.urls import path

from app.views import item_list, item_create, tipo_create

urlpatterns =[
    path('item_list/', item_list),
    path('item_create/', item_create),
    path('tipo_create/', tipo_create)
]