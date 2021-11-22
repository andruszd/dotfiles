alias ae='$EDITOR ~/.bashrc ; source ~/.bashrc'
alias lt='ls --human-readable --size -1 -S --classify'
alias mnt="mount | awk -F' ' '{ printf \"%s\t%s\n\",\$1,\$3; }' | column -t | egrep ^/dev/ | sort"
alias mount='mount |column -t'
alias ls='ls -F --color=auto'
alias sl='ls -F --color=auto'
alias ll='ls -lh'
alias l.='ls -d .* --color=auto'
alias gh='history|grep'
alias left='ls -t -1'
alias count='find . -type f | wc -l'
alias cpv='rsync -ah --info=progress2'
#progress bar on file copy. Useful evenlocal.
alias cpProgress="rsync --progress -ravz"
alias startgit='cd `git rev-parse --show-toplevel` && git checkout master && git pull'
alias cg=`git rev-parse --show-toplevel`
alias c='clear'
## Colorize the grep command output for ease of use (good for log files)##
alias grep='grep --color=auto'
alias egrep='egrep --color=auto'
alias fgrep='fgrep --color=auto'
alias nocomment='grep -Ev "^(#|$)"'
## get rid of command not found ##
alias cd..='cd ..'
## a quick way to get out of current directory ##
alias ..='cd ..'
alias ...='cd ../../../'
alias ....='cd ../../../../'
alias .....='cd ../../../../'
alias .4='cd ../../../../'
alias .5='cd ../../../../..'
alias bc='bc -l'
alias sha1='openssl sha1'
alias mkdir='mkdir -pv'
# install  colordiff package :)
alias diff='colordiff'
alias h='history'
alias j='jobs -l'
alias path='echo -e ${PATH//:/\\n}'
alias now='date +"%T"'
alias nowtime=now
alias nowdate='date +"%d-%m-%Y"'
# Vim
alias vi=vim
alias svi='sudo vi'
alias vis='vim "+set si"'
alias edit='vim'
alias lvim='vim -c "normal" '
# Networking
# Stop after sending count ECHO_REQUEST packets
alias ping='ping -c 5'
# Do not wait interval 1 second, go fast
alias fastping='ping -c 100 -s.2'
alias ports='netstat -tulanp'
## All of our servers eth1 is connected to the Internets via vlan / router etc
alias dnstop='dnstop -l 5  eth1'
alias vnstat='vnstat -i eth1'
alias iftop='iftop -i eth1'
alias tcpdump='tcpdump -i eth1'
# work on wlan0 by default #
# Only useful for laptop as all servers are without wireless interface
alias iwconfig='iwconfig wlan0'
# Firewall
## shortcut for iptables and pass it via sudo#
alias ipt='sudo /sbin/iptables'
# display all rules #
alias iptlist='sudo /sbin/iptables -L -n -v --line-numbers'
alias iptlistin='sudo /sbin/iptables -L INPUT -n -v --line-numbers'
alias iptlistout='sudo /sbin/iptables -L OUTPUT -n -v --line-numbers'
alias iptlistfw='sudo /sbin/iptables -L FORWARD -n -v --line-numbers'
alias firewall=iptlist
# get web server headers #
alias header='curl -I'
# find out if remote server supports gzip / mod_deflate or not #
alias headerc='curl -I --compress'
# do not delete / or prompt if deleting more than 3 files at a time #
alias rm='rm -I --preserve-root'
# confirmation #
alias mv='mv -i'
alias cp='cp -i'
alias ln='ln -i'
# Parenting changing perms on / #
alias chown='chown --preserve-root'
alias chmod='chmod --preserve-root'
alias chgrp='chgrp --preserve-root'
# distro specific  - Debian / Ubuntu and friends #
# install with apt-get
alias updatey="sudo apt-get --yes"
alias apt-get="sudo apt-get -o Acquire::http::Dl-Limit=15"
# update on one command
alias update='sudo apt-get update && sudo apt-get upgrade'
## distrp specifc RHEL/CentOS ##
alias update='yum update'
alias updatey='yum -y update'
alias syi='sudo yum install'
alias sys='sudo yum search'
# become root #
alias root='sudo -i'
alias su='sudo -i'
# reboot / halt / poweroff
alias reboot='sudo /sbin/reboot'
alias poweroff='sudo /sbin/poweroff'
alias halt='sudo /sbin/halt'
alias shutdown='sudo /sbin/shutdown'
# also pass it via sudo so whoever is admin can reload it without calling you #
alias nginxreload='sudo /usr/local/nginx/sbin/nginx -s reload'
alias nginxtest='sudo /usr/local/nginx/sbin/nginx -t'
alias lightyload='sudo /etc/init.d/lighttpd reload'
alias lightytest='sudo /usr/sbin/lighttpd -f /etc/lighttpd/lighttpd.conf -t'
alias httpdreload='sudo /usr/sbin/apachectl -k graceful'
alias httpdtest='sudo /usr/sbin/apachectl -t && /usr/sbin/apachectl -t -D DUMP_VHOSTS'
## pass options to free ##
alias meminfo='free -m -l -t'
## get top process eating memory
alias psmem='ps auxf | sort -nr -k 4'
alias psmem10='ps auxf | sort -nr -k 4 | head -10'
## get top process eating cpu ##
alias pscpu='ps auxf | sort -nr -k 3'
alias pscpu10='ps auxf | sort -nr -k 3 | head -10'
## Get server cpu info ##
alias cpuinfo='lscpu'
## older system use /proc/cpuinfo ##
##alias cpuinfo='less /proc/cpuinfo' ##
## get GPU ram on desktop / laptop##
alias gpumeminfo='grep -i --color memory /var/log/Xorg.0.log'
## this one saved by butt so many times ##
alias wget='wget -c'
## this one saved by butt so many times ##
alias ff4='/opt/firefox4/firefox'
alias ff13='/opt/firefox13/firefox'
alias chrome='/opt/google/chrome/chrome'
alias opera='/opt/opera/opera'
#default ff
alias ff=ff13
#my default browser
alias browser=chrome
## set some other defaults ##
alias df='df -H'
alias du='du -ch'
# top is atop, just like vi is vim
alias top='atop'
## nfsrestart  - must be root  ##
## refresh nfs mount / cache etc for Apache ##
alias nfsrestart='sync && sleep 2 && /etc/init.d/httpd stop && umount netapp2:/exports/http && sleep 2 && mount -o rw,sync,rsize=32768,wsize=32768,intr,hard,proto=tcp,fsc natapp2:/exports /http/var/www/html &&  /etc/init.d/httpd start'
## Memcached server status  ##
alias mcdstats='/usr/bin/memcached-tool 10.10.27.11:11211 stats'
alias mcdshow='/usr/bin/memcached-tool 10.10.27.11:11211 display'
## quickly flush out memcached server ##
alias flushmcd='echo "flush_all" | nc 10.10.27.11 11211'
## Remove assets quickly from Akamai / Amazon cdn ##
alias cdndel='/home/scripts/admin/cdn/purge_cdn_cache --profile akamai'
alias amzcdndel='/home/scripts/admin/cdn/purge_cdn_cache --profile amazon'
## supply list of urls via file or stdin
alias cdnmdel='/home/scripts/admin/cdn/purge_cdn_cache --profile akamai --stdin'
alias amzcdnmdel='/home/scripts/admin/cdn/purge_cdn_cache --profile amazon --stdin'
#Grabs the disk usage in the current directory
alias usage='du -ch | grep total'
#Gets the total disk usage on your machine
alias totalusage='df -hl --total | grep total'
#Shows the individual partition usages without the temporary memory values
alias partusage='df -hlT --exclude-type=tmpfs --exclude-type=devtmpfs'
#Gives you what is using the most space. Both directories and files. Varies on
#current directory
alias most='du -hsx * | sort -rh | head -10'
alias ducks='du -ck | sort -nr | head'
alias psg='ps -Helf | grep -v $$ | grep -i -e WCHAN -e'
alias ps2='ps -ef | grep -v $$ | grep -i '
# file tree
alias tree="find . -print | sed -e 's;[^/]*/;|____;g;s;____|; |;g'"
#quick file tree
alias filetree="find . -print | sed -e 's;[^/]*/;|____;g;s;____|; |;g'"
#turn screen off
alias screenoff="xset dpms force off"
# list folders by size in current directory
alias usage="du -h --max-depth=1 | sort -rh"
alias tgrep='rgrep --binary-files=without-match'
alias serve='python -m SimpleHTTPServer'
alias trace='mtr --report-wide --curses $1'
alias killtcp='sudo ngrep -qK 1 $1 -d wlan0'
alias usage='ifconfig wlan0 | grep 'bytes''
alias connections='sudo lsof -n -P -i +c 15'
alias up1="cd .."
# edit multiple files split horizontally or vertically
alias   e="vim -o "
alias   E="vim -O "
# only file without an extension
alias noext='dsd | egrep -v ".|/"'
# directory-size-date (remove the echo/blank line if you desire)
alias dsd="echo;ls -Fla"
alias   dsdm="ls -FlAh | more"
# show directories only
alias   dsdd="ls -FlA | grep :*/"
# show executables only
alias   dsdx="ls -FlA | grep *"
# show non-executables
alias   dsdnx="ls -FlA | grep -v *"
# order by date
alias   dsdt="ls -FlAtr"
# dsd plus sum of file sizes
#alias   dsdz="ls -Fla $1 $2 $3 $4 $5|awk '{print; x=x+$5} END {print "total bytes = ",x}'"
# only file without an extension
alias noext='dsd | egrep -v ".|/"'
alias machine="echo you are logged in to ... `uname -a | cut -f2 -d' '`"
alias info='clear;machine;pwd'
