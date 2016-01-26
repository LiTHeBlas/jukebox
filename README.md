# Blåsrummet
Alla tjänster körs i Docker-containrar. Det ser till att de är helt isolerade 
från varandra och att du tvingas definiera väldigt tydliga starttillstånd för 
varje tjänst. Rekommenderad läsning: http://12factor.net

# Att starta Docker-containrarna med rätt inställningar
Jag letar efter en bra lösning på detta. Än så länge startar jag dem från min 
dator med hjälp av Docker Compose. //Olle

# Installation av Docker-host
Den fysiska maskinen kör HypriotOS som är en variant av Raspbian. Uppdaterad 
guide för installation finns på 
http://blog.hypriot.com/getting-started-with-docker-on-your-arm-device/. Efter 
detta är det väldigt viktigt att du följer nedanstående steg:

Uppdatera en massa jox.

    rpi-update
    apt-get update && apt-get dist-upgrade

Lägg till ett personligt konto, t.ex.

    adduser olle
    adduser olle sudo

Nu är ett bra tillfälle att logga ut och logga in med ditt egna konto istället.

Inaktivera `root`-lösenordet och se till att kontot förbjuds via SSH. Det finns 
massor av fördelar med att göra detta och cirka inga nackdelar. Passa också på 
att inaktivera `pi`-kontot som har `sudo` (jättedåligt eftersom det också har ett 
standardlösenord).

    sudo passwd -l pi
    sudo passwd -l root
    sudo sed -i 's/PermitRootLogin yes/PermitRootLogin no/' /etc/ssh/sshd_config

Konfigurera nätverksinställningarna.

    sudo sed -i 's/iface eth0 inet dhcp/iface eth0 inet static\naddress 130.236.246.146\nnetmask 255.255.255.0\ngateway 130.236.246.1/' /etc/network/interfaces
    sudo sed -i 's/nameserver 10.0.0.1/nameserver 130.236.246.1/' /etc/resolv.conf
