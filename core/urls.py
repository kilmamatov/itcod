from django.urls import path
import core.views


app_name = 'core'


urlpatterns = [
    path('appleal/', core.views.appleal_count, name='appleal'),
    path('declarer_phone/', core.views.declarer_phone, name='declarer_phone'),
    path('no_admin/', core.views.no_admin, name='no_admin'),
    path('val/', core.views.val, name='val'),
    path('serp/', core.views.serp, name='serp'),
    path('declarer_js/', core.views.declarer_js, name='declarer_js'),
    # почитать про as_view (могут принимать значение атрибутов)
    path('appeals/<int:pk>', core.views.AppealDetailView.as_view()),
    path('declarers/<int:pk>', core.views.DeclarerdDetailView.as_view()),
    path('services/<int:pk>', core.views.ServiceDetailView.as_view()),
    path('appeal_list/', core.views.AppealListView.as_view()),
    path('declarer_list/', core.views.DeclarerListView.as_view()),
    path('appeal_create/', core.views.appeal_create),
    # path('appeal_create/', core.views.AppealCreateView.as_view()),
    path('edit_appeal/', core.views.edit_appeal),
    # path('edit_appeal/<int:pk>', core.views.UpdateAppealView.as_view()),
    path('edit_declarer/', core.views.edit_declarer),
    # path('edit_declarer/<int:pk>', core.views.UpdateDeclarerView.as_view()),
    path('edit_service/', core.views.edit_service),
    # path('edit_service/<int:pk>', core.views.UpdateServiceView.as_view()),
    path('declarer_create/', core.views.declarer_create),
    # path('declarer_create/', core.views.DeclarerCreateView.as_view()),
    path('service_create/', core.views.service_create),
    # path('service_create/', core.views.ServiceCreateView.as_view()),
    path('', core.views.Index.as_view()),
]
