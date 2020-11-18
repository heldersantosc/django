INICIANDO COM DJANGO

- inserindo o ambiente virtual 'venv'

```
python -m venv .\venv
```

- iniciando a venv no powershell

```
.\venv\Scripts\Activate.ps1
```

- instlando o django do arquivo requirements

```
pip install -r requirements.txt
```

- criando o projeto com django

```
django-admin startproject config .
```

- rodando o servidor

```
python manage.py runserver
```

- configurar o banco de dados

- realizar a migration e migrate

```
python .\manage.py makemigrations
```

```
python .\manage.py migrate
```

- criar superusuario

```
python .\manage.py createsuperuser
```

- criando um app

```
django-admin startapp myapp
```
