# This Puppet manifest installs Flask version 2.1.0 using pip3.
package { 'werkzeug':
  ensure   => '2.0.3',
  provider => 'pip3',
}

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['werkzeug'],
}
