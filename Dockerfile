#Obraz Dockera będzie oparty na obrazie Pythona w wersji 3.10.10
FROM python:3.10.10
#Ustawienie zmiennej środowiskowej z informacją o wyprowadzaniu danych bez buforowania
ENV PYTHONUNBUFFERED 1
#Katalog roboczy
WORKDIR /app
#Skopiowanie pliku requirements.txt
COPY requirements.txt .
#Instalacja pakietów z pliku requirements.txt
RUN pip install -r requirements.txt
#Kopiowanie plików
COPY . .
#Wybranie portu
EXPOSE 8000
#Uruchomienie pliku main.py
CMD ["python", "main.py"]
