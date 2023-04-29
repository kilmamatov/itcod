from django.urls import path
import core.views


app_name = 'core'


urlpatterns = [
    # path('appleal/', core.views.appleal, name='appleal'),
    # path('declarer_phone/<int:pk>/', core.views.declarer_phone, name='declarer_phone'),
    # path('no_admin/', core.views.no_admin, name='no_admin'),
    # path('val/<str:values>', core.views.val, name='val'),
    # path('serp/<str:values>', core.views.serp, name='serp'),
    # path('declarer_js/<int:pk>', core.views.declarer_js, name='declarer_js'),
    path('appeals/<int:pk>', core.views.appeal_detail),
    path('declarers/<int:pk>', core.views.declarer_detail),
    path('services/<int:pk>', core.views.service_detail),
    path('appeal_list/', core.views.appeal_list),
    path('', core.views.index)
]
