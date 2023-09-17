
# Kryptoměny

# Markéta má své úspory ve třech kryptoměnách: Czechitacoinu, Polcoinu a PyCoinu. Potřebovala by 
# zjistit, kolik je celková hodnota jejích úspor v celých dolarech. Bohužel její aplikace toto 
# zobrazit neumí, má pouze k dispozici přehled všech transakcí, které jsou v souboru transaction_list.csv. 
# V prvním sloupci je datum transakce, ve druhém sloupci hodnota transakce a ve třetím sloupci 
# kryptoměna, ve které transakce proběhla. Níže máš slovník s aktuáními kurzy těchto měn v dolarech. 
# Zápis znamená, že 1 Polcoin má hodnotu 0.47 dolarů, 1 PyCoin 0.21 dolarů atd.


rates = {"Polcoin": 0.47, "PyCoin": 0.21, "Czechitacoin": 0.13}

Czechitacoin = 0
Polcoin = 0
PyCoin = 0

with open('transaction_list.csv', encoding='utf-8') as file:
    zaznamy = file.read().splitlines()

for polozka in zaznamy:
    polozka = polozka.split(';')
    if polozka[2] == 'PyCoin':
        PyCoin += float(polozka[1])
    elif polozka[2] == 'Czechitacoin':
        Czechitacoin += float(polozka[1])
    else:
        Polcoin += float(polozka[1])

hodnota_PyCoin =  rates['PyCoin'] * PyCoin
hodnota_Czechitacoin =  rates['Czechitacoin'] * Czechitacoin
hodnota_Polcoin = rates['Polcoin'] * Polcoin

hodnota_celkem = hodnota_Czechitacoin + hodnota_PyCoin + hodnota_Polcoin

print(f'Hodnota uspor je {round(hodnota_celkem)} dolaru.')