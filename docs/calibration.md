
# Kalibrierung des JetRacer AI Kits

Die Kalibrierung des JetRacer AI Kits umfasst folgende Komponenten: **Motoren**, **Servo**, **Kamera**, und **Lidar**.

## Motoren
1. Temporäre Kalibrierung:
   ```bash
   rosrun rqt_reconfigure rqt_reconfigure
   ```
2. Dauerhafte Konfiguration:
   Bearbeite die Datei `~/catkin_ws/src/jetracer_ros/cfg/jetracer.cfg`.

## Servo
1. Temporäre Kalibrierung:
   ```bash
   roslaunch jetracer calibrate_linear.launch
   ```
2. Dauerhafte Konfiguration:
   Aktualisiere die Datei `~/catkin_ws/src/jetracer_ros/cfg/jetracer.cfg`.

## Kamera
- Starten des Kamera-Nodes:
  ```bash
  roslaunch jetracer csi_camera.launch
  ```
- Visualisierung auf der Workstation:
  ```bash
  rosrun rqt_image_view rqt_image_view
  ```
- TODO: Kalibrierung der Kamera.

## Lidar
- Starten des Lidar-Nodes:
  ```bash
  roslaunch jetracer lidar.launch
  ```
- Überprüfung der Daten:
  ```bash
  rostopic echo /scan
  ```
