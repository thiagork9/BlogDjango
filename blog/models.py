from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


#Criação das tabelas no banco, após a migration
#copiar app nos apps.py e inserir no settings.py
class Post(models.Model):
    tittle = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True) #criação do slug (meusite.com/primeiro-post)
    author = models.ForeignKey(User, on_delete=models.CASCADE) #faz com que se o autor for deletado o post tbm seja
    body = models.TextField() #corpo do post
    created = models.DateTimeField(auto_now_add=True)# insere a data de criação do post automaticamente
    update = models.DateTimeField(auto_now=True)#a cada modificação a data é atualizada mantendo a data de criação

    #ordenando o post do mais recente para o mais antigo
    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return self.tittle


    #Definindo a ulr de um post
    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"slug": self.slug})