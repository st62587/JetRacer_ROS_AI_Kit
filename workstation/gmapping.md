# **Karto SLAM mit ROS-Bag-Daten**

Diese Anleitung beschreibt, wie Sie eine ROS-Bag-Datei abspielen, den
Gmapping konfigurieren und starten. 

## **Inhaltsverzeichnis**

1. [Voraussetzungen](#voraussetzungen)
2. [Installation und Einrichtung](#installation-und-einrichtung)
3. [Abspielen der ROS-Bag-Datei](#abspielen-der-ros-bag-datei)
4. [Starten von Gmapping](#starten-von-gmapping)

## **Voraussetzungen**

- **ROS**: Eine vollständige ROS1-Installation (z. B. ROS Noetic oder Melodic).
- **Gmapping**: Vorinstalliertes Gmapping-Paket.
- **ROS-Bag-Datei**: Eine Datei mit aufgezeichneten Sensordaten (z. B. `scan`-Topics).

## **Installation und Einrichtung**

**Gmapping installieren**

Falls Gmapping noch nicht installiert ist, führen Sie folgende
Schritte aus:
```
mkdir -p \~/catkin_ws/src
cd \~/catkin_ws/src
catkin_init_workspace
git clone https://github.com/ros-perception/slam_gmapping.git
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
Starten Sie den Gmapping-Knoten mit der Launch-Datei:
```
roslaunch gmapping slam_gmapping_pr2.launch
```
**Hinweis**: Prüfen Sie in der Launch-Datei, ob die TF-Frames für Map, Odometrie, LaserScan usw korrekt definiert sind. Fehlerhafte oder fehlende Frames können zu Problemen bei der Kartierung und Lokalisierung führen.
Die Launch-Datei soll so aussehen:
```
<?xml version="1.0"?>
<launch>
  <node pkg="gmapping" type="slam_gmapping" name="slam_gmapping" output="screen" respawn="true" >
    <remap from="scan" to="scan"/>
    <param name="base_frame" value="base_footprint"/>
    <param name="odom_frame" value="odom"/>
    <param name="map_update_interval" value="2.0"/>
    <param name="maxUrange" value="8.0"/>
    <param name="maxRange" value="12.0"/>
    <param name="sigma" value="0.05"/>
    <param name="kernelSize" value="1"/>
    <param name="lstep" value="0.05"/>
    <param name="astep" value="0.05"/>
    <param name="iterations" value="5"/>
    <param name="lsigma" value="0.075"/>
    <param name="ogain" value="3.0"/>
    <param name="lskip" value="0"/>
    <param name="minimumScore" value="100"/>
    <param name="srr" value="0.01"/>
    <param name="srt" value="0.02"/>
    <param name="str" value="0.01"/>
    <param name="stt" value="0.02"/>
    <param name="linearUpdate" value="0.05"/>
    <param name="angularUpdate" value="0.0436"/>
    <param name="temporalUpdate" value="-1.0"/>
    <param name="resampleThreshold" value="0.5"/>
    <param name="particles" value="8"/>
    <param name="xmin" value="-50.0"/>
    <param name="ymin" value="-50.0"/>
    <param name="xmax" value="50.0"/>
    <param name="ymax" value="50.0"/>
    <param name="delta" value="0.05"/>
    <param name="llsamplerange" value="0.01"/>
    <param name="llsamplestep" value="0.01"/>
    <param name="lasamplerange" value="0.005"/>
    <param name="lasamplestep" value="0.005"/>
  </node>
</launch>
```
**RViz** soll in einem anderen Terminal geöffnet werden.
```
rviz
```
