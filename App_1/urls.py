from django.urls import path
from App_1 import views
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    
    path ('', views.App_1, name = 'App_1'),
    path('home/',views.home, name = 'home'),
    path('contact/',views.contact, name = 'contact'),
    path('link/',views.link, name = 'link'),
    path('delete/<task_id>', views.delete_task, name = 'delete_task'),
    path('edit/<task_id>', views.edit_task, name = 'edit_task'),
    path('done/<task_id>', views.done_task, name = 'done_task')
]
# urlpatterns += staticfiles_urlpatterns()
