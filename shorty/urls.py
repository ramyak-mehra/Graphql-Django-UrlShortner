
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from shortener.views import root, createlink, about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/', createlink, name='create'),
    path('', about, name='about'),
    path('api/' , include('notifications.urls')),
]


if settings.DEBUG:
    urlpatterns += [path('graphql/',
                         csrf_exempt(GraphQLView.as_view(graphiql=True))), ]

urlpatterns += [path('<str:url_hash>/', root, name='root'), ]
