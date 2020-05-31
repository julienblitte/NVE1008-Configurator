# NVE1008-Configurator
Advanced interface for old NiceVision NVE1008

# Purpose
Let you change advanced parameter with NiceVision NVE1008 devices such as 75 Ohms logical terminator.
This has been tested on firmware version **2.0.0.31** and **2.0.0.40**.

# Installation
1. Connect via SSH to your NVE1008 encoder to tansfer files using a tool such as [WinSCP](https://winscp.net/eng/download.php)
2. Transfer following files
- `/opt/www/config.html`
- `/opt/www/cgi-bin/get.cgi`
- `/opt/www/cgi-bin/info.cgi`
- `/opt/www/cgi-bin/set.cgi`
3. Using WinSCP special command or a SSH command line tool such as [Putty](https://www.chiark.greenend.org.uk/~sgtatham/putty/) to your NVE1008 and change file mods
- `chmod 644 /opt/www/config.html`
- `chmod 755 /opt/www/cgi-bin/*`

# Usage
Once installed, you can change advanced settings on the web interface accessing this url:
http://192.168.0.8/config.html

After configuration change, restart the unit and test results using VLC, for example for channel 1, stream 1:
rtsp://192.168.0.8/video101

# Related tools
* Qognify (formerly NiceVision) [Edge Devices Configuration Tool](https://theq.qognify.com)
* [UniversalScanner](https://github.com/julienblitte/UniversalScanner/releases)
* [VLC](https://www.videolan.org/vlc/)