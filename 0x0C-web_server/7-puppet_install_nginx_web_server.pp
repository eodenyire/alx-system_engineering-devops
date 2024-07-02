# Define a class for Nginx configuration
class nginx {

  # Include the standard nginx module
  include puppet::package::nginx

  # Ensure Nginx package is present
  package { 'nginx': ensure => installed }

  # Configure Nginx service
  service { 'nginx':
    ensure => running,
    enabled => true,
    require => Package['nginx'],
  }

  # Define root directory for the default server block
  $www_dir = '/var/www/html'

  # Create the www directory if it doesn't exist
  file { $www_dir:
    ensure => directory,
    owner => 'root',
    group => 'root',
    mode => '0755',
  }

  # Create a simple index.html file
  file { $www_dir + '/index.html':
    ensure => present,
    content => '<!DOCTYPE html><html><body>Hello World!</body></html>',
    owner => 'root',
    group => 'root',
    mode => '0644',
  }

  # Define server block for handling requests
  nginx::resource::server { 'default':
    port => 80,
    server_name => ['localhost'],
    www_root => $www_dir,
    location => {
      '/redirect_me' => {
        rewrite_rules => [
          '^ / permanent',
        ],
      },
    }
  }
}
