from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from research.views import company_research_view

def home_view(request):
    return HttpResponse('<h2>Welcome to Company Researcher</h2><p><a href="/company/">Go to Company Research</a></p>')

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_view, name="home"),   # 👈 homepage
    path("company/", company_research_view, name="company_research"),
]
