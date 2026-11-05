'''
Das Programm 'Kurs -und Prüfungsverwaltung' wurde als Gruppenprojekt für den Kurs 'Grundlagen Programmierung' entwickelt.
Ziel war es Studierende und Ergebnisse zweier Prüfungsbestandteile zu verwalten.

Es wurden folgende fachlichen Regeln beachtet:
    - Projektpunkte und Klausurpunkt liegen zwischen 0 und 50. Außerdem dürfen die Punkte nur ganze Zahlen sein
    - Gesamtpunktzahl setzt sich aus der Summe der Projekt -und Klausurpunkte und beträgt maximal 100
    - Prüfung ist nur bestanden, wenn die Gesamtpunktzahl mindestens 50 Punkte beträgt, wobei die Klausurpunktzahl mindestens 25 Punkte betragen muss
    - Fehlende Prüfungsbestandteile werden als fehlender Dictionary-Schlüssel dargestellt, nicht als None. Solche Datensätze gelten als unvollständig und werden aus Durchschnitt, Bestehensquote und Notenverteilung ausgeschlossen
'''


#Vorgegebener Datensatz mit fiktiven Studenten
studierende = [
 {'id': 101, 'name': 'Anna', 'projekt': 17, 'klausur': 23},
 {'id': 102, 'name': 'David', 'projekt': 24, 'klausur': 34},
 {'id': 103, 'name': 'Sara', 'projekt': 31, 'klausur': 45},
 {'id': 104, 'name': 'Max', 'projekt': 38, 'klausur': 5},
 {'id': 105, 'name': 'Lena', 'projekt': 45, 'klausur': 16},
 {'id': 106, 'name': 'Jonas', 'projekt': 1, 'klausur': 27},
 {'id': 107, 'name': 'Mira', 'projekt': 8, 'klausur': 38},
 {'id': 108, 'name': 'Leon', 'projekt': 15, 'klausur': 49},
 {'id': 109, 'name': 'Nora', 'projekt': 22, 'klausur': 9},
 {'id': 110, 'name': 'Emil', 'projekt': 29, 'klausur': 20},
 {'id': 111, 'name': 'Sofia', 'projekt': 36, 'klausur': 31},
 {'id': 112, 'name': 'Paul', 'projekt': 43, 'klausur': 42},
 {'id': 113, 'name': 'Maja', 'projekt': 50, 'klausur': 2},
 {'id': 114, 'name': 'Felix', 'projekt': 6, 'klausur': 13},
 {'id': 115, 'name': 'Clara', 'projekt': 13, 'klausur': 24},
 {'id': 116, 'name': 'Tim', 'projekt': 20, 'klausur': 35},
 {'id': 117, 'name': 'Laura', 'projekt': 27, 'klausur': 46},
 {'id': 118, 'name': 'Noah', 'projekt': 36},
 {'id': 119, 'name': 'Marie', 'projekt': 41, 'klausur': 17},
 {'id': 120, 'name': 'Ben', 'projekt': 48, 'klausur': 28},
 {'id': 121, 'name': 'Anna', 'projekt': 4, 'klausur': 39},
 {'id': 122, 'name': 'David', 'projekt': 11, 'klausur': 50},
 {'id': 123, 'name': 'Sara', 'projekt': 18, 'klausur': 10},
 {'id': 124, 'name': 'Max', 'projekt': 25, 'klausur': 21},
 {'id': 125, 'name': 'Lena', 'projekt': 32, 'klausur': 32},
 {'id': 126, 'name': 'Jonas', 'projekt': 39, 'klausur': 43},
 {'id': 127, 'name': 'Mira', 'projekt': 46, 'klausur': 3},
 {'id': 128, 'name': 'Leon', 'projekt': 2, 'klausur': 14},
 {'id': 129, 'name': 'Nora', 'projekt': 9, 'klausur': 25},
 {'id': 130, 'name': 'Emil', 'projekt': 16, 'klausur': 36},
 {'id': 131, 'name': 'Sofia', 'projekt': 23, 'klausur': 47},
 {'id': 132, 'name': 'Paul', 'projekt': 30, 'klausur': 7},
 {'id': 133, 'name': 'Maja', 'projekt': 37, 'klausur': 18},
 {'id': 134, 'name': 'Felix', 'projekt': 44, 'klausur': 29},
 {'id': 135, 'name': 'Clara', 'projekt': 0, 'klausur': 40},
 {'id': 136, 'name': 'Tim', 'projekt': 7, 'klausur': 0},
 {'id': 137, 'name': 'Laura', 'projekt': 14, 'klausur': 11},
 {'id': 138, 'name': 'Noah', 'projekt': 21, 'klausur': 22},
 {'id': 139, 'name': 'Marie', 'projekt': 28, 'klausur': 33},
 {'id': 140, 'name': 'Ben', 'projekt': 35, 'klausur': 44},
 {'id': 141, 'name': 'Anna', 'projekt': 42, 'klausur': 4},
 {'id': 142, 'name': 'David', 'projekt': 49, 'klausur': 15},
 {'id': 143, 'name': 'Sara', 'projekt': 5, 'klausur': 26},
 {'id': 144, 'name': 'Max', 'klausur': 29},
 {'id': 145, 'name': 'Lena', 'projekt': 19, 'klausur': 48},
 {'id': 146, 'name': 'Jonas', 'projekt': 26, 'klausur': 8},
 {'id': 147, 'name': 'Mira', 'projekt': 33, 'klausur': 19},
 {'id': 148, 'name': 'Leon', 'projekt': 40, 'klausur': 30},
 {'id': 149, 'name': 'Nora', 'projekt': 47, 'klausur': 41},
 {'id': 150, 'name': 'Emil', 'projekt': 3, 'klausur': 1},
 {'id': 151, 'name': 'Sofia', 'projekt': 10, 'klausur': 12},
 {'id': 152, 'name': 'Paul', 'projekt': 17, 'klausur': 23},
 {'id': 153, 'name': 'Maja', 'projekt': 24, 'klausur': 34},
 {'id': 154, 'name': 'Felix', 'projekt': 31, 'klausur': 45},
 {'id': 155, 'name': 'Clara', 'projekt': 38, 'klausur': 5},
 {'id': 156, 'name': 'Tim', 'projekt': 45, 'klausur': 16},
 {'id': 157, 'name': 'Laura', 'projekt': 1, 'klausur': 27},
 {'id': 158, 'name': 'Noah', 'projekt': 8, 'klausur': 38},
 {'id': 159, 'name': 'Marie', 'projekt': 15, 'klausur': 49},
 {'id': 160, 'name': 'Ben', 'projekt': 22, 'klausur': 9}]

