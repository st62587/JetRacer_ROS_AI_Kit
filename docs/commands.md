
# Wichtige ROS-Befehle für JetRacer

Hier findest du eine Übersicht über die wichtigsten ROS-Befehle für die Arbeit mit dem JetRacer AI Kit.

## Basis-Befehle
- `roscore`: Startet den ROS Master, um die Kommunikation sicherzustellen.
- `rosrun jetracer jetracer.launch`: Startet alle relevanten ROS-Nodes.
- `rostopic list`: Listet alle verfügbaren ROS-Topics auf.
- `rostopic echo /<topic>`: Zeigt die Daten eines spezifischen Topics in Echtzeit an.
- `rosbag record -a`: Nimmt alle Topics auf.
- `rosbag play <dateiname>`: Spielt aufgezeichnete Topics ab.

## Steuerung
- `roslaunch jetracer keyboard.launch`: Steuerung mit der Tastatur.
- `roslaunch jetracer joy.launch`: Steuerung mit einem Gamepad oder Joystick.

## Debugging und Visualisierung
- `rosrun rqt_publisher rqt_publisher`: Manuelles Senden von Nachrichten an Topics.
- `rosrun rqt_plot rqt_plot`: Visualisierung von Datenströmen.
- `rosrun rqt_reconfigure rqt_reconfigure`: Temporäre Anpassungen der Konfiguration.

## Weiterführende Befehle
- `rosmsg show <msg_type>`: Zeigt den Inhalt eines Nachrichtenformats.
- `rostopic type <topic>`: Zeigt den Nachrichtentyp eines Topics.
