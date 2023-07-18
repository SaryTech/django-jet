from django.urls import path
from django.views.i18n import JavaScriptCatalog

from jet.dashboard import dashboard
from jet.dashboard.views import UpdateDashboardModuleView
from jet.dashboard.views import add_user_dashboard_module_view
from jet.dashboard.views import load_dashboard_module_view
from jet.dashboard.views import remove_dashboard_module_view
from jet.dashboard.views import reset_dashboard_view
from jet.dashboard.views import update_dashboard_module_collapse_view
from jet.dashboard.views import update_dashboard_modules_view


app_name = "dashboard"

urlpatterns = [
    path("module/<pk>/", UpdateDashboardModuleView.as_view(), name="update_module"),
    path("update_dashboard_modules/", update_dashboard_modules_view, name="update_dashboard_modules"),
    path("add_user_dashboard_module/", add_user_dashboard_module_view, name="add_user_dashboard_module"),
    path(
        "update_dashboard_module_collapse/",
        update_dashboard_module_collapse_view,
        name="update_dashboard_module_collapse",
    ),
    path("remove_dashboard_module/", remove_dashboard_module_view, name="remove_dashboard_module"),
    path("load_dashboard_module/<pk>/", load_dashboard_module_view, name="load_dashboard_module"),
    path("reset_dashboard/", reset_dashboard_view, name="reset_dashboard"),
    path("jsi18n/", JavaScriptCatalog.as_view(), {"packages": "jet"}, name="jsi18n"),
]

urlpatterns += dashboard.urls.get_urls()
