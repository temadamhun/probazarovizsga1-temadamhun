# 3 Feladat: Timesheet automatizálása

Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ. 

A program töltse be a timesheet app-ot az [https://witty-hill-0acfceb03.azurestaticapps.net/timesheet.html](https://witty-hill-0acfceb03.azurestaticapps.net/timesheet.html) oldalról.

Feladatod, hogy automatizáld selenium webdriverrel a Timesheet  app tesztelését.

Az ellenőrzésekhez __NEM__ kell teszt keretrendszert használnod (mint pl a pytest).
Egyszerűen használj elágazásokat vagy `assert` összehasonlításokat.

# Az alábbi tesztesetekete fedd le:

## TC01: üres kitöltés helyessége
* ha nincs kitoltve az e-mail mező nem lehet megnyomni a "next" feliratú gombot
* ha helytelen (formailag helytelen) e-mailcimmel probáljuk kitölteni a formot nem lehet megnyomni a "next" feliratú gombot

## TC02: helyes kitöltés helyes köszönet képernyő
* töltsük ki a következő adatokkal a formot:
    * test@bela.hu
    * 2 hours and 0 minutes
    * working hard
    * types of work: Time working on visual effects for movie
* nyomjuk meg a "next" feliratú gombot
* ellenőrizzük a megjelenő tartalomban az órák és percek helyességét


### A megoldás beadása
* a megoldásokat a `testproject` mappába tedd, `timesheet.py`
* a lokálisan kidolgozott megoldásokat előbb commitold `git commit`
* majd ne felejtsd el `git push` segítségével a Github szerverre is felküldeni
* ne felejtsd el, hogy pontokat ér a szintaktikai legjobb praktikák megvalósítása (`ctlr`+`alt`+`l`)
* akkor is add be megodásod, ha nem vagy benne biztos, mert részpontokat ér mindennemű a tárgyhoz kötődő kód beadása
* a megodás fájlba írjál kommentet amiben elmagyarázod, hogy mit akartál csinálni. Ne vidd túlzásba, de ne is legyen komment nélkül leadott fájlod.
* nem beadott vagy üres fálj formájában beadott feladat megoldás `0` pontot ér :(