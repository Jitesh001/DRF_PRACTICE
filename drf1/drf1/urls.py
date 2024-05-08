from django.contrib import admin
from django.urls import path, include
from api1 import views as api1_view
from api2 import views as api2_view
from api3 import views as api3_view
from api4 import views as api4_view
from api5 import views as api5_view
from api6 import views as api6_view
from api7 import views as api7_view
from api8 import views as api8_view
from api9 import views as api9_view
from rest_framework.routers import DefaultRouter
#import for rest framework token
from rest_framework.authtoken.views import obtain_auth_token 
#import for customized token
from api9.customeToken import CustomAuthToken
#import for jwt token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from api10 import views as api10_view

router = DefaultRouter()

#viewset or ModelViewset
router.register('api8', api8_view.StudentViewset, basename='student-api8')
router.register('api81', api8_view.StudentReadOnlyViewset, basename='student-api81')

#modelviewst with authentication, permissions, throtllings
router.register('api9', api9_view.StudentViewset, basename='student-api9')
router.register('api91', api9_view.TeacherViewset, basename='teacher-api9')
router.register('api92', api9_view.ProductViewset, basename='product-api9')

#serializer relation (singer -> songs) and nested serialization
#comment out serilzer.py separately to use one of above choices (relation or nested)
router.register('api10-singer', api10_view.SingerViewSet, basename='singer-api10')
router.register('api10-songs', api10_view.SongViewSet, basename='songs-api10')

urlpatterns = [
    path('admin/', admin.site.urls),
    #simple apis from scratch
    path('api1/<int:pk>/', view=api1_view.student_detail, name='student_detail'),
    path('api1/all/', view=api1_view.student_list, name='student_list'),

    #django function/class based views with simple serializer and validations
    #path('api2/stucreate', view=api2_view.student_create, name='student_create'),
    path('api2/stucreate/', view=api2_view.StudentAPI.as_view(), name='student_create'),

    #django class based view with model serializer and validations
    path('api3/stucreate/', view=api3_view.StudentAPI.as_view(), name='student_create'),

    #model serializer and restframework function based views
    #path('api4/', view=api4_view.hello_world, name='hello_world'),
    path('api4/', view=api4_view.student_api, name='student-api'),
    path('api4/<int:pk>/', view=api4_view.student_api, name='student-api'),
    
    #with model serializer and restframework class based views
    path('api5/', view=api5_view.StudentView5.as_view(), name='student-api5'),
    path('api5/<int:pk>/', view=api5_view.StudentView5.as_view(), name='student-api5'),

    #with model serializer and restframework generic views, mixins
    path('api6/', view=api6_view.Student6Api.as_view(), name='student-api6'),
    path('api6/<int:pk>/', view=api6_view.Student6Api.as_view(), name='student-api6'),

    #concrete API views
    path('api7/', view=api7_view.StudentList.as_view(), name='student-api7'),
    path('api7/<int:pk>/', view=api7_view.StudentUpdate.as_view(), name='student-api71'),

    #api8 to api10 as we have used modelViewset with default router
    path('', include(router.urls)),

    #sessionauthentication
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),

    #tokenauthentication
    #path('api-token-auth/', obtain_auth_token, name='api_token_auth'), #default token
    path('api-token-auth/', CustomAuthToken.as_view(), name='api_token_auth'), #customized token

    #jwt tokens
    path('get-jwt/', TokenObtainPairView.as_view(), name='jwt-token'),
    path('jwt-refresh/', TokenRefreshView.as_view(), name='jwt-refresh'),
    path('jwt-verify/', TokenVerifyView.as_view(), name='jwt-verify'),
]
