# CarTrade
CarTrade je web aplikacija za praćenje lagera u prodavaonici rabljenih automobila.
## Funkcionalnosti
### Osnovne funkcionalnosti
1. Dodaj automobil
2. Pogledaj automobile
3. Uredi automobil
4. Izbriši automobil
### Dodatne funkcionalnosti
1. Sortiranje prema marki
2. Sortiranje prema modelu
3. Sortiranje prema godini
4. Sortiranje prema cijeni


----
## Struktura
Omogućeno je dodavanje, pregledavanje, izmjenjivanje te brisanje automobila, sortiranje prema marki, modelu, godini proizvodnje i cijeni. 

----
## Pokretanje
- Preuzeti sve datoteke s Githuba i spremiti ih u mapu
- Putem naredbenog retka pozicionirati se u mapu iz prethodnog koraka
- Pomoću naredbe: _docker build -t cartrade ._ izraditi docker image
- Pomoću naredbe: _docker run -p 5000:8080 cartrade_ pokrenuti konteiner pomoću stvorenog image-a
- Otvoriti preglednik: _localhost:5000_
