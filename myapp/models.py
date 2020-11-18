from django.db import models

# Create your models here.
# DJANGO ORM - Object Relational Mapper


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name="Titulo")
    # campo subtitle facultativo, blank -> faz com que seja possivel enviar vazio pelo painel-adm-
    subtitle = models.CharField(
        max_length=255, null=True, blank=True, verbose_name="Subtitulo"
    )
    content = models.TextField(verbose_name="Corpo do artigo")
    user = models.ForeignKey()

    # aqui ele alterou o nome que é apresentado no painel-adm
    class Meta:
        verbose_name = "Artigo"
        verbose_name_plural = "Artigos"

    # aqui ele retorna o titulo do post ao inves de Post.object.id(1)
    def __str__(self):
        return self.title
