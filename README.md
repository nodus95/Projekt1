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

- konieczne jest poosiadanie pythona w wersji 3.9 do 3.11.3
- pobrana biblioteka argparse
- pobrana biblioteka numpy

- Projekt został wykonany dla systemu operacyjnego Windows 10 i Windows 11

### Jak korzystać z naszego programu?

Dzięki bibliotece argparse jesteśmy w stanie podawać argumenty przy wywołaniu, podając następujące flagi:

```sh
-file
-elip
-trans

```
- "-file" pozwala na wprowadzenie ścieżki do pliku z danymi, które chcemy przetransformować
- "-elip" przyjmuje nazwę elipsoidy
- "-trans" tutaj podajemy wybraną przez nas transformację

Przykładowe wywołanie:

```sh
NASZPROJEKT.py -file C:\Users\krzys\projektinfa\test.txt -elip WGS84 -trans XYZ2BLH

```
Przy wpisywaniu nazw elipsoid oraz transforamcji wielkość liter nie ma znaczenia, więc wywołanie może wyglądać również w taki sposób:

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


### Opis struktury danych w przykładowych plikach wejściowych i wyjściowych

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

Dane to kolejno X, Y, Z. Wszystkie wartości muszą być podane w metrach

Gdyby zaistniała potrzeba odszukania pliku wynikowego, jego nazwa to zawsze:
"twoje_wyniki_(nazwa wybranej transformacji)_(wybrana elipsoida).txt"

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

Przykład 3:

Transformacja:
X, Y, Z -> N, E, U
Plik: iks.txt

W pliku wejściowym w kolumnach 1,2,3 znajdują się kolejno X[m], Y[m], Z[m] (w pierwszym wierszu są to współrzędne odbiornika, a w kolejnych wierszach współrzędne satelitów).


```sh
4674202.0707659787 4444444.7139986877 6545323.345368741
2.87678304399999976e+07 7.1113728000000119e+07 3.847713999999999942e+04
-2.391130946000000089e+07 -2.08423180339500000142e+07 -2.229962486000000034e+06
6.32775858699999936e+07 1.288512925399999879e+07 1.944924987600000203e+07
1.982159728800000250e+07 3.882086669999999925e+06 6.423423310199999809e+07
-5.2132131999999940e+06 -2.445428761199999973e+07 -4.484889633000001311e+06

```

Plik wynikowy: twoje_wyniki_XYZ2NEU._GRS80.txt

```sh
-49818564.026 31712552.917 39749968.243
21083868.808 1372313.084 -32971877.624
-25435897.468 -34265014.626 43023679.071
32835774.457 -10845175.725 48600043.381
11607975.073 -14129582.779 -26836041.331

```
W pliku wyjściowym znajdują się kolejno wektory N, E, U. Wszystkie parametry są wyrażone w metrach.

### Uwagi oraz błędy

- Wszystkie dane wprowadzane w pliku wejściowym **MUSZĄ** być oddzielone spacją. W innym przypadku program nie zadziała.
- Uwaga! Plik z danymi wynikowymi może nie zapisywać się w tym samym folderze w którym znajduję się skrypt! Wtedy należy szukać pliku w C:\Users\ <nazwa_użytkownika>
- Transformacje BL-PL2000 i BL-PL1992 nie poda poprawnych wyników dla elipsoidy Krasowskiego i nie powinny być używane
- Wywołanie programu jest to możliwe tylko wtedy gdy uzytkowink ma powiazany typ plików pythonowych (.py) z programem "python launcher"



