# This script allows Nginx to function better by increasing the number of allowed requests
exec { 'limit':
  command => "sed -i -e 's/15/8192/g' /etc/default/nginx; service nginx restart",
  path    => ['/bin', '/usr/bin', '/usr/sbin']
}