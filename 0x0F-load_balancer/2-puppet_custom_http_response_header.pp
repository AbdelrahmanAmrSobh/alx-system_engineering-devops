# Custom HTTP header in a nginx server
exec { 'update server':
  command  => 'sudo apt-get update',
  provider => 'shell',
}
->
package { 'download nginx':
  ensure   => 'present',
}
->
file_line { 'add HTTP header':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'add_header X-Served-By $hostname;'
}
->
exec { 'restart'
  command  => 'sudo service nginx restart',
  provider => 'shell',
}
