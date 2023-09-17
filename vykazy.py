"""
Data obsahují pracovní výkazy 5 zaměstnanců za srpen 2023. Pro každý pracovní den jsou v datech následující informace:

    date - datum,
    employee - jméno zaměstnance/zaměstnankyně,
    drecord_typeate - typ záznamu, který říká, co zaměstnanec/zaměstnankyně daný den dělal(a), možnosti jsou: "work" (práce), "holiday" (dovolená), "care" (péče o člena rodiny), "unpaid" (neplacené volno),
    worked_on - pokud je typ záznamu "work", je tam vnořený slovník s počty odpracovaných hodin na jednotlivých projektech.

U záznaů typu dovolená, péče o člena rodiny nebo neplacené volno vždy uvažujeme délku 8 hodin. Pokud zaměstnanec pracoval, jsou odpracované hodiny dané součtem práce na jednotlivých projektech a může to být jiné číslo než 8.

Tvým úkolem je vytvořit dva reporty: report o odpracovaných hodinách a absencích každého zaměstnance a report odpracované práce na projektu.

Začnemě s reportem o zaměstnancích. Vstupem pro něj je zbývající dovolená, tj. nárok na dovolenou, který ještě zaměstnanci v tomto kalendářním roce nevyčerpali. Podle nového zákoníku práce je nárok v hodinách.

remaining_holiday = {"Marta Nováková": 120, "Michael Rostock-Poplar": 96, "Ondřej Bartoš": 40, "Daniela Bérová": 168, "Ivan Pilný": 32}

Tvým úkolem je spočítat pro každého zaměstnance (zaměstnankyni):

    kolik odpracoval(a) hodin,
    kolik si vybral(a) dovolené (v hodinách),
    kolik zbývá dovolené na konci září,
    kolik hodin strávil(a) péčí o člena rodiny,
    kolik hodin strávil na neplaceném volnu.
"""

import json

with open('work_hours.json', encoding = 'utf-8') as file:
    data = json.load(file)

remaining_holiday = {"Marta Nováková": 120, "Michael Rostock-Poplar": 96, "Ondřej Bartoš": 40, "Daniela Bérová": 168, "Ivan Pilný": 32}

report = {}
report_project = {}
report_project_employee = {}

for line in data:
    employee = line['employee']
    if employee not in report:
        report[employee] = {"work_hours": 0, "holiday_taken": 0, "holiday_remaining": remaining_holiday[employee], "care": 0, "unpaid": 0}
    

    if line['employee'] == employee and line["record_type"] == "holiday":
        report[employee]['holiday_taken'] += 8
        report[employee]['holiday_remaining'] -= 8
    elif line['employee'] == employee and line["record_type"] == "care":
        report[employee]['care'] += 8
    elif line['employee'] == employee and line["record_type"] == "unpaid":
        report[employee]['unpaid'] += 8
    else:
        for project in line['worked_on']:
            if project not in report_project:
                report_project[project] = 0
                report_project_employee[project] = {}
                print(report_project_employee)
            if employee not in report_project_employee[project]:
                report_project_employee[project][employee] = 0
                print(report_project_employee)

            report[employee]['work_hours'] += line['worked_on'][project]
            report_project[project]  += line['worked_on'][project]
            report_project_employee[project][employee] += line['worked_on'][project]

print(report)
print(report_project)
print(report_project_employee)

  





