from django.urls import path
from django.urls.conf import include
from django.views.generic.edit import UpdateView
from .views import ExerciseList,ExerciseRecord,NewExercise,UpdateExercise,TrainingView,TrainingUpdate

urlpatterns = [
    path("add/",NewExercise.as_view(), name="exercise-add"),
    path('list/',ExerciseList),
    path('',ExerciseList,name="list"),
    path('exercise/<str:muscle>/',ExerciseRecord,name="exercise-detail"),
    path('update/<int:pk>/',UpdateExercise.as_view(),name="exercise-update"),
    path("training/",TrainingView.as_view(),name="training"),
    path("training/update/<int:pk>/",TrainingUpdate.as_view(),name="training-update"),

]
