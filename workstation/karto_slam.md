# **Karto SLAM mit ROS-Bag-Daten**

Diese Anleitung beschreibt, wie Sie eine ROS-Bag-Datei abspielen, den
Karto SLAM konfigurieren und starten. Zudem wird erklärt, welche
Ergebnisse beobachtet werden sollen.

## **Inhaltsverzeichnis**

1. [Voraussetzungen](#voraussetzungen)
2. [Installation und Einrichtung](#installation-und-einrichtung)
3. [Abspielen der ROS-Bag-Datei](#abspielen-der-ros-bag-datei)
4. [Starten von Hector SLAM](#starten-von-hector-slam)

## **Voraussetzungen**

- **ROS**: Eine vollständige ROS1-Installation (z. B. ROS Noetic oder Melodic).
- **Hector SLAM**: Vorinstalliertes Hector SLAM-Paket.
- **ROS-Bag-Datei**: Eine Datei mit aufgezeichneten Sensordaten (z. B. `scan`-Topics).

## **Installation und Einrichtung**

**Hector SLAM installieren**

Falls Karto SLAM noch nicht installiert ist, führen Sie folgende
Schritte aus:
```
mkdir -p \~/catkin_ws/src
cd \~/catkin_ws/src
catkin_init_workspace
git clone https://github.com/ros-perception/slam_karto.git
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
rosbag play <rosbag-file>.bag --clock
```
**Hinweis:** Die Option \--clock simuliert die Zeit der
aufgezeichneten Daten, was für SLAM-Prozesse wichtig ist.

## **Starten von Hector SLAM**

Starten Sie **ROS Core**:
```
roscore
```
Starten Sie den Karto SLAM-Knoten mit der Launch-Datei:
```
roslaunch slam_karto karto_slam.launch
```
**Hinweis**: Prüfen Sie in der Launch-Datei, ob die TF-Frames für Map, Odometrie, LaserScan usw korrekt definiert sind. Fehlerhafte oder fehlende Frames können zu Problemen bei der Kartierung und Lokalisierung führen.

**RViz** soll in einem anderen Terminal geöffnet werden.
```
rviz
```
