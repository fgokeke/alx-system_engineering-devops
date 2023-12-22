#Description: Puppet manifest to install Flask version 2.1.0 using pip3.

exec { 'upgrade_werkzeug':
  command => '/usr/bin/pip3 install --upgrade Werkzeug==2.1.1',
  path    => ['/usr/bin'],
}


package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Exec['upgrade_werkzeug'],
}
