from django.urls import include, path
from rest_framework import routers
from utilisateur import views

router = routers.DefaultRouter()

router.register(r'utilisateurs', views.UtilisateurViewSet)
router.register(r'permissions', views.PermissionViewSet)
router.register(r'conges', views.CongesViewSet)
router.register(r'calendrier', views.Calendrier_CongeViewSet)
router.register(r'prendre_conge', views.Prendre_CongeViewSet)
router.register(r'notes', views.Notes_InternesViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # path('', include(router.urls)),
    path('', views.home, name="homepage"),
    path('home/', views.home, name="homepage"),
    path('login/', views.login, name="signin"),
    path('register/', views.register, name="signup"),
]
