# T.P-FullStack-Python-Javascript-Django

# Curso a distancia ofrecido por Polotics Misiones

# Integrantes: Mariano Aguirre, Edgardo Duarte, Sebastián Dávila, Melisa Madeloine Cruz Martinez. 

https://es.stackoverflow.com/questions/930/roles-de-usuarios-en-django
Pasos para crear usuarios

$ python manage.py createsuperuser
username: admin
pass: 1234

Creamos usuarios

$ python manage.py shell

> > > from usuarios.models import User
> > > Creamos médicos
> > > User.objects.create_user(username='medico1', password='1234', es_medico=True)
> > > User.objects.create_user(username='medico2', password='1234', es_medico=True)
> > > User.objects.all()
> > > [<User: polotic>, <User: medico1>, <User: medico2>]

Creamos secretarias

> > > User.objects.create_user(username='secretaria1', password='1234', es_secretaria=True)
> > > User.objects.create_user(username='secretaria2', password='1234', es_secretaria=True)

Creamos ventas

> > > User.objects.create_user(username='ventas1', password='1234', es_ventas=True)
> > > User.objects.create_user(username='ventas2', password='1234', es_ventas=True)

Creamos taller

> > > User.objects.create_user(username='taller1', password='1234', es_taller=True)
> > > User.objects.create_user(username='taller2', password='1234', es_taller=True)

Creamos gerencia

> > > User.objects.create_user(username='gerente1', password='1234', es_gerencia=True)
> > > User.objects.create_user(username='gerente1', password='1234', es_gerencia=True)

Ahora creamos los grupos y los asociamos con los usuarios

> > > from django.contrib.auth.models import Group
> > > Group.objects.create(name='Medico')
> > > Group.objects.create(name='Secretaria')
> > > Group.objects.create(name='Ventas')
> > > Group.objects.create(name='Taller')
> > > Group.objects.create(name='Gerencia')

> > > grupo = Group.objects.get(name='Secretaria')
> > > user = User.objects.get(username='secretaria1')
> > > user.groups.add(grupo)
> > > user = User.objects.get(username='secretaria2')
> > > user.groups.add(grupo)

> > > grupo = Group.objects.get(name='Medico')
> > > user = User.objects.get(username='medico1')
> > > user.groups.add(grupo)
> > > user = User.objects.get(username='medico2')
> > > user.groups.add(grupo)

> > > grupo = Group.objects.get(name='Taller')
> > > user = User.objects.get(username='taller1')
> > > user.groups.add(grupo)
> > > user = User.objects.get(username='taller2')
> > > user.groups.add(grupo)

> > > grupo = Group.objects.get(name='Ventas')
> > > user = User.objects.get(username='ventas1')
> > > user.groups.add(grupo)
> > > user = User.objects.get(username='ventas2')
> > > user.groups.add(grupo)

> > > grupo = Group.objects.get(name='Gerencia')
> > > user = User.objects.get(username='gerente1')
> > > user.groups.add(grupo)
> > > user = User.objects.get(username='gerente2')
> > > user.groups.add(grupo)

Ahora, solo bastará con preguntar para saber si un usuario pertenece a cierto grupo, en algunas de tus vistas:

def solo_para_medicos(request):
user = request.user
if user.groups.filter(name='Medico').exists(): # Tiene los privilegios de este grupo
else: # Redireccionar, levantar un error, etc.

O usando las funciones definidas en el modelo

def crear_historia_clinica(request):
user = request.user
if user.es_medico: # Redireccionar, levantar un error, etc.
else: # Redireccionar, levantar un error, etc.
