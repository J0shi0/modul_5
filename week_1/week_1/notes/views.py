from rest_framework import generics, permissions

from .models import Note, UserModel
from .forms import NoteForm, LoginForm, SignupForm
from .serializers import NoteSerializer, UserSerializer

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm

from django.shortcuts import render, redirect
from django.views import generic

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy


class CustomLoginView(LoginView):
    redirect_authenticated_user = True
    next_page = reverse_lazy('home')


'''class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('home')'''


def home(request):
    if request.user.is_authenticated:
        notes = Note.objects.filter(user=request.user).order_by('-updated_at')
        context = {'notes': notes}
        return render(request, 'home_page.html', context)
    else:
        login_form = LoginForm()
        signup_form = SignupForm()
        context = {'login_form': login_form, 'signup_form': signup_form}
        return render(request, 'guest_page.html', context)


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignupForm()
    return render(request, 'home_page.html', {'signup_form': form})


@login_required
def note_detail(request, note_id):
    note = get_object_or_404(Note, id=note_id, user=request.user)
    context = {'note': note}
    return render(request, 'note_detail.html', context)


@login_required
def note_new(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect('home')
    else:
        form = NoteForm()
    return render(request, 'note_new.html', {'form': form})


@login_required
def note_edit(request, note_id):
    note = get_object_or_404(Note, id=note_id, user=request.user)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NoteForm(instance=note)
    return render(request, 'note_edit.html', {'form': form, 'note': note})


@login_required
def note_delete(request, note_id):
    note = get_object_or_404(Note, id=note_id, user=request.user)
    note.delete()
    return redirect('home')

'''def home_view(request):
    if 



# представления для пользователя
# class UserCreate(generic.CreateView):
# model = UserModel
# template_name = 'user_card.html'


# представления для заметок
## представление для создания и просмотра всех заметок


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
    serializer_class = NoteSerializer'''