#Notentabelle mit welcher die Gesamtpunktzahl einer Note zugeordnet werden kann. Anzahl der Studenten gibt an, wie viele diese Punktzahl/Note erreicht haben
notentabelle = [
    {'gesamtpunkte': list(range(95, 101)), 'note': 1.0, 'anzahl_studenten': 0},
    {'gesamtpunkte': list(range(90, 95)), 'note': 1.3, 'anzahl_studenten': 0},
    {'gesamtpunkte': list(range(85, 90)), 'note': 1.7, 'anzahl_studenten': 0},
    {'gesamtpunkte': list(range(80, 85)), 'note': 2.0, 'anzahl_studenten': 0},
    {'gesamtpunkte': list(range(75, 80)), 'note': 2.3, 'anzahl_studenten': 0},
    {'gesamtpunkte': list(range(70, 75)), 'note': 2.7, 'anzahl_studenten': 0},
    {'gesamtpunkte': list(range(65, 70)), 'note': 3.0, 'anzahl_studenten': 0},
    {'gesamtpunkte': list(range(60, 65)), 'note': 3.3, 'anzahl_studenten': 0},
    {'gesamtpunkte': list(range(55, 60)), 'note': 3.7, 'anzahl_studenten': 0},
    {'gesamtpunkte': list(range(50, 55)), 'note': 4.0, 'anzahl_studenten': 0},
    {'gesamtpunkte': list(range(0, 50)), 'note': 5.0, 'anzahl_studenten': 0}]


