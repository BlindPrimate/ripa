from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'api/issues', views.IssueView)


urlpatterns = router.urls
