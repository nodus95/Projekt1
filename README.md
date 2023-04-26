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


### Przykładowe użycia naszego programu

Uwaga! Wszystkie współrzędne MUSZĄ być oddzielone spacją!









