# Jetson Nano ROS2 Setup: Upgrade von Ubuntu 20.04 auf 22.04

Dieses Projekt basiert auf dem NVIDIA Jetson Nano Image. Das ursprüngliche Image kann [hier](https://github.com/Qengineering/Jetson-Nano-Ubuntu-20-image) gefunden werden. Aufgrund von Performance-Problemen, die durch den geringen Speicher von 4 GB verursacht wurden, wurde die Desktop-Umgebung entfernt, um die Systemressourcen effizienter nutzen zu können.

Das ursprüngliche Image wurde gemäß der [Anleitung](https://github.com/xronos-inc/jetson-nano-ubuntu-22.04) von Ubuntu 20.04 auf Ubuntu 22.04 aktualisiert. Nach dem Upgrade wurde überprüft, dass das JetPack weiterhin korrekt installiert ist und funktioniert.

### Befehle zum Aktualisieren des Systems und Entfernen der Desktop-Umgebung

1. **Partition erweitern, um zusätzlichen Speicherplatz zu nutzen**
   Da das ursprüngliche Image für eine 32 GB SD-Karte ausgelegt war, aber auf einer 64 GB SD-Karte installiert wurde, führte dies während des Upgrades zu Speicherproblemen. Der Speicherplatz wurde schnell knapp und der erste Upgrade-Versuch schlug fehl, da nicht genügend Speicherplatz zur Verfügung stand. Die Erweiterung der Partition löste dieses Problem. Die folgenden Schritte wurden durchgeführt, um die Partition zu erweitern:
   - Zuerst die aktuelle Speicherplatznutzung anzeigen lassen:
     ```bash
     df -h
     ```
   - Die Partitionstabelle neu einlesen und die Partition erweitern:
     ```bash
     sudo parted /dev/mmcblk0
     ```
     Geben Sie innerhalb des `parted`-Werkzeugs folgende Befehle ein:
     ```
     resizepart 1 100%
     quit
     ```
   - Das Dateisystem auf die gesamte Partition erweitern:
     ```bash
     sudo resize2fs /dev/mmcblk0p1
     ```

2. **Systemupdate auf Ubuntu 22.04 durchführen**
   ```bash
   sudo apt update && sudo apt upgrade -y
   sudo do-release-upgrade
   ```

3. **Desktop-Umgebung entfernen, um Systemressourcen zu sparen**
   ```bash
   sudo apt purge ubuntu-desktop -y && sudo apt autoremove -y && sudo apt autoclean
   sudo apt-get remove nautilus nautilus-* gnome-power-manager gnome-screensaver gnome-termina* gnome-pane*
   sudo apt-get remove gnome-applet* gnome-bluetooth gnome-desktop* gnome-sessio* gnome-user* gnome-shell-common
   sudo apt-get remove zeitgeist-core libzeitgeist* gnome-control-center gnome-screenshot && sudo apt-get autoremove
   sudo apt-get remove --purge libreoffice*
   sudo apt-get remove libreoffice-core
   sudo apt-get remove snapd lightdm cups chromium*
   sudo apt clean
   ```

4. **Überprüfen der JetPack-Installation**
   ```bash
   dpkg -l | grep -i nvidia
   ```

5. **NVIDIA l4t apt Quellen wiederherstellen**
   ```bash
   sudo mv /etc/apt/sources.list.d/nvidia-l4t-apt-sources.list.distUpgrade /etc/apt/sources.list.d/nvidia-l4t-apt-sources.list
   ```

6. **SSSD Boot-Fehler beheben (optional)**
   Dieser Schritt ist nicht zwingend erforderlich, behebt jedoch einen Boot-Fehler im Zusammenhang mit SSSD.
   ```bash
   sudo cp /usr/lib/aarch64-linux-gnu/sssd/conf/sssd.conf /etc/sssd/.
   sudo chmod 600 /etc/sssd/sssd.conf
   ```

7. **ROS2 Humble direkt installieren**
   - ROS2 Setup hinzufügen
     ```bash
     sudo apt update && sudo apt install curl -y
     sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
     sudo sh -c 'echo "deb http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" > /etc/apt/sources.list.d/ros2-latest.list'
     ```
   - ROS2 Humble installieren
     ```bash
     sudo apt update
     sudo apt install ros-humble-desktop -y
     ```

Im Anschluss daran wurde versucht, ROS2 über einen Docker-Container laufen zu lassen, was grundsätzlich funktionierte. Allerdings ergab sich ein Problem bei der Weiterleitung des Terminals bzw. der Weiterleitung von grafischen Anwendungen. Diese Weiterleitung war ohne einen speziellen NVIDIA-Treiber (nicht Teil von JetPack) nicht möglich.

Aus diesem Grund wurde entschieden, ROS2 Humble direkt auf dem System zu installieren. Die Installation von ROS2 Humble verlief problemlos und es konnte erfolgreich in Betrieb genommen werden.
