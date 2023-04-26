# Projekt nr 1
Dzięki naszemu programowi będziesz w stanie przetransformować współrzędne.

### Obsługiwane transformacje:

- Algorytm Hirvonena (X, Y, Z -> phi, lambda H)
- Algorytm odwrotny do Hirvonena (phi, lambda, H -> X, Y, Z)
- X, Y, Z -> N, E, U
- phi, lambda -> X2000, Y2000
- phi, lambda -> X1992, Y1992

### Obsługiwane elipsoidy:
- GRS80
- WGS84
- el. Krasowskiego

### Wymagania: 

- konieczne jest poosiadanie pythona w wersji 3.11.3 lub 3.9
- pobrana biblioteka argparse
- pobrana biblioteka numpy

- Projekt został wykonany dla systemu operacyjnego Windows 11 i Windows 10

### Jak korzystać z naszego programu?

Dzięki bibliotece argparse jesteśmy w stanie podawać argumentów przy wywołaniu podając następujące flagi:

```sh
-file
-elip
-trans

```
- "-file" pozwala na wprowadzenie ścieżki do pliku z danymi, które chcemy przetransformować
- "-elip" przyjmuje nazwę elipsoidy
- "-trans" tutaj podajemy naszą wybraną transformację

Przykładowe wywołanie:

```sh
NASZPROJEKT.py -file C:\Users\krzys\projektinfa\test.txt -elip WGS84 -trans XYZ2BLH

```
Przy wpisywaniu nazw elipsoid oraz transforamcji wielkość liter nie ma znaczenia, więc wywołanie może wyglądać w taki sposób:

```sh
NASZPROJEKT.py -file C:\Users\krzys\projektinfa\test.txt -elip wgs84 -trans xyz2blh

```
Jeżeli wszystko zostało właściwie wprowadzone pojawi się komunikat o poprawnym użyciu programu:
```sh
Plik z twoimi przetransformowanymi wspolrzednymi zostal utworzony ;)
To już wszytko. Dziękujemy za skorzystanie z naszego programu.

```
Natomiast, gdy błędnie wprowadzimy nazwę elipsoidy albo transformacji, lub format dancyh w pliku wejściowym będzie niezgodny z wymaganiami również pojawi się odpowiedni komunikat. Przykładowo:
```sh
Zle wpisales nazwe elipsoidy lub transformacji lub podales nieobslugiwana elipsoide lub transformacje.
To już wszytko. Dziękujemy za skorzystanie z naszego programu.

```

lub 

```sh
Dane w pliku wejsciowym sa blednie podane.
To już wszytko. Dziękujemy za skorzystanie z naszego programu.

```


### Opis struktury danych w przykładowych pliku wejściowym i wyjściowym

Przykład 1:
Transformacja:
X, Y, Z -> phi, lambda, H (Algorytm Hirvonena)
Plik: XYZ.txt

```sh
3664940.500 1409153.590 5009571.170
3664940.510 1409153.580 5009571.167
3664940.520 1409153.570 5009571.167
3664940.530 1409153.560 5009571.168
3664940.520 1409153.590 5009571.170


```

Dane to kolejno X, Y, Z. Wszystkie wartości są podane w metrach


Plik wynikowy: twoje_wyniki_XYZ2BLH_wgs84.txt

```sh
52.0972722193 21.0315333328 141.399
52.0972721620 21.0315331442 141.400
52.0972721213 21.0315329557 141.403
52.0972720861 21.0315327671 141.408
52.0972720869 21.0315332281 141.410

```
Natomiast tutaj uzyskane dane to phi, lambda, H. Phi oraz lambda są w stopniach, a wartości H w metrach.

Przykład 2:

Transformacja:
phi, lambda -> X2000, Y2000
Plik: BL.txt

```sh
69.12332 21.32445
78.32466 27.34333
72.07965 25.98987
72.95975 22.22222
76.42321 23.67575

```
Danymi wejściowymi sa phi[stopnie] oraz lambda[stopnie].


Plik wynikowy: twoje_wyniki_BL2PL2000_wgs84.txt

```sh
7683562.371 5751223.668
8726749.942 5776957.087
8034806.942 5875666.850
8112836.181 5735786.723
8501865.563 5726644.959


```
Po transformacji otrzymujemy w pliku wynikowym dane - X2000 oraz Y2000 wyrażone w metrach.

### Uwagi oraz błędy

- Wszystkie dane wprowadzane w pliku wejściowym **MUSZĄ** być oddzielone spacją. W innym wypadku program nie zadziała.
- Uwaga! Plik z danymi wynikowymi może nie zapisywać się w tym samym folderze w którym znajduję się skrypt! Wtedy należy szukać pliku w C:\Users\<nazwa_użytkownika>





