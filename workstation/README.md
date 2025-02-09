# **Workstation mit ROS-Bridge**
Hier wird die selbst eingerichtete Workstation beschrieben 
und alle darauf installierten Pakete und Befehle.

## **Inhaltsverzeichnis**

1. [Base Betriebssysteme](#base-betriebssysteme)
2. [Installation und Konfiguration des ROS-Systems und der Bridge](#installation-und-konfiguration-des-ros-systems-und-der-bridge)
3. [Weitere installierte Pakete](#weitere-installierte-pakete)
4. [Vorstellung des KI-Modells](#vorstellung-des-ki-modells)

## **Base Betriebssysteme**

Diese Maschine wurde mit Ubuntu 20.04 eingerichtet.

## **Installation und Konfiguration des ROS-Systems und der Bridge**

Die Installation der ROS-Bridge erfordert, dass sowohl ROS1 als auch ROS2 auf demselben Rechner installiert sind.
Demzufolge wurden die folgenden ROS1 und ROS2 Versionen installiert:

### **Installiertes ROS1**

Auf diesem System wurde **ROS1 Noetic** wie folgt installiert:
[ROS1 Noetic Installationsanleitung](https://wiki.ros.org/noetic/Installation/Ubuntu)
Nach der Installation wurde mit folgendem Befehl der Alias **sr1** im System erstellt:
```bash
echo "alias sr1='source /opt/ros/noetic/setup.bash'" >> ~/.bashrc
source ~/.bashrc
```
Um das System auf ROS Noetic zu verweisen, gibt man folgenden Befehl im Terminal ein:
```bash
sr1
```

### **Installiertes ROS2**

Auf dem System wurde **ROS2 Foxy** installiert, wie in dieser Installationsanleitung beschrieben:
[ROS2 Foxy Installationsanleitung](https://docs.ros.org/en/foxy/Installation/Ubuntu-Install-Debians.html)

Nach der Installation wurde wie vorher der Alias **sr2** erstellt:
```bash
echo "alias sr2='source /opt/ros/foxy/setup.bash'" >> ~/.bashrc
source ~/.bashrc
```
Um das System auf ROS2 zu verweisen, gibt man folgenden Befehl im Terminal ein:
```bash
sr2
```

### **ROS-Bridge Installation**
Nach der Installation der beiden ROS-Systeme wurde die **ros-foxy-ros1-bridge** installiert.

Um die Bridge auszuführen, soll zuerst:

- **gebaut** werden:
```bash
sr1
sr2 
colcon build --symlink-install --packages-select ros1_bridge --cmake-force-configure
```

- dann **ROS_MASTER_URI** und **ROS_IP** spezifiziert werden:
```bash
export ROS_MASTER_URI=http://{localhost/Master-IP}:11311
export ROS_IP=Rechner/container-IP
```

- schließlich kann die Bridge gestartet werden:
```bash
ros2 run ros1_bridge dynamic_bridge --bridge-all-topics
```

## **Weitere installierte Pakete**
### **ROSBAG-Converter**
Um eine Rosbag umzuwandeln, ist bereits das Python-Paket **rosbags** installiert.
- Umwandlung **Rosbag in ROS2 Bag**
Man braucht dann nur folgenden Befehl auszuführen:
```bash
rosbags-convert ros1_bag_file.bag --dst output_folder
```

- Umwandlung **ROS2 Bag in Rosbag**
Dafür soll folgender Befehl ausgeführt werden:
```bash
rosbags-convert path/to/ros2_bag_folder --dst output.bag
```

### **Paket zur Image-Extraktion von Rosbag**
Um die Rosbag-Daten wieder anzuwenden, wurde ein Paket installiert, um Bilder und Videos aus der Rosbag zu extrahieren.
Um Bilder aus der Rosbag zu extrahieren, wurde das Paket:

- Extraktion von **Rosbag (ROS1 Bag)**
```bash
rosrun image_view extract_images _sec_per_frame:=value image:=image_topic _image_transport:=compressed/theora
```

- Extraktion von **ROS2 Bag**
```bash
ros2 run image_view extract_images --ros-args -r image:=/csi_cam_0/image_raw --param image_transport:=compressed
```

### **Paket zur Video-Extraktion von Rosbag**

Zum Extrahieren von Videos aus der Rosbag wurde das Repository **rosbag2video** geklont.
Um die Extraktion auszuführen, sollen folgende Befehle eingegeben werden:
```bash
cd rosbag2video

# für eine ROS2 Bag: 
./ros2bag2video.py --fps 25 --rate 1.0 -t /camera_node/image_raw/compressed path/to/your/rosbag2_file.db3

# für eine Rosbag (ROS1 Bag)
./rosbag2video.py --fps 25 --rate 1.0 -t /camera_node/image_raw/compressed path/to/your/rosbag_file.bag
```

### **Jetracer Paket**
Um die Jetracer-Roboter zu steuern, soll das Jetracer-Paket mit den Launch-Files auf der Workstation installiert werden.
Dafür wurde die Workspace **catkin_ws** erstellt.
In dieser Workspace wurde unter **/src** das Jetracer-Repository geklont, gebaut und der Alias **catkin_ws** erstellt,
um diese Workspace unter *ROS1* zu verweisen. Dann kann mit folgendem Befehl die Jetracer-Topic wie */Joy* oder *camera_csi* gestartet werden:
In einem ersten Terminal:
```bash
sr1
export ROS_MASTER_URI=http://IP-Jetracer-Roboter:11311
roscore
```

In einem zweiten Terminal:
```bash
sr1
catkin_ws
roslaunch jetracer topic_launch_file_name.launch
```

## **Vorstellung der KI-Modell**

 
