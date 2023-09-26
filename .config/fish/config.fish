if status is-interactive
    # Commands to run in interactive sessions can go here

    ###############################
    ###         VI MODE         ###
    ###############################
    fish_vi_key_bindings

    ###############################
    ###  ENVIRONMENT VARIABLES  ###
    ###############################

    ###############################
    ###         ALIASES         ###
    ###############################
    alias ls='eza -al --git --icons -s type'
    alias pcmupg='sudo pacman -Syu'
    alias pcmins='sudo pacman -S'
    alias pcmsrc='pacman -Ss'
    alias malina='ssh raspberry'
    alias sedit='EDITOR=nvim sudoedit'

    ###############################
    ###        FOR ESP32        ###
    ###############################
    # source $HOME/docs/projects/esp32/esp-idf/export.fish
    # clear
    
    ###############################
    ###    ACTIVATE STARSHIP    ###
    ###############################
    starship init fish | source
end
