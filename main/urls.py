from django.urls import path
from main.views import (
    show_main, 
    display_items,
    add_items,
    show_xml, 
    show_json, 
    show_xml_by_id, 
    show_json_by_id,
    register,
    login_user,
    logout_user,
    increment_superchat,
    decrement_superchat,
    get_idols_json,
    add_idols_ajax,
    delete_idol,
)

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('display-items', display_items, name='display_items'),
    path('add-items', add_items, name='add_items'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('increment/<int:id>/', increment_superchat, name='increment'),
    path('decrement/<int:id>/', decrement_superchat, name='decrement'),
    path('get-idol/', get_idols_json, name='get_idols'),
    path('add-idols-ajax/', add_idols_ajax, name='add_idols_ajax'),
    path('delete_idol/<int:id>/', delete_idol, name='delete_idol'),
]