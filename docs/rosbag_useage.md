
# Verwendung von ROSBag

Dieses Dokument beschreibt, wie ROSBag verwendet wird, um Topics aufzuzeichnen, abzuspielen und in RViz zu visualisieren.

---

## Aufnahme einer ROSBag-Datei
1. Stelle sicher, dass `roscore` läuft:
   ```bash
   roscore
   ```
2. Starte die relevanten ROS-Nodes, z. B.:
   ```bash
   roslaunch jetracer csi_camera.launch
   ```
3. Beginne mit der Aufzeichnung aller Topics:
   ```bash
   rosbag record -a
   ```
   - **`-a`**: Zeichnet alle verfügbaren Topics auf.
   - **Optional**: Nur bestimmte Topics aufzeichnen:
     ```bash
     rosbag record /camera/image_raw /scan
     ```
4. Beende die Aufzeichnung mit `Ctrl+C`. Die `.bag`-Datei wird im aktuellen Verzeichnis gespeichert.

---

## Abspielen einer ROSBag-Datei
1. Spiele die aufgezeichnete Datei ab:
   ```bash
   rosbag play recording1.bag
   ```
2. Zusätzliche Optionen:
   - `--loop`: Spielt die Datei in einer Endlosschleife ab.
   - `--clock`: Gibt die simulierte Zeit der Aufzeichnung aus:
     ```bash
     rosbag play --loop --clock recording1.bag
     ```

---

## Visualisierung in RViz
1. Starte RViz:
   ```bash
   rviz
   ```
2. Füge die gewünschten Topics hinzu:
   - **Kamera**:
     - Wähle `Image` aus der Liste der verfügbaren Plugins.
     - Setze das Topic auf `/camera/image_raw` oder ein anderes Kameratopic.
   - **Lidar**:
     - Wähle `LaserScan` aus der Liste der verfügbaren Plugins.
     - Setze das Topic auf `/scan`.

3. Synchronisiere RViz mit der simulierten Zeit aus der ROSBag-Datei:
   - Stelle sicher, dass `use_sim_time` aktiviert ist:
     ```bash
     rosparam set use_sim_time true
     ```
   - Aktiviere in RViz die Option `Use Sim Time`.

## Hinweise
- ROSBag-Dateien können groß werden. Achte darauf, nur relevante Topics aufzuzeichnen.
- Nutze `rosbag info <dateiname>` für eine Übersicht der enthaltenen Topics:
  ```bash
  rosbag info recording1.bag
  ```

