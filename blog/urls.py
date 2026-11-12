from django.contrib import admin
from django.urls import path, include
admin.site.site_header = 'Virtual Tour Admin'
admin.site.site_title = 'Virtual Tour Admin'
admin.site.index_title = 'Kelola konten tur virtual'
urlpatterns = [path('admin/', admin.site.urls), path('', include('travel.urls'))]
