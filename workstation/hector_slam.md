# **Hector SLAM mit ROS-Bag-Daten**

Diese Anleitung beschreibt, wie Sie eine ROS-Bag-Datei abspielen, den
Hector SLAM konfigurieren und starten. Zudem wird erklärt, welche
Ergebnisse beobachtet werden sollen.

## **Inhaltsverzeichnis**

1. [Voraussetzungen](#voraussetzungen)
2. [Installation und Einrichtung](#installation-und-einrichtung)
3. [Abspielen der ROS-Bag-Datei](#abspielen-der-ros-bag-datei)
4. [Starten von Hector SLAM](#starten-von-hector-slam)
5. [Beobachtungen und Ergebnisse](#beobachtungen-und-ergebnisse)
6. [Fehlerbehebung](#fehlerbehebung)

## **Voraussetzungen**

- **ROS**: Eine vollständige ROS1-Installation (z. B. ROS Noetic oder Melodic).
- **Hector SLAM**: Vorinstalliertes Hector SLAM-Paket.
- **ROS-Bag-Datei**: Eine Datei mit aufgezeichneten Sensordaten (z. B. `scan`-Topics).

## **Installation und Einrichtung**

**Hector SLAM installieren**

Falls Hector SLAM noch nicht installiert ist, führen Sie folgende
Schritte aus:
```
mkdir -p \~/catkin_ws/src
cd \~/catkin_ws/src
catkin_init_workspace
git clone https://github.com/tu-darmstadt-ros-pkg/hector_slam.git
```

**Installieren Sie die Abhängigkeiten**
```
sudo apt update\
rosdep update\
rosdep install \--from-paths . \--ignore-src -r -y
```

**Kompilieren Sie den Workspace**
```
cd \~/catkin_ws\
catkin_make\
source devel/setup.bash
```

## **Abspielen der ROS-Bag-Datei**

Navigieren Sie zum Verzeichnis mit der ROS-Bag-Datei:
```
cd path/to/your/rosbag
```
Starten Sie die Wiedergabe der Datei:
```
rosbag play \<rosbag-file\>.bag \--clock
```
**Hinweis:** Die Option \--clock simuliert die Zeit der
aufgezeichneten Daten, was für SLAM-Prozesse wichtig ist.

## **Starten von Hector SLAM**

Starten Sie **ROS Core**:
```
roscore
```
Starten Sie den Hector SLAM-Knoten mit der Launch-Datei:
```
roslaunch hector_slam_launch tutorial.launch
```

**RViz** wird automatisch geöffnet. Prüfen Sie die folgenden Standard-Displays:

* **Map**: Zeigt die erstellte Karte in Echtzeit.
* **TF**: Visualisiert die Transformationshierarchie zwischen den Frames.
* **Path**: Zeigt die Trajektorie des Roboters.
* **Pose**: Zeigt die aktuelle Position des Roboters.

Manuelle Hinzufügung von Displays:
* **LaserScan**: Zeigt die LIDAR-Daten.

**Beobachtungen und Ergebnisse**

**Karte**
Hector SLAM sollte die Umgebungskarte in Echtzeit erstellen.

**TF-Frames**
Stellen Sie sicher, dass die TF-Frames wie map, odom, base_imu_link, und
laser_frame korrekt miteinander verbunden sind. Nutzen Sie dazu:
rosrun tf tf_echo \<source_frame\> \<target_frame\>

**Robot-Trajektorie (Path)**
Die Trajektorie des Roboters wird im RViz unter dem **Path**-Display
angezeigt. Sie sollte die Bewegung des Roboters konsistent und präzise
darstellen.

**Position des Roboters (Pose)**
Das **Pose**-Display zeigt die aktuelle Position und Orientierung
des Roboters. Diese Werte sollten mit der Trajektorie übereinstimmen.

