from rest_framework import generics, permissions

from .models import Note
from .serializers import NoteSerializer, UserSerializer

from django.contrib.auth import get_user_model
from django.shortcuts import render


# представления для пользователя
class UserList(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


# представления для заметок
## представление для создания и просмотра всех заметок
class NoteList(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


## представление для просмотра, обновления и удаления кокретной записки
class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)


def user_card(request):
    user = {"name": "Иван Иванов", "email": "ivan@example.com"}
    return render(request, 'user_card.html', {'user': user})


def note_card(request, note_id):
    note = Note.objects.get(id=note_id)
    return render(request, 'note_card.html', {'note': note})


def notes_list(request):
    notes = Note.objects.all().order_by('-created_at')
    return render(request, 'notes_list.html', {'notes': notes})


class NoteListCreate(generics.ListCreateAPIView):
    queryset = Note.objects.all().order_by('-created_at')
    serializer_class = NoteSerializer


class NoteRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
