from django.urls import path
from .views import WeightAdd,WeightController,WeightUpdate,WeighList,WeightDelete


urlpatterns = [
    path("",WeightAdd.as_view(),name="weight"),
    path("history/",WeightController),
    path("update/<int:pk>/",WeightUpdate.as_view(),name="weight-update"),
    path("delete/<int:pk>/",WeightDelete.as_view(),name="weight-delete"),
    path("list/",WeighList.as_view(),name="weight-list")
]
