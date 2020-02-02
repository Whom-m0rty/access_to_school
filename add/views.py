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
                  VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""", (last + 1, first_name, surname, patronymic, timezone.now(),
                                                          slug, email, timezone.now(), 'False'))
    conn.commit()
    conn.close()
    return HttpResponse(slug)


def commit(request, slug):
    conn = sqlite3.connect("db.sqlite3")
    c = conn.cursor()
    c.execute("SELECT * FROM api_post WHERE slug = :slug", {'slug': slug})
    in_school = c.fetchone()[8]
    if in_school == "True":
        in_school = "False"
    else:
        in_school = "True"
    c.execute("UPDATE api_post SET in_school = :in_school, last_use = :last_use WHERE slug = :slug",
              {'in_school': in_school, 'slug': slug, 'last_use': str(timezone.now())})
    conn.commit()
    conn.close()
    return HttpResponse("OK")