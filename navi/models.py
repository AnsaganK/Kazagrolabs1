from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Corms(models.Model):
    client = models.ForeignKey("ClientCorm", on_delete=models.CASCADE, related_name="corms")
    count = models.IntegerField()
    parent = models.OneToOneField('self', on_delete=models.CASCADE,blank=True, null=True, related_name="children")
    date = models.DateField(null=True, blank=True)
    statusChoice = (
        ('Поступило', 'Поступило'),
        ('Готово', 'Готово')
    )
    status = models.CharField(max_length=200, default='Поступило', choices=statusChoice)

    def __str__(self):
        return str(self.count)

    class Meta:
        verbose_name = 'Корм'
        verbose_name_plural = 'Корма'

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    name = models.CharField(max_length=200, verbose_name="Активность")
    time = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Активность'
        verbose_name_plural = 'Активности'

class Client(models.Model):
    name = models.CharField(max_length=500)
    countSamples = models.IntegerField()
    date = models.DateField(null=True, blank=True)
    nowTime = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

class ClientCorm(models.Model):
    name = models.CharField(max_length=500)
    date = models.DateField(null=True, blank=True)
    nowTime = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Клиент(Корма)'
        verbose_name_plural = 'Клиенты(корма)'

class elementsName(models.Model):
    name = models.CharField(max_length=500)
    basic = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Элемент'
        verbose_name_plural = 'Элементы'

class Samples(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='samples')
    count = models.IntegerField()
    elements = models.ManyToManyField(elementsName, related_name='elements')
    date = models.DateField(null=True, blank=True)
    nowTime = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    def __str__(self):
        return self.client.name + " (" + str(self.count) + " проб, " + str(len(self.elements.all()))+" эл.)"
    class Meta:
        verbose_name = 'Проба'
        verbose_name_plural = 'Пробы'

class Selection(models.Model):
    nameClient = models.ForeignKey(Client, on_delete=models.CASCADE)
    countSamples = models.IntegerField(null=True, blank=True)
    samples = models.ForeignKey(Samples, on_delete=models.CASCADE,null=True,blank=True, related_name="selection")
    date = models.DateField(null=True, blank=True)
    nowTime = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    statusChoice = (
        ('Поступило', 'Поступило'),
        ('В процессе', 'В процессе'),
        ('Готово', 'Готово')
    )
    status = models.CharField(max_length=200, default='Поступило', choices=statusChoice)

    def __str__(self):
        return self.samples.client.name + " (" + str(self.samples.count) + " проб, " + str(len(self.samples.elements.all()))+" эл.)"

    class Meta:
        verbose_name = 'Почвоотбор'
        verbose_name_plural = 'Почвоотбор'


class Preparation(models.Model):
    nameClient = models.ForeignKey(Client, on_delete=models.CASCADE)
    countSamples = models.IntegerField(null=True, blank=True)
    samples = models.ForeignKey(Samples, on_delete=models.CASCADE,null=True,blank=True, related_name="preparation")
    date = models.DateField(null=True, blank=True)
    nowTime = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    statusChoice = (
        ('Поступило', 'Поступило'),
        ('В процессе', 'В процессе'),
        ('Готово', 'Готово')
    )
    status = models.CharField(max_length=200,default='Поступило',choices=statusChoice)

    parent = models.ForeignKey(Selection, on_delete=models.CASCADE, blank=True, null=True, related_name = "children")
    selfParent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name = "selfChildren")

    def __str__(self):
        return str(self.nameClient.name)

    class Meta:
        verbose_name = 'Пробоподготовка'
        verbose_name_plural = 'Пробоподготовка'


class Laboratory(models.Model):
    nameClient = models.ForeignKey(Client, on_delete=models.CASCADE)
    countSamples = models.IntegerField(null=True, blank=True)
    samples = models.ForeignKey(Samples, on_delete=models.CASCADE,null=True,blank=True,  related_name="laboratory")
    date = models.DateField(null=True, blank=True)
    nowTime = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    statusChoice = (
        ('Поступило','Поступило'),
        ('В процессе', 'В процессе'),
        ('Готово', 'Готово')
    )
    status = models.CharField(max_length=200,default = 'Поступило',choices=statusChoice)

    parent = models.ForeignKey(Preparation, on_delete=models.CASCADE, blank=True, null=True, related_name = "children")
    selfParent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name="selfChildren")

    def __str__(self):
        return str(self.nameClient)

    class Meta:
        verbose_name = 'Лаборатория'
        verbose_name_plural = 'Лаборатория'

class Agrohym(models.Model):
    nameClient = models.ForeignKey(Client, on_delete=models.CASCADE)
    countSamples = models.IntegerField(null=True, blank=True)
    samples = models.ForeignKey(Samples, on_delete=models.CASCADE,null=True,blank=True,  related_name="agrohym")
    date = models.DateField(null=True, blank=True)
    nowTime = models.DateTimeField(auto_now_add=True,blank=True, null=True)

    statusChoice = (
        ('Поступило','Поступило'),
        ('В процессе', 'В процессе'),
        ('Готово', 'Готово')
    )
    status = models.CharField(max_length=200,default = 'Поступило',choices=statusChoice)

    def __str__(self):
        return self.nameClient.name

    #@property
    #def archive(self):
    #    if self.status == 'Готово' and self.date > (datetime.now()).date():
    #        return True
    #    return False

    class Meta:
        verbose_name = 'Агрохим'
        verbose_name_plural = 'Агрохим'