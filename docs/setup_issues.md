
# Probleme und Lösungen bei der ersten Inbetriebnahme des JetRacer AI Kits

Während der ersten Inbetriebnahme des JetRacer AI Kits traten einige Herausforderungen auf. Hier sind die häufigsten Probleme und deren Lösungen:

## 1. Bootloader-Probleme
Der Bootloader des Jetson Nano war beschädigt und musste neu geflasht werden. Dies erforderte den **NVIDIA SDK Manager**. Eine Herausforderung hierbei war, dass der SDK Manager ein **Ubuntu 18.04** Betriebssystem voraussetzt, welches **nicht in einer virtuellen Maschine** laufen darf.

### Lösung:
- Installation von Ubuntu 18.04 auf einem physischen Rechner.
- **Problem:** Secure Boot verhinderte die Installation auf einem neuen Laptop.
  - Netzwerkadapter-Treiber konnten aufgrund von Sicherheitsrichtlinien nicht installiert werden.
- **Lösung:** Wechsel zu einem älteren Laptop, bei dem Secure Boot keine Rolle spielte.

### Alternativlösung:
Die Einschränkung auf Ubuntu 18.04 kann umgangen werden, indem die Datei `/etc/os-release` so angepasst wird, dass sie den Werten von Ubuntu 18.04 entspricht. Dies ermöglicht die Verwendung des SDK Managers unter Ubuntu 20.04 oder 22.04. Siehe:  
👉 [GitHub: xronos-inc/jetson-nano-ubuntu-22.04](https://github.com/xronos-inc/jetson-nano-ubuntu-22.04)

---

## 2. Serielle Verbindung zum JetRacer
Für die Fehleranalyse empfiehlt es sich, einen **TTL-to-USB-Adapter** zu verwenden. Dies ermöglicht eine serielle Verbindung mit dem JetRacer, um Fehler auszulesen, selbst wenn keine Bildschirmausgabe erfolgt.

### Empfehlung:
- Beschaffung eines **TTL-to-USB-Adapters**.
- Verwendung eines seriellen Terminals wie `minicom` oder `screen`, um auf die serielle Ausgabe zuzugreifen.

---

## Fazit
Die Inbetriebnahme des JetRacer kann durch hardwarebedingte Einschränkungen erschwert werden. Mit den oben beschriebenen Lösungen lassen sich jedoch die meisten Probleme effektiv umgehen.

