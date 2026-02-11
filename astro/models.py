from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class TiposDeConteudo(models.TextChoices):
    texto = "texto"
    video = "video"
    audio = "audio"
    imagem = "imagem"


class Tema(models.Model):
    nome = models.CharField()
    adicionado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


class Conteudo(models.Model):
    assunto = models.CharField(max_length=200)
    tipo = models.CharField(choices=TiposDeConteudo.choices, default=TiposDeConteudo.texto)
    autor = models.ForeignKey(User, on_delete=models.PROTECT)
    # ManyToMany -> n pra n
    temas_relacionados = models.ManyToManyField(Tema, through="TemaToConteudo")

    # Relacionar conteudo a tema principal, maximo 1 subtema, (pode ter temas relacionados)
    # o mesmo tema pode aparecer em 2 "constelações" diferentes, de tema principal e subtema
    # Anotações diferentes podem aparecer com base em: estamos vendo o conteúdo a partir do tema? ou do subtema?
    # constelações de temas -> agrupam os conteudos


class TemaToConteudo(models.Model):
    # Esta tabela faz a associação entre Tema e Conteudo
    tema = models.ForeignKey(Tema, on_delete=models.PROTECT)
    conteudo = models.ForeignKey(Conteudo, on_delete=models.PROTECT)
    nivel_aprofundamento = models.PositiveIntegerField(default=1)
    nivel_associacao = models.PositiveIntegerField(default=1)


class AssociacaoTema(models.Model):
    # Esta tabela faz a associação entre dois Temas
    #
    # Define o quão próximo um tema fica do outro
    #  
    # TODO Depois, validar duplicidade de (tema1, tema2)
    # (1, 2)
    # (2, 1)
    tema1 = models.ForeignKey(Tema, on_delete=models.PROTECT, related_name="tema1")
    tema2 = models.ForeignKey(Tema, on_delete=models.PROTECT, related_name="tema2")
    nivel_interconexao = models.PositiveIntegerField(default=1)
    nivel_associacao = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return f"{self.tema1} <-> {self.tema2}"
    
    class Meta:
        unique_together = ["tema1", "tema2"]


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


'''
tutorial, grafo pequeno
balao onde falas o que achas antes de assistie ao video que já é uma questao
se termina - recompensa de desbloqueia de algo mesmo no caminho do que ja viu, comentarios de outras pessoas? Novos conteudo?
ganha poder de tutor?

sistema de recompensa - aura apos terminar missoes (compensaçao por progresso individual) 
e tambem recompensar se ajudou mais os usuarios (compensaçao por interaçao)

ficha do usuario:
timeline
os conteudos que ja viu
a partir da decisao do usuario de onde começar, algumas opçoes de inicio se apagam outras nao, a depender do grau de associacao
''' 


