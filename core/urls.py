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
    path('appeals/<int:pk>', core.views.appeal_detail.as_view()),
    path('declarers/<int:pk>', core.views.declarer_detail.as_view()),
    path('services/<int:pk>', core.views.service_detail.as_view()),
    path('appeal_list/', core.views.appeal_list.as_view()),
    path('declarer_list/', core.views.declarer_list.as_view()),
    path('appeal_create/', core.views.appeal_create),
    path('edit_appeal/<int:pk>', core.views.edit_appeal),
    path('edit_declarer/<int:pk>', core.views.edit_declarer),
    path('edit_service/<int:pk>', core.views.edit_service),
    path('declarer_create/', core.views.declarer_create),
    path('service_create/', core.views.service_create),
    path('', core.views.index.as_view()),
]
