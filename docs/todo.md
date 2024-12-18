# TODO-Liste

## Aufgabenübersicht

- [ ] **Aufgabe 1: Optimiertes Image für Jetracer erstellen**
  - **Hauptverantwortlich:** Colin Kastens
  - **Zuarbeit:** Bitte ergänzen
  - **Beschreibung:** Erstellen eines Images für den Jetracer, optimiert auf unsere Bedürfnisse.

- [ ] **Aufgabe 2: Script für individuelle anpassbare Szenarien**
  - **Hauptverantwortlich:** Colin Kastens
  - **Zuarbeit:** Tue Cung
  - **Beschreibung:** Erstellung eines Scripts, mit dem individuelle Launch-Dateien für die Entwicklung und Wiederholbarkeit von Szenarien mit minimalem Konfigurationsaufwand generiert werden können. Es soll sowohl auf dem Jetracer als auch auf einer Workstation funktionieren.

- [ ] **Aufgabe 3: Erstellen neuer ROSBAGs**
  - **Hauptverantwortlich:** Colin Kastens
  - **Zuarbeit:** Bitte ergänzen
  - **Beschreibung:** Erstellung neuer ROSBAGs nach Vorgabe bzw. Anforderungen

- [ ] **Aufgabe 4: Fortsetzung der Evaluation der SLAM-Ansätze
- **Hauptverantwortlich:** Vanelle Happi
- **Beschreibung:** Fortsetzung der Evaluation der SLAM-Ansätze mit einer neu aufgenommenen ROS-Bag-Datei. Dabei soll eine festgelegte Strecke abgefahren werden, um zu überprüfen, ob eine korrekte Karte erstellt wird.

- [ ] **Aufgabe 5: Untersuchung der Ursachen für Verzögerungen bei der Rosbag1-Aufnahme**
- **Hauptverantwortlich:** Christian Temfac
- **Beschreibung:** Während des letzten Integrationstests des Autos und der Workstation mit der Bridge wurde eine Rosbag-Aufnahme mit ROS Noetic über die Bridge gestartet. Dies führte zu einer Steuerungsverzögerung des Autos. Es soll untersucht werden, um die Ursachen der Verzögerung festzustellen.

- [ ] **Aufgabe 6: Untersuchung der Übermittlung von Befehlen an den Motor bei der Implementierung der Szenarien**
- **Hauptverantworlich:**
- **Beschreibung:** Recherche über den Nachrichtentyp, der in den entsprechenden Szenarien an das Auto bzw. die Motoren geschickt wird. Dabei sollen das Nachrichtenformat und das Verhalten der Motoren beim Empfang der Nachricht untersucht werden. 

---

## Details zu den Aufgaben

### Aufgabe 1: Optimiertes Image für Jetracer erstellen
- **Hauptverantwortlich:** Colin Kastens
- **Zuarbeit:** Bitte ergänzen
- **Beschreibung:** Erstellung eines Images für den Jetracer, optimiert auf unsere Bedürfnisse.
- **Teilaufgaben:**
  - [x] OS installieren
  - [x] Netzwerk konfigurieren
  - [x] Jetracer einrichten
  - [ ] (DOING) Jetracer kalibrieren
  - [ ] Abhängigkeiten installieren/konfigurieren
  - [ ] Script-Integration (siehe Aufgabe 2)
  - [ ] Testen
    - [ ] Testziele definieren
  - [ ] Image erstellen

---

### Aufgabe 2: Script für individuelle anpassbare Szenarien
- **Hauptverantwortlich:** Colin Kastens
- **Zuarbeit:** Tue Cung
- **Beschreibung:** Erstellung eines Scripts, mit dem individuelle Launch-Dateien für die Entwicklung und Wiederholbarkeit von Szenarien erstellt werden können. Das Script soll sowohl auf dem Jetracer als auch auf einer Workstation funktionieren.
- **Teilaufgaben:**
  - [ ] Alle möglichen Topics/Nodes identifizieren
  - [ ] Zusammenfassen zu sinnvollen Gruppen
  - [ ] Script erstellen, das neue Launch-Dateien erzeugen kann, optimiert auf mögliche Szenarien
  - [ ] Testen

---

### Aufgabe 3: Erstellen neuer ROSBAGs
- **Hauptverantwortlich:** Colin Kastens
- **Zuarbeit:** Bitte ergänzen
- **Beschreibung:** Erstellung neuer ROSBAGs nach Vorgabe bzw. Anforderungen
- **Teilaufgaben:**
  - [ ] Abholen der Strecke
  - [ ] Aufbauen der Strecke
  - [ ] Aufnahme ROSBAG
  - [ ] ROSBAG Hochladen

---

### Aufgabe 4: Fortsetzung der Evaluation der SLAM-Ansätze
- **Hauptverantwortlich:** Vanelle Happi
- **Teilaufgaben:**
  - [ ] Festgelegte Strecke abgefahren
  - [ ] Überprüfung der korrekten Kartenerstellung

---

### Aufgabe 5: Untersuchung der Ursachen für Verzögerungen bei der Rosbag1-Aufnahme
- **Hauptverantwortlich:** Christian Temfac
- **Teilaufgaben:**
  - [ ] Recherche und Annahme über die möglichen Verzögerungsursachen
  - [ ] Neue Integrationstests durchführen
  - [ ] Überprüfung der Annahmen
  - [ ] Fazit ziehen

---

### Aufgabe 6: Untersuchung der Übermittlung von Befehlen an den Motor bei der Implementierung der Szenarien
- **Hauptverantwortlich:** Christian Temfac
- **Zuarbeit:** Bitte ergänzen
- **Teilaufgaben:**
  - [x] Szenarien definieren
  - [ ] Nachrichtentyp und Topic für Motoren festlegen
  - [ ] Virtuelle Simulation der Nachrichtenübertragung
  - [ ] Virtuelle Simulation des Motorverhaltens beim Empfang der Nachricht
  - [ ] Integration der Ergebnisse mit der KI 