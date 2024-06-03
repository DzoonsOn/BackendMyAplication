# BackendMyAplication
1.Tworzenie folderu i klonowanie repozytorium:

Utwórz nowy folder o nazwie backend.
Otwórz w nim konsolę i wpisz następującą komendę, aby sklonować repozytorium:
"git clone https://github.com/DzoonsOn/BackendMyAplication"

2.Otwieranie projektu w edytorze:

Uruchom edytor do Pythona, najlepiej aktualną wersję PyCharm.
Otwórz projekt, który właśnie zklonowałeś.

3.Tworzenie superużytkownika:

Otwórz terminal w PyCharmie i wpisz komendę, aby dodać superużytkownika z właściwościami admina:

"python manage.py createsuperuser"

Podaj przykładowe dane.

"
Username: Janek0007
Email address: jan@gmail.com
Password: pio
Password (again): pio
"
Jeśli hasło jest zbyt krótkie, system wyświetli ostrzeżenie. Aby obejść walidację hasła, wpisz:

This password is too short. It must contain at least 8 characters.
Bypass password validation and create user anyway? [y/N]: y

4.Uruchamianie serwera:

Aby uruchomić serwer, wpisz w konsoli PyCharm:
"python manage.py runserver"


Jeśli napotkasz problemy, wykonaj dodatkowe kroki migracji bazy danych:
"python manage.py makemigrations"
"python manage.py migrate"
Następnie ponownie uruchom serwer:
"python manage.py runserver"


5. Korzystanie z aplikacji:
Możesz teraz zalogować się, zarejestrować i wylogować bezpośrednio z przeglądarki, odwiedzając odpowiednie strony:
Rejestracja: http://localhost:8000/user/auth/registration/
Logowanie: http://localhost:8000/user/auth/login/
Wylogowanie: http://localhost:8000/user/auth/logout/

Polam sprawdzić !!!!
Aby uzyskać dostęp do panelu administracyjnego, odwiedź:
http://localhost:8000/admin/ i zaloguj się danymi superużytkownika.


IMPORTANT!!!!! Aby móc korzystać z pełnoprawnej aplikacji, najpierw musimy uruchomić serwer, doperio potem można zobaczyć efekty wizualne na frontencie(można pobierać front i backend równolegle).
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Postępuj zgodnie z powyższymi krokami, aby prawidłowo skonfigurować środowisko i uruchomić projekt.




"1.pip install django-resized
2.python.exe -m pip install --upgrade pip
3.pip install dj-rest-auth
4.pip install django-rest-auth
5.pip install django-allauth
6.pip install 'dj-rest-auth[with_social]'
7.python -m venv env
8.pip install virtualenv
9.pip install pillow
10.python manage.py makemigrations"

