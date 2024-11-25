# Problem mit Launch-Dateien im ROS 2 Jetracer-Projekt

In diesem Projekt wurde versucht, die Launch-Dateien von ROS 1 auf ROS 2 zu portieren. Der Übergang von ROS 1 zu ROS 2 erfordert einige wesentliche Änderungen, da ROS 2 ein Python-basiertes Launch-System verwendet, anstelle der XML-Dateien von ROS 1.

## Status der Launch-Dateien

- **Kamera Launch-Datei (`csi_camera.launch.py`)**
  - Die Launch-Datei für die Kamera konnte erfolgreich auf ROS 2 portiert werden. Die Kamera wird gestartet und streamt das Bild erfolgreich.

- **Andere Launch-Dateien (z.B. `jetracer.launch.py`)**
  - Andere Launch-Dateien wie `jetracer.launch.py` bereiten derzeit noch Probleme. Ein spezifisches Problem ist, dass das entsprechende ausführbare Programm ('jetracer') im Installationsverzeichnis nicht gefunden wird. Dies deutet darauf hin, dass die Installation des Skripts nicht korrekt erfolgt ist oder dass die Pfadangaben in der Launch-Datei nicht stimmen.

## Portierungsprozess der `csi_camera.launch` von ROS 1 auf ROS 2

Der Port der Launch-Datei `csi_camera.launch` von ROS 1 auf ROS 2 beinhaltete mehrere Schritte, da sich die Struktur und Syntax zwischen den beiden Versionen erheblich unterscheiden. Nachfolgend wird der Prozess beschrieben:

1. **Konvertierung von XML zu Python**
   - In ROS 1 wurden Launch-Dateien im XML-Format geschrieben. In ROS 2 wird hingegen ein Python-basiertes Launch-System verwendet. Die ursprüngliche `csi_camera.launch`-Datei wurde daher von XML in Python umgeschrieben, um die neuen Anforderungen von ROS 2 zu erfüllen.

2. **Verwendung von `LaunchDescription` und `Node`**
   - ROS 2 verwendet die Klasse `LaunchDescription` zur Definition der Launch-Konfiguration und die Klasse `Node` zur Definition der zu startenden Nodes.
   - Jeder Node wird in der Python-Datei als Instanz der Klasse `Node` definiert, wobei Parameter, Remappings und andere Eigenschaften angegeben werden können.

3. **Anpassung von Parametern und Remappings**
   - Die Parameter und Remappings, die zuvor in der XML-Datei definiert waren, wurden in der Python-Launch-Datei mit Hilfe von Dictionaries und Listen definiert. Beispielsweise wurden Kameraparameter wie `sensor_id`, `width`, `height`, und `fps` direkt in der Python-Datei als Parameter an den Node übergeben.

4. **Neuer Aufbau des Projekts/Workspaces**
   - Nach der Anpassung der Launch-Dateien musste der ROS 2-Workspace neu aufgebaut werden, um sicherzustellen, dass alle Änderungen berücksichtigt wurden.
   - Der Befehl zum Neuaufbau war:
     ```bash
     colcon build --packages-select jetracer
     ```
   - Nach dem Build-Prozess wurde die Umgebung neu geladen, um sicherzustellen, dass alle Pakete korrekt eingebunden sind:
     ```bash
     source install/setup.bash
     ```

5. **Test und Validierung**
   - Nach der Anpassung wurde die Launch-Datei mehrfach getestet, um sicherzustellen, dass die Kamera erfolgreich startet und das Bild streamt. Fehler wie fehlende Parameter oder falsche Pfade wurden iterativ behoben.
   - Eine wichtige Maßnahme zur Fehlerbehebung war das Auslesen der Log-Dateien, die sich im Verzeichnis `.ros/log/` befinden. Diese Logs lieferten wertvolle Informationen über fehlgeschlagene Starts und halfen dabei, spezifische Fehler zu identifizieren.

6. **Verwendung des `gscam` Nodes**
   - Der `gscam` Node wurde verwendet, um die Kamerastreams zu verarbeiten. Dabei mussten spezifische Anpassungen für die GStreamer-Konfiguration vorgenommen werden, damit die Kamera ordnungsgemäß funktioniert.

7. **Fehlerbehebung durch Log-Analyse**
   - Die Analyse der Log-Dateien nach jedem Build oder Startversuch war entscheidend, um Fehler zu finden und zu beheben.
   - Die Logs wurden mit folgenden Befehlen angezeigt:
     ```bash
     cat ~/.ros/log/latest_build/*.log
     ```
   - Typische Fehler waren fehlende ausführbare Dateien, fehlende Parameter oder nicht korrekt gesetzte Pfade.

## Nächste Schritte

- **Individuelle Anpassung aller Launch-Dateien**
  - Jede Launch-Datei muss individuell an die neue ROS 2-Struktur angepasst werden.
  - Python-Skripte müssen korrekt als ausführbare Dateien installiert und in den entsprechenden Verzeichnissen abgelegt werden.

- **Fehlerbehebung der Node-Installation**
  - Überprüfen, ob alle Skripte korrekt im Installationsverzeichnis (`~/ros2_ws/install/<package_name>/lib/<package_name>/`) abgelegt und als ausführbare Dateien markiert wurden.
  - Anpassen der Launch-Dateien, um sicherzustellen, dass die korrekten Pfade und Pakete angegeben sind.

- **Test und Validierung**
  - Nach jeder Anpassung der Launch-Dateien sollte eine Testausführung erfolgen, um sicherzustellen, dass die entsprechenden Nodes korrekt gestartet werden können und keine Fehlermeldungen auftreten.

## Fazit

Der erfolgreiche Port der Kamera-Launch-Datei ist ein wichtiger erster Schritt, aber die anderen Launch-Dateien müssen noch individuell angepasst werden, um mit der neuen ROS 2-Umgebung kompatibel zu sein. Der Fokus liegt nun auf der Behebung von Installations- und Ausführungsproblemen der einzelnen Nodes, damit die gesamte Funktionalität des Jetracer-Projekts wiederhergestellt werden kann.

