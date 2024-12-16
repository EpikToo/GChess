from django.contrib import admin
from django.urls import path
from ninja_extra import NinjaExtraAPI
from analysis.api import ChessAPI

api = NinjaExtraAPI()
api.register_controllers(ChessAPI)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
]