
# ubuntu
PS1='\[\033[01;32m\]$(whoami) $(hostname) \[\033[35m\]$(date "+%m%d.%H%M") \[\033[01;34m\]$(pwd) \n \[\033[01;31m\] %> \[\033[00m\]'
# mac
# export PS1=$'\e[01;32m %n@%m \e[01;35m %d \e[01;34m %t \n \e[01;31m $> \e[01;00m'
# enable color support of ls and also add handy aliases
if [ -x /usr/bin/dircolors ]; then
    test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
    alias ls='ls --color=auto'
    alias ll='ls -atlF --color=auto'
    alias dir='dir --color=auto'
    alias vdir='vdir --color=auto'
    alias grep='grep --color=auto'
    alias fgrep='fgrep --color=auto'
    alias egrep='egrep --color=auto'
fi


function b64() {
  base64 $1 |sed -e 's/^/data:image\/jpeg;base64,/g'  | pbcopy;
}


info() {
    echo "hostname: `cat /etc/hostname`  `hostname`"
    echo "ip: `hostname -I`"
    echo

    file=`realpath $1`
    echo "path: $file"
    echo

    if [ -f "$file" ]; then
        if [ -b "$file" ]; then
            echo "$file is a binary file."
        elif [ -d "$file" ]; then
            echo "$file is a directory."
        elif [ -L "$file" ]; then
            echo "$file is a symbolic link."
        else
            echo "$file is a regular file."
        fi
    else
        echo "$file does not exist."
    fi
    echo

    stat $file
    echo

    if file "$file" |grep -qE 'image|bitmap'; then
        echo "File has the headers of an image"
        identify $file
    fi
    echo
}