def pruefe_id(id):
    '''
    Diese Funktion überprüft, ob eine als String eingegebene Studierenden-ID im gültigen Bereich liegt.
    '''

    #Überprüfung, ob der String zu einem INT umgewandelt werden kann
    if (id.isdigit() == False):
        raise TypeError ('Eingabe muss eine Zahl sein')
    
    id_int = int(id)

    #Überprüfung, ob ID im erlaubten Zahlenbereich liegt
    if (id_int < 100 or id_int > 999):
        raise ValueError ("ID muss im dreistelligen Bereich liegen")

    return True


def pruefe_name(name):
    '''
    Funktion die überprüft ob eingetragener Name zulässig ist. Ein Name ist zulässig, falls dieser nur aus mindestens einem Buchstaben besteht. Bindestriche und Leerzeichen für Doppelnamen sind außerdem erlaubt.
    '''

    #Überprüfung ob der Name leer ist
    if name == '':
        raise ValueError("Name darf nicht leer sein")
    
    #Überprüfung ob ungültige Zeichen enthalten
    counter = 0
    for zeichen in name:
        if(zeichen.isalpha()):
            counter += 1
        elif (zeichen != '-' and zeichen != ' '):
            raise ValueError("Der Name darf nur Buchstaben, Leerzeichen und Bindestriche enthalten")

    #Name muss mindestens einen Buchstaben enthalten
    if(counter < 1):
        raise ValueError("Name muss mindestens einen Buchstaben enthalten")
    return True


def pruefe_punktzahl(punktzahl):
    '''
    Funktion die überprüft ob die eingetragene Punktzahl die angegebenen Regeln erfüllt
    '''

    #Punktzahl muss eine ganze Zahl zwischen 0 und 50 sein

    if not (punktzahl.isdigit()) or not (0 <= int(punktzahl) <= 50):
        raise ValueError("Punktzahl ist ungültig. Gültige Werte müssen zwischen 0 und 50 Punkten liegen.")
    else:
        return True


def id_vorhanden(id):
    '''
    Funktion die untersucht, ob eine Studenten-ID bereits in der Liste vorhanden ist
    '''
    try:

        #Gibt es einen Studenten, zu dem die eingegebene ID gehört?
        
        pruefe_id(id)
        for student in studierende:
            if student['id'] == int(id):
                return True
            
        return False

    except Exception as fehler:
        raise ValueError(f'Fehlerhafte Eingabe: {fehler}')


def suche_studenten(eingabe):
    '''
    Funktion, die einen Studenten anhand seiner ID oder seines Namens sucht. Gibt Anzahl der gefundenen Elemente und diese selbst in Form eines Dictionaries zurück
    '''
    
    try:
        #Gibt es einen Studierenden mit dieser ID? -> läuft in den ersten Except-Block, wenn die Eingabe keine gültige ID ist (siehe id_vorhanden())
        vorhanden = id_vorhanden(eingabe)

        #Vorhandenen Studenten zurückliefern, wenn er existiert -> ID ist immer eindeutig
        if vorhanden:
            for student in studierende:
                if student['id'] == int(eingabe):
                    return {'menge': 'eins', 'ergebnis': student}

        #Ansonsten Information zurückgeben, dass kein Student gefunden wurde
        else:
            return {'menge': 'keine', 'ergebnis': 'Kein Student mit dieser ID wurde gefunden.'}
        
    except:
        try:
            #Ist die Eingabe ein gültiger Name? -> läuft in den zweiten Except-Block, wenn die Eingabe keine gültige ID ist (siehe pruefe_name())
            pruefe_name(eingabe)

            #Liste für gefundene Studenten initiieren -> Es kann mehrere Studenten mit demselben Namen geben / es kann nach einem Teil eines Namens gesucht werden
            gefunden = []

            #Alle übereinstimmenden Studenten in die Liste aufnehmen
            for student in studierende:
                if eingabe in student['name']:
                    gefunden.append(student)

            #Wenn nur ein Student gefunden wurde, diesen einzeln zurückliefern
            if(len(gefunden) == 1):
                return {'menge': 'eins', 'ergebnis': gefunden[1]}

            #Wenn mehrere gefunden -> Liste zurückliefern
            elif(len(gefunden) > 1):
                return {'menge' : 'mehrere', 'ergebnis': gefunden}

            #Wenn keiner gefunden -> Info zurückliefern
            else:
                return {'menge': 'keine', 'ergebnis': 'Kein Student mit diesem Namen gefunden'}
                    
        except:
            #Information zurückliefern, dass Eingabe ungültig ist
            return {'menge': 'keine', 'ergebnis': 'Eingabe ist weder ein gültiger Name, noch eine gültige ID. Student konnte nicht gefunden werden.'}


