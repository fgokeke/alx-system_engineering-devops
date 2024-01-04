#!/usr/bin/env bash
# File: 5-nginx_config.pp

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Configure Nginx to listen on port 80
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  replace => true,
  content => "# Nginx default configuration
server {
    listen 80 default_server;

    location / {
        root /var/www/html;
        index index.html;
    }

    location /redirect_me {
        return 301 http://example.com/new_page;
    }
}
",
  notify  => Service['nginx'],
}

# Create Hello World HTML page
file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
}

# Ensure symbolic link to enable the new configuration
file { '/etc/nginx/sites-enabled/default':
  ensure => link,
  target => '/etc/nginx/sites-available/default',
}

# Restart Nginx to apply the changes
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}

