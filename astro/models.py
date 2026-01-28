from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class TiposDeConteudo(models.TextChoices):
    texto = "texto"
    video = "video"
    audio = "audio"
    imagem = "imagem"


class Conteudo(models.Model):
    assunto = models.CharField(max_length=200)
    tipo = models.CharField(choices=TiposDeConteudo.choices, default=TiposDeConteudo.texto)
    autor = models.ForeignKey(User, on_delete=models.PROTECT)


class Tema(models.Model):
    nome = models.CharField()
    adicionado_em = models.DateTimeField(auto_now_add=True)



# feedbacks (comentarios)

# gamificação -> sistema de pontos para acesso de conteúdo
# acessos - de acordo com o feedback


# duolingo -> micro tarefas - te recompensa por fazer todos os dias um mínimo

# AVA (somente com conteúdos) -

# objetivo - relaxar, sem pressão
# aprender mesmo sem fórmulas ou termos científicos


## constelação -> grafo de conteúdos visitados personalizado individualmente

## cooperação entre usuários -> sistema de anotações compartilhadas

# linguagem acessível e pessoal, mas conceitualmente aprofundada
 

# Temas
# buraco negro
# vida fora da terra
# origem do universo
# evolução do universo
# planetas
# estrelas 
# galáxias 
# exploração espacial
# cosmologia
# ciclo de vida das estrelas
# asteroides
# fake news e pseudociência


# O que ensinar?
# componentes, partes, estrutura das coisas 
# ciclos (como nasce, vive e morre)
# ideias de dimensões(tamanho) e distâncias
# como sabemos isso? 
# o que não sabemos disso?

# contribuições e discussões relevantes -> highlights

# algoritmo de sugestões com base em histórico/temas escolhidos

# MVP -> fechar um escopo 
# conteudos posicionados em constelações, temas, universo


# começar pelo ensino de medida de distancia (primeiro degrau)
# usuario aprender a dinamica da plataforma 
# usuário não tem a percepção de que é um tutorial

# publico-alvo principal: qualquer pessoa curiosa em astronomia
# inicialmente pós ensino fundamental

# objetivo é acessibilizar o conhecimento científico