def einzelner_student(id):
    '''
    Diese Funktion dient als suchwerkzeug für andere Funktionen, die anhand einer ID einen einzelnen Studenten finden müssen. Wenn kein oder mehrere Studenten gefunden werden wird ein Fehler ausgelöst.
    '''

    #Studenten-ID wird gesucht
    if suche_studenten(id)['menge'] == "eins":
        return suche_studenten(id)['ergebnis']
    elif suche_studenten(id)['menge'] == "keine":
        raise RuntimeError("Es wurde kein Student mit dieser ID gefunden.")
    elif suche_studenten(id)['menge'] == "mehrere":
        raise RuntimeError("Es wurden mehrere Studenten mit dieser ID gefunden.")


def student_hinzufuegen(name, projekt_punkte, klausur_punkte):
    '''
    Funktion die einen neuen Studenten hinzufügt, falls ID nicht vergeben wurde und Punkte die Regeln erfüllen.
    '''
    #Studierende aufsteigend nach ID sortieren
    studierende.sort(key = lambda x: x['id'])

    #Überprüfung ob eingegebene Werte erlaubt sind
    try:
        #ID für den neuen Studenten generieren, die 1 größer als die größte existierende ist
        id = studierende[-1].get('id') + 1

        if id_vorhanden(str(id)):
            raise ValueError(f"Automatisch generierte ID {id} ist bereits vorhanden")

        #Eingegebener Name gültig?
        pruefe_name(name)

        #Eingegebene Punktzahlen gültig? -> Wenn ja zu INT konvertieren
        if projekt_punkte != '':
            pruefe_punktzahl(projekt_punkte)
            projekt_punkte = int(projekt_punkte)

        if klausur_punkte != '':
            pruefe_punktzahl(klausur_punkte)
            klausur_punkte = int(klausur_punkte)

        #Studenten erzeugen und leere Werte entfernen
        student = {'id': int(id), 'name': name, 'projekt': projekt_punkte, 'klausur': klausur_punkte}

        if student['projekt'] == '':
            del student['projekt'] 
        if student['klausur'] == '':
            del student['klausur'] 

        #Falls alle Eingaben korrekt sind, wird ein neuer Student hinzugefügt
        studierende.append(student)

        
    #Fehler ausgeben, falls aufgetreten
    except ValueError as fehler:
        raise ValueError (f"Fehler beim Hinzufügen des Studenten: {fehler}")


def bearbeite_name(id, name):
    '''
    Funktion die einen Namen zur gegebenen ID überarbeitet
    '''
    #Studenten finden
    student = einzelner_student(id)

    #Name gültig? -> ändern falls ja
    try:
        pruefe_name(name)
        student['name'] = name

    #Fehler ausgeben falls nicht
    except ValueError as fehler:
        raise ValueError(f'Fehler beim Ändern des Namens: {fehler}')


def bearbeite_punkte(id, punkte, typ):
    '''
    Funktion die die Punktzahl für Klausur oder Projekt eines Studenten ändert
    '''

    #Suche Studenten
    student = einzelner_student(id)
    

    #Ändere Punktzahl falls Punktzahl valide
    try:
        pruefe_punktzahl(punkte)

        if typ == 'projekt':
            student['projekt'] = int(punkte)
        elif typ == 'klausur':
            student['klausur'] = int(punkte)
        else:
            raise ValueError('Ungültiger Typ der Punkte. Es wird nur projekt und klausur akzeptiert.')

    #Fehler ausgeben, falls aufgetreten
    except ValueError as fehler:
        raise ValueError(f'Fehler beim Ändern der Punktzahl: {fehler}')


