# Kirjastosovellus
Sovelluksen tarkoituksena on simuloida verkkokirjaston toimintoja. Tavalliset käyttäjät voivat hakea ja varata aineistoa sekä kirjoittaa ja selata arvosteluja. Ylläpitäjät voivat lisätä uutta aineistoa sekä hallinnoida lainausoikeuksia. 

Sovelluksella on seuraavat ominaisuudet:

- Sovelluksessa näkyy kirjaston aineisto. Käyttäjä voi etsiä tietoa teoksista, varata teoksia ja lukea niistä arvosteluja. Jokainen käyttäjä on peruskäyttäjä tai ylläpitäjä.

- Käyttäjä voi kirjautua sisään ja ulos sekä rekisteröityä palveluun.

- Käyttäjä voi teosta nimen, tekijän, kielen tai julkaisuvuoden perusteella. Hakutulosta klikkaamalla teoksesta näytetään lisää tietoja.

- Käyttäjä voi antaa arvion (arvosana 1-5 ja kommentti) teoksesta ja lukea muiden antamia arvioita.

- Käyttäjä voi varata teoksen ja selata omia varauksiaan. Jos teokseen on varauksia, sen saatavuustiedot päivittyvät. Teos ei ole saatavilla, jos siihen tulee varauksia.

- Ylläpitäjä voi lisätä ja poistaa teoksia sekä määrittää niistä näytettävät tiedot.

- Ylläpitäjä voi poistaa käyttäjän antaman arvion.

- Ylläpitäjä voi ottaa pois käyttäjän lainausoikeuden, mikä estää myös teoksen varaamisen.

Tällä hetkellä sovellukseen on toteutettu rekisteröityminen ja sisäänkirjautuminen, haku- ja arvostelutoiminto, omien varauksen tarkastelu sekä lainausoikeuden poistamisen mahdollistava toiminto. Tarkoituksena on vielä parantaa hakutoimintoa, sillä tällä hetkellä hakusanoina toimivat vain teoksen nimi, kirjailija tai kieli yksinään (esim. hakusanat 'tove jansson' tai 'suomi'). Sovellukseen on toteutettava myös ylläpitäjän mahdollisuus poistaa aineistoa ja arvioita. Lisäksi sovelluksen ulkoasua tullaan vielä kehittämään.

Sovelluksen Heroku-osoite: https://fierce-everglades-26533.herokuapp.com/
