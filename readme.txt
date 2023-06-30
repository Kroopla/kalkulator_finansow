Programowanie III, laboratorium – Projekt
Kalkulator wydatków
Szymon Kroplewski 300200
https://github.com/Kroopla/kalkulator_finansow

Na starcie aplikacji wita nas menu:

Co chcesz zrobić?
1. Dodaj wydatek
2. Wyświetl wszystkie wydatki
3. Szukaj
4. Wykres 
9. Wyczyść cały kalkulator
0. Zakończ program

Należy podawać pojedyncze cyfry w celu interakcji z menu

1. Dodaj wydatek
W tej pozycji dodajemy wydatek; Należy podać:
-Kwotę
-Dzień 		(w formacie dwucyfrowej 01,03,10 etc.)
-Miesiąc	(w formacie dwucyfrowej 02,03,11 etc.)
-Rok		(nie może być ujemny)
-Kategorię
-Opis (Opcjonalnie)

2. Wyświetl wszystkie wydatki
Wyświetlają nam się wszystkie dane w formie tekstowej

3. Szukaj
Pojawia nam się następne menu:
"Chcę szukać po:
1. Dacie
2. Okresie
3. Kategorii"

W wyszukiwaniu po Dacie możemy szukać nie podając dnia (wciskając sam ENTER). Wtedy dostaniemy informacje na bazie miesiąca i roku.
Analogiczna sytuacja z miesiącem. Możemy nie podać dnia ani miesiąca. Wtedy wyszukujemy po roku.

W wyszukiwaniu po okresie podajemy dwie daty, początkową i końcową. Otrzymujemy wyniki z podanego przedziału.

W wyszukiwaniu po kategorii, otrzymujemy liste wszystkich wpisanych kategori. Po wpisaniu danej kategorii, otrzymamy wszystkie wpisy z nią związane.

4. Wykres
Po wpisaniu zakresu dat z jakich chcemy otrzymać wykres, wybieramy czy wykres ma być liniowy czy słupkowy. Na Wykresie wyświetlają się dodatkowo średnia, mediana, dominanta.

9. Wyczyść cały kalkulator
Usuwa wszystkie dane z bazy

0. Zakończ program
Kończy program

Przy wpisaniu innej cyfry, znaku lub pustego pola otrzymamy komunikat "Podano złą wartość!