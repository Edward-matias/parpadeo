from rest_framework import routers
from .api import ProjectViewset

router = routers.DefaultRouter()

#router.register('face/parpadeos',ProjectViewset,'')
router.register(prefix='post', basename='post', viewset=ProjectViewset)

urlpatterns =router.urls