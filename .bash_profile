#
# ~/.bash_profile
#

[[ -f ~/.bashrc ]] && . ~/.bashrc

###############################
### ENVIRONMENTAL VARIABLES ###
###############################

export XDG_CONFIG_HOME="$HOME/.config"
export XDG_DATA_HOME="$HOME/.local/share"
export XDG_CACHE_HOME="$HOME/.cache"
export XDG_STATE_HOME="$HOME/.local/state"
export XDG_RUNTIME_DIR="/run/user/$UID"
export PATH="${PATH}:${HOME}/.local/bin"
export PATH="${PATH}:${HOME}/.emacs.d/bin"
export WORKON_HOME="${HOME}/.local/share/virtualenvs"
export EDITOR="emacsclient -c -a"