def bearbeite_id():
    '''
    Funktion die die ID eines Studenten ändert - WIRD NICHT BENUTZT, IDs SIND FEST
    '''

    #Suche nach der ID
    id = input('Gib die ID des Studenten ein, die du bearbeiten möchtest: ')
    student = suche_studenten(id)
    if student is not None:
        print(f'Die Daten zu dieser ID lauten: {student}\n')
    else:
        return

    #Wahl einer neuen ID
    neue_id = input('Gib die neue ID ein: ')
    if (neue_id.isdigit() == False) or (int(neue_id) < 101):
        print('Fehler: Studenten-ID muss eine natürliche Zahl größer 100 sein.')
    else:
        if id_vorhanden(neue_id) == True:
            print('Fehler: Die Studenten-ID ist bereits vergeben.')
        else:
            student['id'] = neue_id


def berechne_note(id):
    '''
    Funktion welche die gesamte Punktzahl und die Note eines Studenten berechnet
    '''
    try:
        id = str(id)    

        #Studenten-ID wird gesucht
        student = einzelner_student(id)

        #Variablen für die Ausgabe initiieren
        endnote = 0.0
        gesamt_punkte = 0.0

        #Gibt es Punktzahlen für Klausur und Projekt?
        if student.get('projekt') != None and student.get('klausur') != None:
            projekt_punkte = student['projekt']
            klausur_punkte = student['klausur']
            gesamt_punkte = projekt_punkte + klausur_punkte

            #Bedingung fürs Bestehen wird überprüft
            if (klausur_punkte < 25) or (gesamt_punkte < 50):
                endnote = 5.0
                return {'endnote': endnote,'gesamtpunkte': gesamt_punkte}

            #Passende Note aus der Notentabelle suchen und Ergebnis zurückliefern
            else:
                for noten in notentabelle:
                    if gesamt_punkte in noten['gesamtpunkte']:
                        endnote = noten['note']
                        return {'endnote': endnote,'gesamtpunkte': gesamt_punkte}
                    
        #Fehlermeldung, falls Noten fehlen
        else:
            raise KeyError ('Dem Studenten fehlen Noten im Projekt und/oder der Klausur.')

    #Fehler zurückmelden, falls aufgetreten
    except Exception as fehler:
        raise RuntimeError(f'Fehler beim Berechnen der Note: {fehler}')


def generiere_einzelbericht (id):
    '''
    Diese Funktion generiert ein Dictionary, das einen Bericht für einen einzelnen Studenten abbildet. Es enthält Namen, Projektnote, Klausurnote, Gesamtpunktzahl, Gesamtnote und Bestehensstatus des Studenten.
    '''
    try:
    #Eingabe prüfen
        id = str(id)

        #Studentendaten suchen
        student = einzelner_student(id)

        #Noten des Studenten auswerten
        noten = berechne_note(id)

        #Hat der Student bestanden?
        if(noten['endnote'] < 5.0):
            bestanden = 'Ja'
        else:
            bestanden = 'Nein'

    
        #Bericht erstellen und zurückgeben
        bericht = {'name': student['name'], 'projekt': student['projekt'], 'klausur': student['klausur'], 'gesamtpunkte': noten['gesamtpunkte'], 'endnote': noten['endnote'], 'bestanden': bestanden}
        return bericht

    #Falls ein fehler auftritt, Fehlermeldung ausgeben
    except RuntimeError as fehler:
        raise RuntimeError(f'Fehler beim Generieren des Einzelberichts: {fehler}')


def berechne_kursdurchschnitt():
    '''
    Funktion welche den Kursdurchschnitt berechnet
    '''
    kurs_note = 0.0
    anzahl_berücksichtigt = 0
    anzahl_übersprungen = 0

    #Berechnung der Noten für jeden Student aus der Liste, der in beiden Einträgen Punkte hat
    for student in studierende:
        try:
            ergebnis = berechne_note(str(student['id']))
            kurs_note += ergebnis['endnote']
            anzahl_berücksichtigt += 1
        except:
            anzahl_übersprungen += 1
            continue

    if anzahl_berücksichtigt > 0:
        kurs_durchschnitt = round(kurs_note / anzahl_berücksichtigt, 1)
        informationen = {'durchschnitt': kurs_durchschnitt, 'gesamt': anzahl_übersprungen + anzahl_berücksichtigt, 'übersprungen': anzahl_übersprungen}
        return informationen   
    else:
        raise RuntimeError(f'Fehler beim Berechnen des Durchschnitts: Es konnten keine gültiegen Noten berechnet werden. Es wurden {anzahl_übersprungen} Studierende ausgewertet')


