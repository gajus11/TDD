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