Instalacja na mydevil.net.

0. Włączenie w mydevil.net uruchamiania własnych aplikacji:
    Dodatkowe usługi -> Uruchamianie własnego oprogramowania

1. Stworzenie katalogu na wirtualne środowisko:
    mkdir ~/.virtualenvs/

2. Stowrzenie wirtualnego środowiska:
    cd ~/.virtualenvs/
    virtualenv nazwa_środowiska -p /usr/local/bin/python3.5

3. Stworzenie subdomeny w mydevil.net.

4. Stworzenie strony w mydevil.net, wybranie jako srodowska uruchomieniowego pliku
    ~/.virtualenvs/nazwa_srodowiska/bin/python3.5

5. Scigniecie repozytorium:
    cd ~/domains/nazwa_subdomeny/
    rm -rf public_python
    git clone https://lgajownik@bitbucket.org/lgajownik/tdd.git public_python

6. Wrzucenie do folderu public_python pliku passenger.wsgi.py

7. Utworznie folderu dla bazy danych: (SQLite)
    mkdir ../database

8. Stworzenie folderów dla plików statycznych:
    mkdir python_public/public
    mkdir python_public/public/static
    mkdir python_public/public/media

9. Stworzenie bazy danych:
    python manage.py migrate

10. Zebranie plików statycznych:
    python manage.py collectstatic


Konfiguracja JENKINS:
1. Zainstalowac pluginy:
    - Violation
    - xvfb
    - Cobertura
    - ShiningPanda
2. Stworzyc Joba -> Free Software
3. Ustawienia projektu:
    a) Wpisac odpowiednie zrodlo kodu
    b) Poll SCM (budowanie raz na godzine)
        - H * * * *
    c) Zaznaczyc opcje Start Xvfb before the build...
    d) W post build dodac akcje:
        - Publish Cobertura
         reports/coverage.xml
        - Publish JUnit
         reports/junit.xml
        - Publish Violations
         pep8: reports/pep8.report
         pylint: reports/pyflakes.report, reports/pylint.report
    e) Build Command:
        pip install -r requirements.txt
        pip install selenium==2.39
        pip install pyvirtualdisplay
        pip install pep8
        pip install pylint
        pip install pyflakes
        python manage.py jenkins



pip install -r requirements.txt
pip install selenium==2.39
pip install pyvirtualdisplay
pip install pep8
pip install pylint
pip install pyflakes
python manage.py test lists accounts
python manage.py test functional_tests