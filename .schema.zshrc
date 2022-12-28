# If you come from bash you might have to change your $PATH.
#
# https://github.com/Powerlevel9k/powerlevel9k/wiki/Show-Off-Your-Config
# exec $SHELL
#
ZSH_THEME="powerlevel9k/powerlevel9k"

POWERLEVEL9K_SHORTEN_DIR_LENGTH=2
POWERLEVEL9K_MODE='awesome-patched'
POWERLEVEL9K_PROMPT_ON_NEWLINE=true

POWERLEVEL9K_VCS_GIT_HOOKS=(vcs-detect-changes)

POWERLEVEL9K_VCS_GIT_ICON=''
POWERLEVEL9K_VCS_STAGED_ICON='\u00b1'
POWERLEVEL9K_VCS_UNTRACKED_ICON='\u25CF'
POWERLEVEL9K_VCS_UNSTAGED_ICON='\u00b1'
POWERLEVEL9K_VCS_INCOMING_CHANGES_ICON='\u2193'
POWERLEVEL9K_VCS_OUTGOING_CHANGES_ICON='\u2191'

POWERLEVEL9K_HOME_ICON=''
POWERLEVEL9K_HOME_SUB_ICON=''
POWERLEVEL9K_FOLDER_ICON=''
POWERLEVEL9K_ETC_ICON=''

POWERLEVEL9K_RAM_BACKGROUND="black"
POWERLEVEL9K_RAM_FOREGROUND=249
POWERLEVEL9K_RAM_ELEMENTS=(ram_free)

POWERLEVEL9K_MULTILINE_FIRST_PROMPT_PREFIX="\n"
POWERLEVEL9K_MULTILINE_LAST_PROMPT_PREFIX="$ "

POWERLEVEL9K_LEFT_PROMPT_ELEMENTS=(dir)
POWERLEVEL9K_RIGHT_PROMPT_ELEMENTS=(virtualenv vcs battery ssh ram load time)

POWERLEVEL9K_DIR_HOME_FOREGROUND=011
POWERLEVEL9K_DIR_HOME_SUBFOLDER_FOREGROUND=010

POWERLEVEL9K_SHORTEN_STRATEGY="truncate_middle"
POWERLEVEL9K_SHORTEN_DIR_LENGTH=4

POWERLEVEL9K_STATUS_VERBOSE=false
export DEFAULT_USER="$USER"

export ZSH="/Users/qw/.oh-my-zsh"
source $ZSH/oh-my-zsh.sh

# source ~/.bashrc

export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8

alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'
alias ll="ls -lht"




export PS1=$'\e[01;32m %n@%m \e[01;35m %d \e[01;34m %t \n \e[01;31m $> \e[01;00m'
