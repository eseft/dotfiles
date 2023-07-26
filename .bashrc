#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

###############################
###         ALIASES         ###
###############################

# alias ls='ls --color=auto'
alias ls='exa -al --git --icons -s type'
alias pcmupg='sudo pacman -Syu && sigdwmblocks 7'
alias pcmins='sudo pacman -S'
alias pcmsrc='pacman -Ss'

alias malina='ssh raspberry'


##############################
###    BASH COMPLITIONS    ###
##############################

[ -r /usr/share/bash-completion/bash_completion   ] && . /usr/share/bash-completion/bash_completion

##############################
###         PROMPT         ###
##############################

set -o vi

PS1='[\u@\h \W]\$ '
eval "$(starship init bash)"
