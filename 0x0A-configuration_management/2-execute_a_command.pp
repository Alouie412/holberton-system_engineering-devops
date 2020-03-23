# This script executes a command using Puppet. In this case, kills a process

exec {'killmenow':
  command => 'pkill',
}