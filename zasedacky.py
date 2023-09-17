"""
Naše společnost má aktuálně kanceláře se 4 zasedačkami: Forman, Vlasy, Goya a Amadeus. Aktuálně 
plánuje stěhování do nových prostor a řeší, kolik zasedacích místností by tam mělo být. Proto chce 
spočítat, jak moc jsou v současnosti zasedačky využívané.

Níže máš přehled naplánovaných meetingů v jednotlivých zasedačkách během jednoho vybraného dopoledne. 
Každý meeting trvá právě jednu hodinu, začíná v celou hodinu (např. v 8:00). Tvým úkolem je spočítat 
pro každou hodinu vypsat počet volných zasedaček.
"""

meetingy = [
    ["8:00-8:59", "Forman", "Pravidelný meeting managementu"],
    ["8:00-8:59", "Vlasy", "Plánování vánočního večírku"],
    ["9:00-9:59", "Forman", "Setkání se zákazníkem - Macromo"],
    ["9:00-9:59", "Amadeus", "Pohovor - paní Řeháková"],
    ["9:00-9:59", "Goya", "Příprava marketingové kampaně"],
    ["9:00-9:59", "Vlasy", "Plán cash-flow"],
    ["10:00-10:59", "Forman", "Pohovor - paní Hrachovcová"],
    ["10:00-10:59", "Goya", "Setkání se zákazníkem - Livesport"],
    ["11:00-11:59", "Amadeus", "Stěhování - plánování prohlídek"],
    ["11:00-11:59", "Forman", "Scrum - Python tým"],
    ["11:00-11:59", "Goya", "Pohovor - paní Halasová"],
]

free = [4,4,4,4]

for meeting in meetingy:
    hour = meeting[0].split(":")[0]
    index = int(hour) - 8
    free[index] -= 1

print(free)

