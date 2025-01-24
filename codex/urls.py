from django.conf.urls import url
from codex.views import client,solutions,surveysol,services,aboutus,contact

urlpatterns=[
    url(r'^client/$',client,name="client"),
    url(r'^contact/$',contact,name="contact"),
    url(r'^solutions/$',solutions,name="solutions"),
    url(r'^aboutus/$',aboutus,name="aboutus"),
    url(r'^surveysol/$',surveysol,name="surveysol"),
    url(r'^services/$',services,name="services")
]