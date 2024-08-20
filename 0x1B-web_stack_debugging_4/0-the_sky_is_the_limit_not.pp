# solve task 1 by editing file and setting ulimit to 2000
exec {
    '/usr/bin/env sed -i s/15/2000/ /etc/default/nginx':
} -> exec {
    '/usr/bin/env service nginx restart':
}
