========
powerall
========

**powerall** is a python-based project which leverages the Raspberry Pi 4 along with an INA260
precision digital current and power monitor to track the power generation capabilities of solar
and wind sources to determine power availability in a givent location over time.

Configuring a systemd service
=============================

Copy the *powerall.service* file to the /etc/systemd/system folder on your machine.  Execute the following
commands::

    systemctl enable powerall
    service start powerall

The powerall application will now run every time your machine boots up, and will restart if an error
causes it to stop.
