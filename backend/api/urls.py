from django.urls import path
from . import views

urlpatterns = [
    path("notes/", views.NoteListCreate.as_view(), name="note-list"), #create and list notes
    path("notes/delete/<int:pk>/", views.NoteDelete.as_view(), name="delete-note"), #delete a note
]