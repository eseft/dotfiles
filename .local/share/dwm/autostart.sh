#!/usr/bin/env sh
dwmblocks &
# Polkit
lxpolkit &
# Daemon scripts from dwmblocks
$HOME/.local/src/dwmblocks/daemons/pulse_daemon.sh &
sleep 1 &&
sigdwmblocks 2; sigdwmblocks 4; sigdwmblocks 7 &
source $HOME/.bashrc &
/usr/bin/emacs --daemon &
/usr/bin/syndaemon -i 0.5 -K -R &
# CAPS_LOCK Acts as an Escape wile presing alone
# xcape -t 500 -e 'Control_L=Escape' &
# XRandR monitor settings
xrandr --output HDMI-A-0 --auto --output eDP --auto --right-of HDMI-A-0 &
picom --config /home/di/.config/picom/picom.conf &
nitrogen --restore &
pasystray &
