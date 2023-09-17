"""

    Spočítej, kolik procent podstatných jmen ženského rodu se řídí popsaným pravidlem, tj. množné 
    číslo má na konci "en". Nezapomeň do výpočtu zahrnout pouze podstatná jména v ženském rodě. 
    K výpočtu použij vzorová data níže.
    
    Vypiš podstatná jména, která toto pravidlo porušují. Objasní ti to i zvláštní název tohoto 
    cvičení.

"""
data = [
    "die Auslieferung;die Auslieferungen",
    "die Botschaft;die Botschaften",
    "die Vereinbarung;die Vereinbarungen",
    "die Spannung;die Spannungen",
    "die Gefolgschaft;die Gefolgschaften",
    "die Wurzel;die Wurzeln",
    "die Wache;die Wachen",
    "die Drohung;die Drohungen",
    "die Vermittlung;die Vermittlungen",
    "die Gelegenheit;die Gelegenheiten",
    "die Sphäre;die Sphären",
    "die Spaltung;die Spaltungen",
    "die Gewalt;die Gewalten",
    "die Lust;die Lüste",
    "die Bedrohung;die Bedrohungen",
    "die Richtung;die Richtungen",
    "die Küste;die Küsten",
    "die Gebärde;die Gebärden",
    "die Übung;die Übungen",
    "die Fremdsprache;die Fremdsprachen",
    "die Wendung;die Wendungen",
    "die Grundlage;die Grundlagen",
    "die Beziehung;die Beziehungen",
    "die Einhaltung;die Einhaltungen",
    "die Pflicht;die Pflichten",
    "die Strafmaßnahme;die Strafmaßnahmen",
    "die Lesart;die Lesarten",
    "die Anzeige;die Anzeigen",
    "die Sorge;die Sorgen",
    "das Unbehagen;die Unbehagen",
    "die Einsetzung;die Einsetzungen",
    "die Sperrung;die Sperrungen",
    "die Abschaffung;die Abschaffungen",
    "die Beschränkung;die Beschränkungen",
    "die Ausfuhr;die Ausfuhren",
    "die Entspannung;die Entspannungen",
    "die Empörung;die Empörungen",
    "die Nachfrage;die Nachfragen",
    "die Notwendigkeit;die Notwendigkeiten",
    "die Größe;die Größen",
    "die Schuld;die Schulden",
    "die Aufregung;die Aufregungen",
    "die Voraussetzung;die Voraussetzungen",
    "die Wahl;die Wahlen",
    "die Absage;die Absagen",
    "die Zugehörigkeit;die Zugehörigkeiten",
    "der Nachmittag;die Nachmittage",
    "die Notlage;die Notlagen",
    "die Absetzung;die Absetzungen",
    "die Anlehnung;die Anlehnungen",
    "die Einschüchterung;die Einschüchterungen",
    "die Leitung;die Leitungen",
    "die Beratung;die Beratungen",
    "die Volksabstimmung;die Volksabstimmungen",
    "die Unterstützung;die Unterstützungen",
    "die Überraschung;die Überraschungen",
    "die Zustimmung;die Zustimmungen",
    "die Anerkennung;die Anerkennungen",
    "die Fähigkeit;die Fähigkeiten",
    "die Fahne;die Fahnen",
    "der Widerstand;die Widerstände",
    "die Stellung;die Stellungen",
    "die Einnahme;die Einnahmen",
    "der Zwischenfall;die Zwischenfälle",
    "die Fluggesellschaft;die Fluggesellschaften",
    "der Notruf;die Notrufe",
    "die Gemeinsamkeit;die Gemeinsamkeiten",
    "die Anforderung;die Anforderungen",
    "die Zulässigkeit;die Zulässigkeiten",
    "der Zuschuss;die Zuschüsse",
    "die Fernstraße;die Fernstraßen",
    "die Verzögerung;die Verzögerungen",
    "die Sanierung;die Sanierungen",
    "die Instandhaltung;die Instandhaltungen",
    "die Zuspitzung;die Zuspitzungen",
    "die Angliederung;die Angliederungen",
    "das Schild;die Schilder",
    "die Behauptung;die Behauptungen",
    "der Schub;die Schübe",
    "die Stellungnahme;die Stellungnahmen",
    "die Frist;die Fristen",
    "die Behandlung;die Behandlungen",
    "die Übereinstimmung;die Übereinstimmungen",
    "die Einrichtung;die Einrichtungen",
    "die Notenbank;die Notenbanken",
    "die Offenbarung;die Offenbarungen",
    "die Verfolgung;die Verfolgungen",
    "die Flut;die Fluten",
    "die Verhandlung;die Verhandlungen",
    "die Umfrage;die Umfragen",
    "die Erleichterung;die Erleichterungen",
    "die Einmischung;die Einmischungen",
    "die Erhebung;die Erhebungen",
    "die Festnahme;die Festnahmen",
    "der Schlüssel;die Schlüssel",
    "die Gabel;die Gabeln",
    "die Steigerung;die Steigerungen",
    "der Sohn;die Söhne",
    "die Wende;die Wenden",
    "die Bürgschaft;die Bürgschaften",
]

feminum = 0
regular = 0


for word in data:
    if word[:3] == "die":
        feminum += 1
        if word [-2:] == "en":
            regular += 1
        else:
            print(word)    

percentage = regular/feminum * 100

print(round(percentage,2))

