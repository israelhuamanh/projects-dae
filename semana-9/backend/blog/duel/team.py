"""Team answers for the ORM duel.

Authors: James Huaman Quispe, Israel Huaman.
One function per question, each returning a QuerySet.
Checked with: python manage.py duel
"""
from datetime import date  # noqa: F401  (you will need it in question 3)

from django.db.models import Count, Q  # noqa: F401

from blog.models import Author, Category, Comment, Post, Profile, Tag  # noqa: F401


def q1():
    """Los artículos que ya están publicados."""
    return Post.objects.filter(published=True)


def q2():
    """Los artículos que no tienen categoría asignada."""
    return Post.objects.filter(category__isnull=True)


def q3():
    """Los artículos publicados entre el 1 de marzo y el 31 de mayo de 2026, ambos días incluidos."""
    return Post.objects.filter(
        published_at__range=(date(2026, 3, 1), date(2026, 5, 31))
    )


def q4():
    """Los artículos con más de dos comentarios."""
    return Post.objects.annotate(n_comments=Count("comments")).filter(
        n_comments__gt=2
    )


def q5():
    """Los tres artículos publicados con más comentarios; de cada uno, cuántos comentarios
    (`n_comments`) y cuántas etiquetas (`n_tags`)."""
    return (
        Post.objects.filter(published=True)
        .annotate(
            n_comments=Count("comments", distinct=True),
            n_tags=Count("tags", distinct=True),
        )
        .order_by("-n_comments")[:3]
    )


def q6():
    """Los artículos escritos por autores de Perú (publicados o no)."""
    return Post.objects.filter(author__profile__country="Perú")


def q7():
    """Los comentarios de los artículos de la categoría «Tecnología»."""
    return Comment.objects.filter(post__category__name="Tecnología")


def q8():
    """Los autores que nunca han publicado un artículo."""
    return Author.objects.exclude(posts__published=True)
