from django.urls import path
from main.views import show_main, create_product, show_product, show_xml, show_json, show_xml_by_id, show_json_by_id, register
from main.views import login_user
from main.views import logout_user
from main.views import edit_product
from main.views import delete_product
from main import views

app_name = 'main'

#TI 3
urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product/', create_product, name='create_product'),
    path('product/<uuid:id>/', show_product, name='show_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<uuid:product_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<uuid:product_id>/', show_json_by_id, name='show_json_by_id'),
    #TI 4
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    #TI 5
    path('product/<uuid:id>/edit', edit_product, name='edit_product'),
    path('product/<uuid:id>/delete', delete_product, name='delete_product'),
    path('jersey/', views.jersey, name='jersey'),
    path('shoes/', views.shoes, name='shoes'),
    path('ball/', views.ball, name='ball'),
    path('accessory/', views.accessory, name='accessory'),
    path('other/', views.other, name='other'),

]
