# order-up
A project to learn sqlalchemy and flask

## setup
Create virtual environment
```bash
python3 -m venv venv
```

Activate environment
```bash
source venv/bin/activate
```

Install requirements
```bash
pip install -r requirements.txt
```

Create database (make sure docker is running)
```bash
docker run --name sqlalchemy_test -e POSTGRES_USER=sqlalchemy_test -e POSTGRES_DB=sqlalchemy_test -e POSTGRES_PASSWORD=password -p 5432:5432 -d postgres
```

If already exists check if its running
```bash
docker ps
```

If its not running then start it
```bash
docker start sqlachemy_test
```
