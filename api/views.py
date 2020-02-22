from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils import timezone
from django.views.generic import View
from django.http import HttpResponse
from django.core.mail import send_mail


from .models import Post
from .serializers import PostSerializer
from .forms import StudentForm

# Create your views here.

class PostView(APIView):
    def get(request, self, slug):
        post = Post.objects.get(slug__iexact=slug)
        serializer = PostSerializer(post)
        return Response({'post': serializer.data})

def index(request):
    if request.method == 'POST':
        query = request.POST.get('q')
        q = Post.objects.all().filter(surname__icontains=query)
    else:
        q = Post.objects.all()
    return render(request, "index.html", {"students": q})

def view(request, slug):
    q = Post.objects.get(slug=slug)
    return render(request, "view.html", {"student": q})


def api_create(request, first_name, surname, patronymic, email):
    q = Post(first_name=first_name, surname=surname, patronymic=patronymic, email=email)
    q.save()
    return HttpResponse("OK")

def api_commit(request, slug):
    q = Post.objects.get(slug__iexact=slug)
    in_school = q.in_school
    if in_school == 'True':
        send_mail('Ваш ребенок {} покинул школу!'.format(q.first_name),
                  'Ваш ребенок {} покинул школу!'.format(q.first_name), 'm0rtydisg@gmail.com',
                  [q.email])
        in_school = 'False'
    else:
        send_mail('Ваш ребенок {} прибыл в школу!'.format(q.first_name),
                  'Ваш ребенок {} прибыл в школу!'.format(q.first_name), 'm0rtydisg@gmail.com',
                  [q.email])
        in_school = 'True'
    q.in_school = in_school
    q.last_use = timezone.now()
    q.save()

    return HttpResponse("OK")

def missing(request):
    q = Post.objects.all().filter(in_school='False')
    return render(request, "index.html", {"students": q})

class Create(View):
    def get(self, request):
        form = StudentForm()
        return render(request, 'create.html', {'form': form})

    def post(self, request):
        bound_form = StudentForm(request.POST)

        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect('/')