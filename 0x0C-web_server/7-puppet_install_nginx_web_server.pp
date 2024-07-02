# Puppet manifest to install and configure Nginx with a 301 redirect

package { 'nginx':
  ensure => installed,
}

service { 'nginx':
  ensure => running,
  enable => true,
  require => Package['nginx'],
}

file { '/var/www/html/index.nginx-debian.html':
  ensure  => file,
  content => '<html><body><h1>Hello World!</h1></body></html>',
  require => Package['nginx'],
}

file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx/default.erb'),
  require => Package['nginx'],
}

service { 'nginx':
  ensure => running,
  subscribe => File['/etc/nginx/sites-available/default'],
}
