from django.conf.urls import url
from django.urls import path
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
    # path('', include(router.urls)),
    path('', views.home, name='accueil'),
    path('home/', views.home, name='accueil'),
    path('login/', views.login, name='connexion'),
    path('logout/', views.logout, name='deconnexion'),
    path('register/', views.register, name='inscription'),
    path('userspace/', views.userDashboard, name='espace utilisateur'),
    path('profile/', views.profile, name='profile'),
    path('404/', views.page404, name='not found'),
    path('addEmploye/', views.addEmploye, name='ajouter Employe'),
    path('permissions/', views.Listpermissions, name='permissions'),
    url(r'^validate/(?P<pk>\d+)$', views.Accepter, name='accepter'),
    url(r'^reject/(?P<pk>\d+)$', views.Rejeter, name='rejeter'),
    path('calendrier/', views.conges, name='calendrier'),
    path('blank/', views.blank, name='page vierge'),
    path('buttons/', views.buttons, name='boutons'),
    path('cards/', views.cards, name='cartes'),
    path('charts/', views.charts, name='graphes'),
    path('forgotpass/', views.forgotPass, name='Mot de passe oublie'),
    path('demandepermis/', views.demandePermis, name='demande permission'),
    path('qr/', views.CodeQR, name='code qr'),
    path('qrscan/', views.qrscan, name='scan qr'),
    path('pause/', views.PauseDej_Debut, name='debutpause'),
    path('pausef/', views.PauseDej_Fin, name='finpause'),
    path('depart', views.Depart, name='depart'),
    path('notes/', views.notesform, name='ajout note'),
    path('sendnote/', views.notes, name='ajouter'),
    path('tables/', views.tables, name='tables'),
    path('pointage/', views.tablePresence, name='pointage'),
    path('animation/', views.animation, name='animations'),
    path('border/', views.border, name='borders'),
    path('color/', views.color, name='couleurs'),
    path('other/', views.other, name='autres'),
    path('utilisateurs/', views.utilisateurs, name='membres'),
    path('conges/', views.conges, name='conges'),
    path('permissions/', views.Listpermissions, name='permissions'),
    path('error/', views.error, name='erreur')
]
