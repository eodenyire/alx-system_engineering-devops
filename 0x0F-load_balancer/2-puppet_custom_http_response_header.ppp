# Puppet manifest to add custom HTTP header to Nginx configuration

# Declare node or class if necessary
node default {
    # Install Nginx package
    package { 'nginx':
        ensure => installed,
    }

    # Define file path for Nginx configuration file
    $nginx_conf_file = '/etc/nginx/nginx.conf'

    # Add custom HTTP header to Nginx configuration
    file { $nginx_conf_file:
        ensure  => file,
        content => template('nginx/nginx.conf.erb'),
        notify  => Service['nginx'],
    }

    # Define Nginx service
    service { 'nginx':
        ensure    => running,
        enable    => true,
        subscribe => File[$nginx_conf_file],
    }
}
