# This script creates a file and sets certain parameters using Puppet

file {'/tmp/holberton':
  ensure  => 'directory',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',
  content => 'I love Puppet',
}