from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("polls/", include("polls.urls")),  # polls/でpolls.urlsを参照する
    path("admin/", admin.site.urls),  # ここでincludeを使わないのはadminが例外だから
]
