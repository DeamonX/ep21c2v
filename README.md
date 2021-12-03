# Feladat megoldása és benyújtás

1. Nyissa meg:
   1. _VCS / Get from Version Control..._ VAGY
   2. _Git / Clone..._
2. A _Get From Version Control_ ablakban adja meg a jelen repository URL-jét: https://github.com/csekok/ep21c2v.git
3. Kattintson a _Clone_ gombra.
4. Válassza a _Git / GitHub / Share Project on GitHub_ lehetőséget.
5. Kattintson a _Project Is Already on GitHub_ ablakban a _Share Anyway_ gombra.
6. Kattintson a _Share Project On GitHub_ ablakban a _Share_ gombra.
7. A feladat megoldására 3 óra áll rendelkezésre.
8. A feladat befejezésekor, de legkésőbb a 3. óra leteltekor kommitolja fel a megoldást.

# Feladatkiírás

Egy aprócikk boltban minden árucikk darabja 1000 Ft. Ha egy vásárlás során valaki egy adott árucikkből több darabot
is vesz, a második ára már csak 900 Ft, a harmadik és minden további darab pedig 800 Ft. Tehát a harmadik ugyanolyan
cikk vásárlása után már nem csökken tovább az ár.

A vásárlók kosarában legalább 1 termék van. A kosarak tartalmát a _kosar.txt_ fájl írja le, amelyben
soronként egy-egy árucikk neve vagy az F karakter szerepel. A fájlban legfeljebb 2000 sor lehet. Az F karakter jelzi,
ha a vásárló kosarában nincs több árucikk, a fizetés következik. Az árucikk neve akár több szóból is állhat.

Példa a _kosar.txt_ fájl első néhány sorára:
<pre>
toll
F
colostok
HB ceruza
HB ceruza
colostok
toll
szatyor
csavarkulcs
doboz
F
</pre>

A példa alapján az első vásárló összesen 1 tollat vásárolt, ezért összesen 1000 Ft-ot kell fizetnie. A második vásárló
hatféle árucikket vásárolt (HB ceruzából és colostokból többet is) összesen 7800 Ft értékben.

Írjon programot az alábbi feladatok megoldására:
1. Olvassa be és tárolja el a _kosar.txt_ tartalmát!
2. Határozza meg, hányszor fizettek a pénztárnál!
3. Kérje be a felhasználótól egy vásárlás sorszámát! Írassa ki:
   - hány darab árucikk volt a kosárban,
   - mely árucikkekből és milyen mennyiségben vásároltak,
   - a vásárlás összegét.
4. Kérje be a felhasználótól egy árucikk nevét! Határozza meg, melyik vásárlásnál vettek először, melyiknél utoljára
és összesen hány alkalommal vásároltak az árucikkből!
5. Készítsen _osszeg.txt_ néven fájlt, ami soronként tartalmazza egy-egy vásárlás alkalmával fizetendő összeget!


A programnak 3 modulból kell állnia:
   1. _kosar_: Az egyes vásárlások kezelését biztosító _Kosar_ osztályt tartalmazza.
      - Az osztály attribútumai:
         - _termekek_: a kosárban lévő árucikkek (név-mennyiség párok)
         - _osszeg_: a vásárlás összege
      - Az osztály metódusai:
         - \_\__init_\_\_: A kosár létrehozásakor beállítja az osztály attribútumait.
         - _osszeg_lekerdezese_: A vásárlás összegének lekérdezése.
         - _termekek_lekerdezese_: Az árucikk-mennyiség párok lekérdezése.
         - _termekek_szamanak_lekerdezese_: A kosárban lévő termékek számának lekérdezése.
         - _arucikk_mennyisegenek_lekerdezese_: Egy árucikknek a kosárban megtalálható mennyiségének lekérdezése.
         - _kosar_tartalmanak_kiiratasa_: Kiírja a kosár tartalmát a konzolra.
   2. _bolt_: Az összes vásárlást összefogó _Bolt_ osztályt tartalmazza.
      - Az osztály egyetlen attribútuma a kosarak listája.
      - Az osztály metódusai:
         - \_\__init_\_\_: A kosár létrehozásakor beállítja az osztály attribútumait.
         - feladat_1: 1. feladat megoldása.
         - feladat_2: 2. feladat megoldása.
         - feladat_3: 3. feladat megoldása.
         - feladat_4: 4. feladat megoldása.
         - feladat_5: 5. feladat megoldása.
   3. _main_: A _bolt_ modul függvényeinek meghívását tartalmazza.

## Megoldás közben ügyeljen az alábbiakra

- **Az előre megírt metódusok mellé tetszőleges mennyiségű saját metódusokat írhat, ha szükségesnek látja!**
- A képernyőre írást igénylő részfeladatok eredményének megjelenítése előtt írja a képernyőre a feladat sorszámát!
- Ha a felhasználótól kér be adatot, jelenítse meg a képernyőn, milyen értéket vár!
- Ellenőrizze a felhasználó által megadott adatok helyességét, érvényességét!

## Minta a szöveges kimenetek kialakításához

A képernyőre írást nem igénylő feladatok esetén nem szükséges a feladat sorszámát sem kiíratnia.

### Teszteset 1

<pre>
1. feladat: A kosar.txt beolvasása.
2. feladat: 141 alkalommal fizettek a pénztárnál.
3. feladat: Adja meg a vásárlás sorszámát: 1
1 termék volt a kosárban.
A kosár tartalma:
    1 toll

A vásárlás összege: 1000 Ft
4. feladat: Adja meg az árucikk nevét: kefe
Első vásárlás sorszáma: 5
Utolsó vásárlás sorszáma: 139
32 alkalommal vásároltak az árucikkből.
5. feladat: A vásárlások összegének mentése az osszeg.txt fájlba.
</pre>

### Teszteset 2

<pre>
1. feladat: A kosar.txt beolvasása.
2. feladat: 141 alkalommal fizettek a pénztárnál.
3. feladat: Adja meg a vásárlás sorszámát: 142
Nem volt ilyen sorszámmal vásárlás.
4. feladat: Adja meg az árucikk nevét: csavar
Nem vásároltak ebből a termékből.
5. feladat: A vásárlások összegének mentése az osszeg.txt fájlba.
</pre>

### Teszteset 3

<pre>
1. feladat: A kosar.txt beolvasása.
2. feladat: 141 alkalommal fizettek a pénztárnál.
3. feladat: Adja meg a vásárlás sorszámát: elso
Nem volt ilyen sorszámmal vásárlás.
4. feladat: Adja meg az árucikk nevét: HB ceruza
Első vásárlás sorszáma: 2
Utolsó vásárlás sorszáma: 137
39 alkalommal vásároltak az árucikkből.
5. feladat: A vásárlások összegének mentése az osszeg.txt fájlba.
</pre>

### Példa az _osszeg.txt_ fájl első néhány sorára:

<pre>
1000
7800
4600
2000
5000
5800
</pre>
