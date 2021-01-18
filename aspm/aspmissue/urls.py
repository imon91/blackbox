from django.contrib import admin
from django.urls import path

from aspmissue import views

app_name = "aspmissue"
urlpatterns = [
    path('', views.index, name='index'),
    path('model_detail/<int:id>', views.modelDetail, name='modelDetail'),
    path('market_issue/', views.marketIssue, name='marketIssue'),
    path('xcel_view/<int:id>', views.xcel_view, name='xcel_view')
]
