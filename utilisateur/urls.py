from django.urls import include, path
from utilisateur import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'utilisateurs', views.UtilisateurViewSet)
router.register(r'permissions', views.PermissionViewSet)
router.register(r'conges', views.CongesViewSet)
router.register(r'calendrier', views.Calendrier_CongeViewSet)
router.register(r'prendre_conge', views.Prendre_CongeViewSet)
router.register(r'notes', views.Notes_InternesViewSet)
router.register(r'presence', views.PresenceViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('home/', views.home, name='accueil'),
    path('login/', views.login, name='connexion'),
    path('logout/', views.logout, name='deconnexion'),
    path('register/', views.register, name='inscription'),
    path('userspace/', views.userspace, name='espace utilisateur'),
    path('adminspace/', views.adminspace, name='espace administateur'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
