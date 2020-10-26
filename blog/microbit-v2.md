------------------------------
Title: BBC micro:bit verzia 2
Summary: Pred pár dňami Micro:bit Educational Foundation verejnila novú
         verziu populárneho micro:bitu, ktorá obsahuje niekoľko nových funkcií.
Author: Marek Mansell
Bio: <a href="//marekmansell.sk">Marek Mansell</a> je zanieteným edukátorom, organizátorom a experimentátorom. Pracuje na projekte Učíme s Hardvérom,
     spoluorganizuje PyCon SK, študuje na FIIT STU a pomáha s produkciou na Festivale Atmosféra.
Date: 26.10.2020
Hidden: False
---------------------------

Pred pár dňami [Micro:bit Educational Foundation](https://microbit.org/new-microbit/) zverejnila novú verziu populárneho micro:bitu, ktorá obsahuje niekoľko nových funkcií. To samozrejme ale prinieslo množstvo otázok súvisiacich s prechodom na novú verziu micro:bitu, ktoré sa pokúsim zopovedať v tomto príspevku.

### Čo nové prináša micro:bit V2?

Začnime s tým, aké nové funkcie micro:bit V2 ponúka. Sú to najmä:

- Integrovaný reproduktor na prehrávanie melódií
- Integrovaný mikrofón (rozpoznáva úroveň hluku v okolí)
- Logo micro:bitu vie rozpoznávať dotyk prstom (slúži ako "tretie tlačidlo")
- Nový energiu šetriaci mód, vďaka ktorému je možné nechať pripojené batérie
- 3.3V regulátor dokáže poskytnúť až 200mA prúdu pre pripojené zariadenia
- Viac RAM aj Flash pamäte

Nový micro:bit má aj zopár "kozmetických" zmien -- napríklad "vykrajované" kolíky či zvýraznenú anténu na Bluetooth komunikáciu. Podrobnú špecifikáciu nájdete [tu.](https://tech.microbit.org/hardware/)

![Zdroj: [Micro:bit Educational Foundation](https://microbit.org/new-microbit/)](images/microbit-v2.png)

### Budú na novom micro:bite fungovať programy a hardvérové doplnky pre pôvodný micro:bit?

**Áno, všetky existujúce programy budú fungovať aj na novom micro:bite.** Ak ale máte na počítači uložené *.hex* súbory, tak ich budete musieť nahrať naspäť do prostredia *MakeCode* a stiahnuť si novo vygenerovaný *.hex* súbor. Tento novo stiahnutý súbor bude fungovať aj na pôvodnom micro:bite aj na novom micro:bite. To isté platí aj pre *online Python editor*.

Čo sa týka hardvérových doplnkov, tam dosiahnuť sto percentnú kompatibilitu môže byť náročnejšie, nakoľko takéto doplnky sú vyrábané desiatkami rôznych výrobcov. Cieľom Micro:bit Educational Foundation je, aby pre pôvodné micro:bity fungovalo všetko tak, ako doteraz.

### Čo ak mám pôvodné micro:bity?

Prirodzene sa vynára otázka, čo robiť, ak máte zakúpené pôvodné micro:bity. V skratke -- nemusíte robiť vôbec nič. Pôvodný micro:bit bude stále plne funkčný, všetko, čo sa s ním dalo robiť doteraz bude fungovať naďalej. Zároveň k nemu existuje obrovské množstvo návodov, videí a metodík, čiže v niektorých prípadoch môže byť ešte vhodnejší, ako nový micro:bit.

Kým nový micro:bit ponúka niekoľko vylepšení a nových funkcií, žiadne z nich nie sú až tak zásadné, aby znamenali, že musíte nevyhnutne prejsť na nový micro:bit. Napríklad v prípade prehrávania hudby je možno ešte vhodnejšie (a hlavne názornejšie) pre žiakov, ak si pomocou krokosvorkových káblikov pripoja externý reproduktor a tým sa naučia, ako funguje 3,5mm JACK.

### Strojové učenie a Umelá inteligencia

Vďaka rozšírenej RAM a Flash pamäti bude na micro:bite možné robiť "náročnejšie" aktivity, ako napríklad strojové učenie či umelú inteligenciu. K tomuto ale Micro:bit Educational Foundation ešte nezverenila podrobnejšie informácie, môžeme ich čakať až v priebehu roka 2021. Predpokladám však, že takéto aktivity sa budú týkať najmä stredných škôl.

### Zhrnutie
Napriek nadšeniu z novej verzie táto zmena ovplyvní výučbu s micro:bitmi na základných školách iba minimálne. Na stredných školách bude citelnejšia zmena iba v prípade, ak sa rozhodnete časom robiť so žiami strojové učenie alebo umelú inteligenciu, ktorých podoby sú ale teraz ešte neznáme.

Ak máte akékoľvek ďalšie otázky, neváhajte sa ich spýtať na [forum.python.sk](https://forum.python.sk/)


![Predná strana pôvodného a nového micro:bitu. Zdroj: [Micro:bit Educational Foundation](https://microbit.org/new-microbit/)](images/microbit-v2-front.png)
![Zadná strana pôvodného a nového micro:bitu. Zdroj: [Micro:bit Educational Foundation](https://microbit.org/new-microbit/)](images/microbit-v2-back.png)
![Porovnanie pôvodného a nového micro:bitu. Zdroj: [Micro:bit Educational Foundation](https://microbit.org/new-microbit/)](images/microbit-v2-chart.png)
