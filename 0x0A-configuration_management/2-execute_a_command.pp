# Description: Puppet manifest to kill a process named 'killmenow' using pkill.


exec { 'kill_killmenow_process':
  command  => '/usr/bin/pkill -f "killmenow"',
  provider => 'shell',
}
