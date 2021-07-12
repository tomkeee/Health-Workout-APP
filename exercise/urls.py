from django.urls import path
from django.urls.conf import include
from django.views.generic.edit import UpdateView
from .views import ExerciseList,ExerciseRecord,NewExercise,UpdateExercise,TrainingList,TrainingAdd

urlpatterns = [
    path("add/",NewExercise.as_view(), name="exercise-add"),
    path('list/',ExerciseList),
    path('',ExerciseList,name="list"),
    path('exercise/<str:muscle>/',ExerciseRecord,name="exercise-detail"),
    path('update/<int:pk>/',UpdateExercise.as_view(),name="exercise-update"),
    path("profile/",include("profiles.urls")),
    path("training/",TrainingList.as_view(),name="training"),
    path("training/add",TrainingList.as_view(),name="training-add"),
    path("training/add/",TrainingAdd.as_view())
]