def berechne_notenverteilung():
    '''
    Funktion die die Notenverteilung berechnet, speichert und als Text ausgibt
    '''

    notenverteilung = {}
    for note in notentabelle:
        note['anzahl_studenten'] = 0

    #Berechnung der Noten, falls alle Punkte vorhanden sind
    for student in studierende:
        try:
            note_student = berechne_note(str(student['id']))
        except:
            continue

        #Erghöhung der Anzahl der Studenten mit einer bestimmten Note
        for note in notentabelle:
            if note_student['gesamtpunkte'] in note['gesamtpunkte']:
                note['anzahl_studenten'] += 1
            else:
                continue

    for note in notentabelle:
        notenverteilung[note['note']] = note['anzahl_studenten']
    return notenverteilung


def berechne_bestehensquote():
    '''
    Funktion die die Bestehensquote berechnet
    '''

    anzahl_bestanden = 0
    anzahl_nicht_bestanden = 0

    for student in studierende:
    #Überprüfung der Punktzahlen sowie Veränderung der Counter
        try:
            ergebnis = berechne_note(str(student['id']))
            if ergebnis['endnote'] != 5.0:
                anzahl_bestanden += 1
            else:
                anzahl_nicht_bestanden += 1
        except:
            continue

    if anzahl_bestanden + anzahl_nicht_bestanden == 0:
        raise ZeroDivisionError('Es konnten keine Studenten berücksichtigt werden.')

    bestehensquote = (anzahl_bestanden / (anzahl_bestanden + anzahl_nicht_bestanden)) * 100
    return round(bestehensquote, 2)


def finde_besten_studenten():
    '''
    Funktion, die den oder die besten Studenten anhand der Punkt findet
    '''

    max_punkte = -1
    beste_studenten = []

    for student in studierende:
        #Überprüfung ob der Student in beiden Kategorien Punkte hat
        try:
            projekt_punkte = student['projekt']
            klausur_punkte = student['klausur']
        except KeyError:
            continue

        gesamtpunkte = klausur_punkte + projekt_punkte

        if gesamtpunkte > max_punkte:
            max_punkte = gesamtpunkte
            #Komplette Liste wird aktualisiert, falls Student am meisten Punkte hat
            beste_studenten = [student]
        #Liste wird ergänzt, falls mehrere Studenten die gleiche Anzahl an Punkten haben
        elif gesamtpunkte == max_punkte:
            beste_studenten.append(student)

    if len(beste_studenten) > 0:
        return {'max_punkte': max_punkte, 'beste_studenten': beste_studenten}
    else:
        return {}


def finde_schlechtesten_studenten():
    '''
    Funktion die, die Studenten mit den wenigsten Punkten zurückliefert
    '''

    min_punkte = 101
    schlechteste_studenten = []

    for student in studierende:
        #Überprüfung ob der Student in beiden Kategorien Punkte hat
        try:
            projekt_punkte = student['projekt']
            klausur_punkte = student['klausur']
        except KeyError:
            continue

        gesamtpunkte = projekt_punkte + klausur_punkte

        if gesamtpunkte < min_punkte:
            min_punkte = gesamtpunkte
            #Komplette Liste wird aktualisiert, falls Student am meisten Punkte hat
            schlechteste_studenten = [student]
        #Liste wird ergänzt, falls mehrere Studenten die gleiche Anzahl an Punkten haben
        elif gesamtpunkte == min_punkte:
            schlechteste_studenten.append(student)

    if len(schlechteste_studenten) > 0:
        return {'min_punkte': min_punkte, 'schlechteste_studenten': schlechteste_studenten}
    else:
        return {}


def bestätigung ():
    '''
    Diese Funktion wird während des Programmablaufs genutzt, um eine Bestätigung des Users einzuholen
    '''

    entscheidung = input('Sind Sie sich sicher (j/n)? >')
    if (entscheidung == 'j'):
        return True
    elif (entscheidung == 'n'):
        return False

    #Falls eingabe ungültig, nochmal fragen
    elif (entscheidung not in ['j','n']):
        return(bestätigung())


