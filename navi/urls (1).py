from django.urls import path
from .views import *
from django.contrib.auth import views as acc

urlpatterns = [
    #path('login/', login, name = 'login'),
    path('',general, name="general"),

    path('selection/', selection, name = 'selection'),
    path('preparation/', preparation, name = 'preparation'),
    path('laboratory/', laboratory, name = 'laboratory'),
    path('agrohym/', agrohym, name = 'agrohym'),

    path('addSelection/', addSelection, name = 'addSelection'),
    path('addPreparation/', addPreparation, name = 'addPreparation'),
    path('addLaboratory/', addLaboratory, name = 'addLaboratory'),
    path('addAgrohym/', addAgrohym, name = 'addAgrohym'),

    path('updateSelection/<int:pk>', updateSelection, name = "updateSelection"),
    path('updatePreparation/<int:pk>', updatePreparation, name = "updatePreparation"),
    path('updateLaboratory/<int:pk>', updateLaboratory, name = "updateLaboratory"),
    path('updateAgrohym/<int:pk>', updateAgrohym, name = "updateAgrohym"),

    path('deleteSelection/<int:pk>', deleteSelection, name = "deleteSelection"),
    path('deletePreparation/<int:pk>', deletePreparation, name = "deletePreparation"),
    path('deleteLaboratory/<int:pk>', deleteLaboratory, name = "deleteLaboratory"),
    path('deleteAgrohym/<int:pk>', deleteAgrohym, name = "deleteAgrohym"),
    path('deleteArchiveAgrohym/<int:pk>', deleteArchiveAgrohym, name = "deleteArchiveAgrohym"),

    path('selection/<int:pk>', detailSelection, name = "detailSelection"),
    path('preparation/<int:pk>', detailPreparation, name = "detailPreparation"),
    path('laboratory/<int:pk>', detailLaboratory, name = "detailLaboratory"),
    path('agrohym/<int:pk>', detailAgrohym, name = "detailAgrohym"),

    path('archiveAgroHym/',archiveAgroHym,name='archiveAgroHym'),
    path('accounts/login/',acc.LoginView.as_view(),name='login'),
    path('accounts/logout/',acc.LogoutView.as_view(),name='logout'),
    path('signup/', signup, name = 'signup'),
    path('addUser/', addUser, name = 'addUser'),
    path('listUser/', listUser, name = 'listUser'),
    path('table/', table, name = 'table'),
    path('statistics/', statistics, name = 'statistics'),

    path('clients/', clients, name = 'clients'),
    path('addClient/', addClient, name = 'addClient'),
    path('detailClient/<int:pk>', detailClient, name = 'detailClient'),
    path('deleteClient/<int:pk>', deleteClient, name = 'deleteClient'),
    path('updateClient/<int:pk>', updateClient, name = 'updateClient'),

    path('samples/', samples, name = 'samples'),
    path('addSample/', addSample, name = 'addSample'),
    path('updateSample/<int:pk>', updateSample, name = 'updateSample'),
    path('deleteSample/<int:pk>', deleteSample, name = 'deleteSample'),
    #path('signup/', signup, name='signup'),
]