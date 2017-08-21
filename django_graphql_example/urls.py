from graphene_django.views import GraphQLView
from django.conf.urls import url

# Put here otherwise you get
# ValueError: attempted relative import beyond top-level package
# If adding this url below to config.urls
urlpatterns = [
    url(r'^graphql', GraphQLView.as_view(graphiql=True)),
]
