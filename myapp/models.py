from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# DJANGO ORM - Object Relational Mapper

# models.PROTECT -> não permite que o usuario seja excluido se tiver post
# models.CASCADE -> remove todos os posts quando o usuario é excluido
# models.SET_NULL -> inseri null em todos os post que o usuario foi excluido,
# o campo precisa permitir que seja colocado null

# campo subtitle facultativo, blank -> faz com que seja possivel enviar vazio pelo painel-adm-


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name="Titulo")
    subtitle = models.CharField(
        max_length=255, null=True, blank=True, verbose_name="Subtitulo"
    )
    content = models.TextField(verbose_name="Corpo do artigo")
    user = models.ForeignKey(
        User, on_delete=models.PROTECT, null=True, verbose_name="Autor"
    )
    categories = models.ManyToManyField(Category)

    # aqui ele alterou o nome que é apresentado no painel-adm
    class Meta:
        verbose_name = "Artigo"
        verbose_name_plural = "Artigos"

    # aqui ele retorna o titulo do post ao inves de Post.object.id(1)
    def __str__(self):
        return self.title
