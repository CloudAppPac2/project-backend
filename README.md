# project-backend

Aby uruchomić aplikację należy:

1. Uruchomić plik main.py

2. Wpisać w przeglądarce adres: http://127.0.0.1:8000/ lub http://127.0.0.1:8000/hello

Pierwsza opcja wyświetli napis w oknie przeglądarki "Hello, world!"
Druga opcja wyświtli napis "Hello, what's your name?" i pole tekstowe. Po wypełnieniu pola imieniem i kliknięciu Submit ukaże się napis: "Hello, (wartość pola)!"

Kod został wyposażony w możliwość przetesotwania.
Aby uruchomić testy Locust należy:

1. Wpisać w pustym terminalu polecenie "Locust"

2. Uruchomić plik main.py

3. Wpisać w przeglądarce adres: http://localhost:8089/

4. Wpisać w przeglądarce adres: http://127.0.0.1:8000/ lub http://127.0.0.1:8000/hello

5. Ustawić parametry testów (liczba userów, którzy będą wykonywać reqest; ile userów w ciągu sekundy wykona request; adres (http://127.0.0.1:8000/ lub http://127.0.0.1:8000/hello))i je uruchomić
