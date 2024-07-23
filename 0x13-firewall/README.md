# config firewall using UFW

UFW is an interface to linux built in firewall iptables
UFW is easier to use for beginners

First task is to deny all request that aren't using HTTP, HTTPS, SSH on their correct port

Second task is to allow redirect from port 8080 to port 80
Nginx wasn't listening on 8080 so I made it listen on 8080

first task is applied on web-01, web-02 and lb-01
second task is applied on web-01 and web-02