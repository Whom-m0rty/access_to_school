from django.shortcuts import render
from django.http import HttpResponse
import sqlite3
from django.utils import timezone
from .gen_slug import gen_slug

# Create your views here.


def create(request, first_name, surname, patronymic, email):
    conn = sqlite3.connect("db.sqlite3")
    c = conn.cursor()
    c.execute("SELECT * FROM api_post")
    last = c.fetchall()[-1][0]
    slug = gen_slug()
    c.execute("""INSERT INTO api_post
                  VALUES (?, ?, ?, ?, ?, ?, ?)""", (last + 1, first_name, surname, patronymic, slug, email, timezone.now()))
    conn.commit()
    conn.close()
    return HttpResponse(first_name + ' ' + surname + ' ' + patronymic + ' ' + email)
