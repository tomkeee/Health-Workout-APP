from django.urls import path
from django.urls.conf import include
from django.views.generic.edit import UpdateView
from .views import ExerciseList,ExerciseRecord,NewExercise,UpdateExercise

urlpatterns = [
    # path("q/",NewExercise.as_view())
    # path('add/',SaveExercise),
    path("add/",NewExercise.as_view(), name="exercise-add"),
    path('list/',ExerciseList),
    path('',ExerciseList),
    path('exercise/<str:muscle>/',ExerciseRecord,name="exercise-detail"),
    path('update/<int:pk>/',UpdateExercise.as_view(),name="exercise-update"),
    path("profile/",include("profiles.urls")),

]
