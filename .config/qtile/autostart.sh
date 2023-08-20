#!/usr/bin/env bash
lxpolkit &
/usr/bin/emacs --daemon &
picom --config $HOME/.config/picom/picom.conf &
nitrogen --restore &
nm-applet &
pasystray &
