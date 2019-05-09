from django.conf.urls import url,include
from telecombat_app import views
app_name='telecombat_app'
urlpatterns=[
url(r'^telecombat18/$',views.telecombat18,name='telecombat18'),
url(r'^telecombat19/$',views.telecombat19,name='telecombat19'),
url(r'^studentachievements/$',views.studentachievements,name='studentachievements'),
url(r'^departmentactivities/$',views.departmentactivities,name='departmentactivities'),
]
