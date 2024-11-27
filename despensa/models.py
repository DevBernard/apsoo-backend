from django.db import models
from django.db.models import ForeignKey
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

Usuario = get_user_model()
    

class Categoria(models.Model):
    nome = models.CharField(unique=True, max_length=32)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    class PrioridadeChoices(models.TextChoices):
        BAIXA = 'S1', 'Baixa'
        BAIXA_MEDIA = 'S2', 'Baixa Média'
        MEDIA = 'S3', 'Média'
        MEDIA_ALTA = 'S4', 'Média Alta'
        ALTA = 'S5', 'Alta'
    nome = models.CharField(max_length=127, unique=True)
    categoria = ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    prior = models.CharField(max_length=2, choices=PrioridadeChoices, default=PrioridadeChoices.MEDIA)#era Integer, mas ocupa mais espaço em disco
    #prior = ForeignKey(Prioridade, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.nome

#model da Despensa
class Despensa(models.Model):
    descricao = models.CharField('Descrição Breve',max_length=255)
    categorias = models.ManyToManyField(Categoria) #categorias_permitidas
    gerente = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.descricao

#acesso entre usuario e despensa:
# class NivelPermissao(models.Model):
#     pass

#Models para o item
class Mercado(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    def __str__(self): 
        return self.nome

class Marca(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    def __str__(self): 
        return self.nome

class Item(models.Model):
    data_vencimento = models.DateTimeField("Data de Vencimento")
    data_compra = models.DateTimeField(default=timezone.now)
    preco = models.FloatField()
    consumido = models.BooleanField(default=False)
    produto = ForeignKey(Produto, on_delete=models.PROTECT)
    mercado = ForeignKey(Mercado, on_delete=models.PROTECT)
    comprador = ForeignKey(Usuario, on_delete=models.PROTECT, null=True)
    despensa = ForeignKey(Despensa, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'Itens'

    def clean(self):
        categoria_id = self.produto.categoria.id
        despensa_categorias = self.despensa.categorias
        if not despensa_categorias.filter(id=categoria_id).exists():
            raise ValidationError('A despensa não permite tal Categoria de Produto')
    
    def __str__(self):
        return f'{str(self.produto)} validade: f{str(self.data_vencimento)}'

#models para lista de compras
class ListaCompra(models.Model):
    usuario = ForeignKey(Usuario, on_delete=models.CASCADE)
    destino = ForeignKey(Despensa, on_delete=models.CASCADE)  #tvz PROTECT seja melhor

class ProdutoQuantidade(models.Model):
    qtd = models.PositiveIntegerField()
    produto = ForeignKey(Produto, on_delete=models.PROTECT)
    lista_compra = ForeignKey(ListaCompra, on_delete=models.CASCADE)

    class Meta:
        unique_together = [['lista_compra','produto']]

    def __str__(self):
        return f'{self.produto}: {self.qtd} unidades'

#relacionamento entre despensa e produto
class QuantidadePadrao(models.Model): 
    class Meta:
        unique_together = ['despensa','produto']
        verbose_name_plural = "Quantidades Padrão"
    qtd_min = models.PositiveIntegerField( blank=True, null=True)
    qtd_med = models.PositiveIntegerField( blank=True, null=True)
    qtd_max = models.PositiveIntegerField( blank=True, null=True)
    despensa = ForeignKey(Despensa, on_delete=models.CASCADE) 
    produto = ForeignKey(Produto, on_delete=models.CASCADE)

#classes de historico
class Consumo(models.Model):
    data_hora = models.DateTimeField(auto_now_add=True)
    item = ForeignKey(Item, on_delete=models.CASCADE)
    usuario = ForeignKey(Usuario, on_delete=models.SET_NULL, null=True) #deletar o usuario nao implica que o item nao tenha sido consumido

    class Meta:
        unique_together = ['item','usuario']

class Transferencia(models.Model):
    def clean(self):
        if self.destino.id == self.origem.id:
            raise ValidationError("O destino deve ser diferente da origem.")
        
    class SituacaoChoices(models.TextChoices):
        SOLICITADO = 'S'
        CONFIRMADO = 'C'
        NEGADO = 'N'
    situacao = models.CharField(max_length=1, choices=SituacaoChoices, default=SituacaoChoices.SOLICITADO)
    data_hora = models.DateTimeField(auto_now_add=True)
    origem = ForeignKey(Despensa,on_delete=models.CASCADE, related_name='+') 
    destino = ForeignKey(Despensa,on_delete=models.CASCADE, related_name='+')
    #tem como utilizar isso para verificar todas as saídas e entradas assim:
    #adicionando uma relate_name pra origem e destino, e permitindo null=True pra origem e destino
    #adicionando uma transferencia para toda inserção de item com origem = None
    #adicionando uma transferencia para todo consumo com destino = None
    
    usuario = ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)

class ItensTransferidos(models.Model):
    item = ForeignKey(Item,on_delete=models.CASCADE)
    transferencia = ForeignKey(Transferencia, on_delete=models.CASCADE)