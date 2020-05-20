# This Puppet script fixes a typo that causes error 500 on Wordpress. ...Seriously?
exec { 'replace':
  command   => "sed -i -e 's/class-wp-locale.phpp/class-wp-locale.php/g' /var/www/html/wp-settings.php",
  path      =>  '/bin',
}
