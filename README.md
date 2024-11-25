
# JetRacer ROS AI Platform

Dieses Repository dient als Entwicklungsplattform für das **JetRacer ROS AI Kit**. Ziel ist es, die Funktionalität des Kits zu erweitern und eine Basis für zukünftige Projekte zu schaffen. Es beinhaltet Code, Dokumentation und Tutorials für den Aufbau, die Konfiguration und die Steuerung des JetRacer.

## 📋 Projektübersicht

Das Projekt umfasst folgende Bereiche:
- **Auto**: Aufbau und Konfiguration des JetRacer mit ROS.
- **Workstation**: Entwicklung von Tools und Schnittstellen zur Steuerung und Datenvisualisierung.
- **Datenverarbeitung**: Aufzeichnung und Analyse von Sensordaten sowie Integration von KI-Modellen.

## 📂 Repository-Struktur

Struktur verlatet muss angepasst werden

```plaintext
JetRacer_ROS_AI_Platform/
├── README.md                # Übersicht und Projektbeschreibung
├── docs/                    # Dokumentation und Tutorials
│   ├── tutorial_links.md    # Links zu offiziellen Tutorials
│   ├── installation.md      # Installationsanleitungen
│   └── architecture.md      # Softwarearchitektur
├── auto/                    # Code und Dokumentation für das Auto
│   ├── src/                 # ROS-Nodes und Skripte
│   ├── sensors/             # Sensorintegration und Kalibrierung
│   ├── control/             # Steuerung und Bewegungsalgorithmen
│   └── README.md            # Details zum Autoteil des Projekts
├── workstation/             # Tools und Schnittstellen für die Workstation
│   ├── src/                 # ROS-Nodes und Datenvisualisierung
│   ├── connection/          # Verbindung zwischen Auto und Workstation
│   └── README.md            # Beschreibung und Anleitungen
└── LICENSE                  # Lizenzinformationen
```

## 🔗 Tutorials und Ressourcen

Die folgenden Tutorials bilden die Grundlage für das Projekt:
- [Assembly Manual](https://www.waveshare.com/wiki/JetRacer_ROS_AI_Kit_Tutorial_I:_Assembly_Manual)
- [Install Jetson Nano Image](https://www.waveshare.com/wiki/JetRacer_ROS_AI_Kit_Tutorial_II:_Install_Jetson_Nano_Image)
- [Weitere Tutorials...](https://www.waveshare.com/)

## 🚀 Erste Schritte

### Voraussetzungen
- JetRacer ROS AI Kit
- Jetson Nano Developer Kit
- ROS Melodic oder neuer
- Ubuntu 18.04 (Nvidia-Version mit JetPack 4.x)

### Installation
1. Clone dieses Repository:
   ```bash
   git clone https://github.com/<dein-username>/JetRacer_ROS_AI_Platform.git
   cd JetRacer_ROS_AI_Platform
   ```
2. Folge den Anleitungen in `docs/installation.md`, um das Projekt einzurichten.

### Beispiel: Auto starten
1. ROS-Nodes im Verzeichnis `auto/src` ausführen:
   ```bash
   roslaunch jetracer jetracer.launch
   ```
2. Sensoren überprüfen und Daten visualisieren.

## 🤝 Beitrag leisten

Beiträge sind willkommen! Bitte folge diesen Schritten:
1. Forke das Repository.
2. Erstelle einen neuen Branch:
   ```bash
   git checkout -b feature/neue-funktion
   ```
3. Sende einen Pull-Request.

## 🛡️ Lizenz

Dieses Projekt steht unter der [MIT-Lizenz](LICENSE).

---

Vielen Dank an alle Mitwirkenden für ihre Unterstützung bei diesem Projekt!
