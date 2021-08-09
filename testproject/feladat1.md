## 1 Feladat: Hogwards express jegyautomata

A Hogwards express nemrég rájött, hogy érdemes lenne önkiszolgálóvá tenni a jegykiállító rendszert a hallgatók
vasútvonalán. Lehet, hogy drágák a baglyok.

Itt találod az önkiszolgáló webes applikáció prototípusát:
[https://witty-hill-0acfceb03.azurestaticapps.net/hogwards.html](https://witty-hill-0acfceb03.azurestaticapps.net/hogwards.html)

Készíts egy Python python applikációt (akár csak egy darab python fileban) ami selenium-ot használ.

Teszteld le, hogy az általad megadott adatokkal tölti-e ki a jegyet az applikáció. (vigyázz, mert elkézpelhető, hogy némely adatokat egynél több helyen is megjeleníti a jegyen az applikáció)

Nem kell negatív tesztesetet készítened. Egy pozitív teszteset teljesen elég lesz.

Az ellenőrzésekhez __NEM kell__ teszt keretrendszert használnod (mint pl a pytest). Egyszerűen használj elágazásokat
__NEM kell__ OOP-t használnod. Viszont tartalmazzon vizsgálatot a megodásod. Lehetőleg használj az `assert` összehasonlításokat.

### A megoldás beadása

* a megoldásokat a `testproject` mappába tedd, `hogwards.py`
* a lokálisan kidolgozott megoldásokat előbb commitold `git commit`
* majd ne felejtsd el `git push` segítségével a Github szerverre is felküldeni
* ne felejtsd el, hogy pontokat ér a szintaktikai legjobb praktikák megvalósítása (`ctlr`+`alt`+`l`)
* akkor is add be megodásod, ha nem vagy benne biztos, mert részpontokat ér mindennemű a tárgyhoz kötődő kód beadása
* a megodás fájlba írjál kommentet amiben elmagyarázod, hogy mit akartál csinálni. Ne vidd túlzásba, de ne is legyen
  komment nélkül leadott fájlod.
* nem beadott vagy üres fálj formájában beadott feladat megoldás `0` pontot ér :(
{"mode":"full","isActive":false}