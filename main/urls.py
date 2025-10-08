from django.urls import path
from main import views

app_name = 'main'

urlpatterns = [
    path('', views.show_main, name='show_main'),
    path('create-product/', views.create_product, name='create_product'),
    path('product/<uuid:id>/', views.show_product, name='show_product'),
    path('xml/', views.show_xml, name='show_xml'),
    path('json/', views.show_json, name='show_json'),
    path('xml/<uuid:product_id>/', views.show_xml_by_id, name='show_xml_by_id'),
    path('json/<uuid:product_id>/', views.show_json_by_id, name='show_json_by_id'),

    # AJAX / API endpoints (for AJAX)
    path('api/products/', views.show_json, name='api_products'),                    # GET list
    path('api/products/create/', views.add_product_ajax, name='api_products_create'), # POST create
    path('api/products/<uuid:product_id>/', views.show_json_by_id, name='api_products_detail'), # GET single
    path('api/products/<uuid:product_id>/edit/', views.edit_product_ajax, name='api_products_edit'), # POST edit
    path('api/products/<uuid:product_id>/delete/', views.delete_product_ajax, name='api_products_delete'), # POST delete

    # Auth
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),

    # TI 5 CRUD pages
    path('product/<uuid:id>/edit', views.edit_product, name='edit_product'),
    path('product/<uuid:id>/delete', views.delete_product, name='delete_product'),

    # categories
    path('jersey/', views.jersey, name='jersey'),
    path('shoes/', views.shoes, name='shoes'),
    path('ball/', views.ball, name='ball'),
    path('accessory/', views.accessory, name='accessory'),
    path('other/', views.other, name='other'),
]
