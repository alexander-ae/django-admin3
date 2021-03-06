"""
TODO - Add URL namespace
"""

from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.IndexView.as_view(),
        name="admin3_index"
    ),
    url(
        regex=r'^(?P<app_label>[_\-\w]+)/(?P<model_name>[_\-\w]+)/$',
        view=views.ModelListView.as_view(),
        name="admin3_model_list"
    ),
    # url(
    #     regex=r'^(?P<app_label>[_\-\w]+)/(?P<model_name>[_\-\w]+)/(?P<id>[\w]+)/$',
    #     view=views.ModelDetailView.as_view(),
    #     name="model_detail"
    # ),
    # url(
    #     regex=r'^(?P<app_label>[_\-\w]+)/(?P<model_name>[_\-\w]+)/(?P<id>[\w]+)/edit/$',
    #     view=views.ModelEditFormView.as_view(),
    #     name="model_detail_edit_form"
    # ),
    # url(
    #     regex=r'^(?P<app_label>[_\-\w]+)/(?P<model_name>[_\-\w]+)/add/$',
    #     view=views.ModelAddFormView.as_view(),
    #     name="model_detail_add_form"
    # ),
    # url(
    #     regex=r'^(?P<app_label>[_\-\w]+)/(?P<model_name>[_\-\w]+)/(?P<id>[\w]+)/delete/$',
    #     view=views.ModelDeleteView.as_view(),
    #     name="model_delete"
    # )
]
