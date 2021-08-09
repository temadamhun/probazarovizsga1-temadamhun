# 2 Feladat: Sales tax applikáció funkcióinak automatizálása

Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ. 

A program töltse be a sales tax app-ot az [https://witty-hill-0acfceb03.azurestaticapps.net/salestax.html](https://witty-hill-0acfceb03.azurestaticapps.net/salestax.html) oldalról.

Feladatod, hogy automatizáld selenium webdriverrel a sales tax kalkulátort.

# Az alábbi tesztesetekete fedd le:

## TC01: üres kitöltés helyessége
* nem kell ellenőrizni, hogy üresek-e a mezők, csak azt, hogy alapból a "Subtotal" feliratú gomb megnyomásakor a `salestax` azonosítójú mező 0.00 értéket kell mutasson.
* illetve a "Calculate Order" gomb megyomására a `gtotal` mező 4.95 értéket kell mutasson

## TC02: 6" x 6" Volkanik Ice kitöltés helyessége
* válasszuk ki a Product Item feliratú mezőből a `6" x 6" Volkanik Ice` értéket
* a quantity feliratú mezőbe írjunk 1-et
* ellenőrizzük, hogy a "Subtotal" feliratú gomb megnyomásakor a `salestax` azonosítójú mező 4.95 értéket kell mutasson.
* illetve a "Calculate Order" gomb megyomására a `gtotal` mező 9.90 értéket kell mutasson

Az ellenőrzésekhez __NEM__ kell teszt keretrendszert használnod (mint pl a pytest).
Egyszerűen használj elágazásokat vagy `assert` összehasonlításokat.


### A megoldás beadása
* a megoldásokat a `testproject` mappába tedd, `salestax.py`
* a lokálisan kidolgozott megoldásokat előbb commitold `git commit`
* majd ne felejtsd el `git push` segítségével a Github szerverre is felküldeni
* ne felejtsd el, hogy pontokat ér a szintaktikai legjobb praktikák megvalósítása (`ctlr`+`alt`+`l`)
* akkor is add be megodásod, ha nem vagy benne biztos, mert részpontokat ér mindennemű a tárgyhoz kötődő kód beadása
* a megodás fájlba írjál kommentet amiben elmagyarázod, hogy mit akartál csinálni. Ne vidd túlzásba, de ne is legyen komment nélkül leadott fájlod.
* nem beadott vagy üres fálj formájában beadott feladat megoldás `0` pontot ér :(