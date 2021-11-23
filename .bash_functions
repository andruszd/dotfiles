up()
{
    dir=""
    if [ -z "$1" ]; then
        dir=..
    elif [[ $1 =~ ^[0-9]+$ ]]; then
        x=0
        while [ $x -lt ${1:-1} ]; do
            dir=${dir}../
            x=$(($x+1))
        done
    else
        dir=${PWD%/$1/*}/$1
    fi
    cd "$dir";
}

chmoddr()
{
  # CHMOD _D_irectory _R_ecursivly

  if [ -d "$1" ]; then
    echo "error: please use the mode first, then the directory";
    return 1;
  elif [ -d "$2" ]; then
    find $2 -type d -print0 | xargs -0 chmod $1;
  fi
}

assimilate()
{
  _assimilate_opts="";

  if [ "$#" -lt 1 ]; then   echo "not enough arguments";    return 1;  fi
  SSHSOCKET=~/.ssh/assimilate_socket.$1;
  echo "resistance is futile! $1 will be assimilated";
  if [ "$2" != "" ]; then
    _assimilate_opts=" -p$2 ";
  fi

  ssh -M -f -N $_assimilate_opts -o ControlPath=$SSHSOCKET $1;
  if [ ! -S $SSHSOCKET ]; then echo "connection to $1 failed! (no socket)"; return 1; fi

  ### begin assimilation

  # copy files
  scp -o ControlPath=$SSHSOCKET ~/.bashrc $1:~;
  scp -o ControlPath=$SSHSOCKET -r ~/.config/htop $1:~;

  # import ssh key
  if [[ -z $(ssh-add -L|ssh -o ControlPath=$SSHSOCKET $1 "grep -f - ~/.ssh/authorized_keys") ]]; then
    ssh -o ControlPath=$SSHSOCKET $1 "mkdir ~/.ssh > /dev/null 2>&1";
    ssh-add -L > /dev/null&&ssh-add -L|ssh -o ControlPath=$SSHSOCKET $1 "cat >> ~/.ssh/authorized_keys"
  fi
  ssh -o ControlPath=$SSHSOCKET $1 "chmod -R 700 ~/.ssh";

  ### END
  ssh -S $SSHSOCKET -O exit $1 2>1 >/dev/null;
}