#Programmablauf

#Begrüßungsnachricht
print(f'''Willkommen bei der Kurs- und Prüfungsverwaltung des Kurses ADGF2 der NIEB Hochschule.
Bitte wählen Sie die gewünschte Funktion aus:
''')

#Übergeordnete Schleife, bildet das Hauptmenü ab
while True:

    print(f'''
{85 * "-"}

"1" - Studierende suchen
"2" - Studierende hinzufügen
"3" - Kursanalyse anzeigen
"4" - Notenverteilung anzeigen

"exit" - Programm beenden

    ''')

    #Abfrage der gewünschten Funktion
    eingabe = input(">")

    
    if eingabe == "1":
        #So lange suchen, bis ein eindeutiger Student gefunden wurde oder der User die Suche abbricht
        gefunden = False
        while not gefunden:

            #Suchbegriff abfragen
            suche = input('Name oder ID ("exit" zum abbrechen) >')

            #Abbrechen, wenn der User "exit" eingibt
            if(suche.lower() == 'exit'):
                break

            #Suche einleiten    
            else:
                suchergebnis = suche_studenten(suche)

                #Wenn kein Student gefunden wurde, User benachrichtigen und in einen neuen Suchdurchlauf wechseln
                if(suchergebnis['menge'] == 'keine'):
                    print (suchergebnis['ergebnis'])

                #Wenn genau ein Student gefunden wurde, diesen speichern und Ausgeben und Suche beenden
                elif(suchergebnis['menge'] == 'eins'):
                    student = suchergebnis['ergebnis']
                    print (f'Student gefunden: {suchergebnis['ergebnis']}')
                    gefunden = True

                #Wenn mehrere Studenten gefunden werden, diese Ausgeben und um Angabe der passenden ID beten
                else:
                    print (f'Mehrere Studenten gefunden:') 
                    print(suchergebnis['ergebnis'])
                    print('Bitte geben Sie die ID des gesuchten Studenten an:')

        #Wenn ein eindeutiger Student gefunden wurde, neues Menü mit Aktionen zum Studenten öffnen
        while gefunden:
            print(f'''
Was möchten Sie tun?

{85 * '-'}

"1" - Bericht von {student["name"]} anzeigen 
"2" - Student bearbeiten
"3" - Student löschen
"exit" - Zurückkehren

            ''')

            eingabe = input('>')


            if eingabe == '1':
                #Bericht generieren und ausgeben
                bericht = generiere_einzelbericht(student['id'])
                print(f'''
Name: {bericht['name']}
Projektnote: {bericht['projekt']}
Klausurnote: {bericht['klausur']}
Gesamtpunktzahl: {bericht['gesamtpunkte']}
Gesamtnote: {bericht['endnote']}
Bestanden: {bericht['bestanden']}

                ''')


            elif eingabe == '2':
                #Neues Menü zur Bearbeitung öffnen

                while True:
                    print(f'''
Was möchten Sie bearbeiten?

{85 * '-'}

"1" - Name: {student.get('name')}
"2" - Projektnote: {student.get('projekt')}
"3" - Klausurnote: {student.get('klausur')}
"exit" - Bearbeiten beenden
                    ''')

                    eingabe = input('>')

                    if eingabe == '1':
                        #Namen abfragen und Änderung bestätigen lassen
                        eingabe = input('Neuer Name >')
                        if (bestätigung()):
                            #Änderung versuchen, Fehler ausgeben falls nicht erfolgreich
                            try:
                                bearbeite_name(student['id'])
                            except ValueError as fehler:
                                print(f'{fehler} Bitte Änderung erneut versuchen.')
                        
                    elif eingabe =='2':
                        #Punktzahl abfragen und Änderung bestätigen lassen
                        punktzahl = input('Neue Punktzahl >')
                        if (bestätigung()):
                            #Änderung versuchen, Fehler ausgeben falls nicht erfolgreich
                            try:
                                bearbeite_punkte(student['id'], punktzahl, 'projekt')
                            except ValueError as fehler:
                                print(f'{fehler} Bitte Änderung erneut versuchen.')

                    elif eingabe =='3':
                        #Punktzahl abfragen und Änderung bestätigen lassen
                        punktzahl = input('Neue Punktzahl >')
                        if (bestätigung()):
                            #Änderung versuchen, Fehler ausgeben falls nicht erfolgreich
                            try:
                                bearbeite_punkte(student['id'], punktzahl, 'projekt')
                            except ValueError as fehler:
                                print(f'{fehler} Bitte Änderung erneut versuchen.')

                    elif eingabe.lower() == 'exit':
                        #Menü verlassen
                        break

                    else:
                        print('Ungültige Einabe. Erlaubte Eingaben sind:')

            elif eingabe == '3':
                #Bestätigung einholen, Student entfernen und Bestätigungsnachricht ausgeben
                if(bestätigung()):
                    student_entfernt = studierende.pop(student)
                    print(f'Student {student_entfernt} erfolgreich entfernt')

            elif eingabe == 'exit':
                #Menü verlassen
                gefunden = False

            else:
                    print('Ungültige Einabe. Erlaubte Eingaben sind:')
                

    elif eingabe == '2':
        #Menü zum Hinzufügen von Studenten öffnen
        while True:
            #Attribute abfragen 
            name = input('Name des Studenten >')
            projektnote = input('Punktzahl Projekt (falls nicht bekannt "enter" drücken) >')
            klausurnote = input('Punktzahl Klausur (falls nicht bekannt "enter" drücken) >')

            try:
                #Student hinzufügen und Bestätigungsnachricht ausgeben
                student_hinzufuegen(name, projektnote, klausurnote)
                print(f"Student {studierende[-1]} erfolgreich hinzugefügt")

            #Fehler ausgeben, falls er auftritt
            except ValueError as fehler:
                print(f'{fehler} Bitte erneut versuchen.')

            #Abfragen, ob ein weiterer Student hinzugefügt werden soll
            weiter = input('Einen weiteren Studenten hinzufügen (j/n) >')

            #Falls nicht, Menü verlassen
            if weiter != 'j':
                break

            

    elif eingabe == '3':
        #Kursanalyse einleiten
        try:
            kursdurchschnitt = berechne_kursdurchschnitt()
            print(f'Kursdurchschnitt: {kursdurchschnitt}\n')
        
            bestehensquote = berechne_bestehensquote()
            print(f'Die Bestehensquote liegt bei {bestehensquote}%\n')
        
            #Beste Studenten ausgeben
            beste_studenten = finde_besten_studenten()
            if beste_studenten:
                print(f"Die höchste Punktzahl beträgt {beste_studenten['max_punkte']} Punkte.")
                print('Erreicht von:')
                for student in beste_studenten['beste_studenten']:
                    print(f"• {student['name']} | ID: {student['id']}")
                print()
            else:
                print('Keine Studenten mit vollständigen Punktzahlen vorhanden.')
                print()
        
            #Schlechteste Studenten ausgeben
            schlechteste_studenten = finde_schlechtesten_studenten()
            if schlechteste_studenten:
                print(f"Die niedrigste Punktzahl beträgt {schlechteste_studenten['min_punkte']} Punkte.")
                print('Erreicht von:')
                for student in schlechteste_studenten['schlechteste_studenten']:
                   print(f"• {student['name']} | ID: {student['id']}")
                print()
            else:
                print('Keine Studenten mit vollständigen Punktzahlen vorhanden.')
        
        except (ValueError, ZeroDivisionError) as fehler:
                print(f'Fehler bei der Kursanalyse: {fehler}\n')



    elif eingabe == '4':
        #Notenverteilung anzeigen
        try:
            notenverteilung = berechne_notenverteilung()
            print('Notenverteilung:')
            for note, anzahl in notenverteilung.items():
                print(f'• Note {note}: {anzahl} Studenten')
        
        except (ValueError, KeyError, TypeError) as fehler:
            print(f'Fehler bei der Berechnung der Notenverteilung: {fehler}\n')


    
    elif eingabe.lower() == "exit":
        #Programm beenden
        print('Vielen Dank, das Programm wird nun beendet')
        break

    else:
        print('Ungültige Einabe. Erlaubte Eingaben sind:')

    