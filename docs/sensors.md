
# Integration der Sensoren und Aktuatoren

Dieses Dokument beschreibt die Integration der Sensoren und Aktuatoren für das JetRacer AI Kit.

## Kamera
- Start des Kamera-Nodes:
  ```bash
  roslaunch jetracer csi_camera.launch
  ```
- Anpassung der Auflösung:
  Bearbeite die Datei `catkin_ws/src/jetbot_pro/launch/csi_camera.launch`.

## Lidar
- Start des Lidar-Nodes:
  ```bash
  roslaunch jetracer lidar.launch
  ```
- Visualisierung und Filterung:
  ```bash
  roslaunch jetracer laser_filter.launch
  ```

## Motoren und Servo
- Steuerung und Kalibrierung:
  ```bash
  rosrun rqt_reconfigure rqt_reconfigure
  ```
- Dauerhafte Einstellungen in:
  `~/catkin_ws/src/jetracer_ros/cfg/jetracer.cfg`
