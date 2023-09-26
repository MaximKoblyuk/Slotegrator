#1

# for allow all ports 
sudo iptables -A INPUT -s IP_adress -j ACCEPT

# create the chain 
sudo iptables -N INBOUND
sudo iptables -N OUTBOUND

# accept for outbount all ports 
sudo iptables -A ALLOWED_OUTBOUND -j ACCEPT

# Save
sudo service iptables save

#2 and 3

# create user chain
sudo iptables -N ALLOWED_DB_APP

# For IP
sudo iptables -A DB_APP or ON_DEMAND -d 10.72.1.1 -j ACCEPT

# add rulse
sudo iptables -A INPUT -j DB_APP
sudo iptables -A OUTPUT -j DB_APP

# Save
sudo service iptables save


#4 create TEMPORARY_ACCESS with potrs 80,443 and time 
sudo iptables -A TEMPORARY_ACCESS -s 192.168.1.100 -p tcp --dports 80,443 -m time --timestart 01:00 --timestop 23:00 -j ACCEPT


# for loging data, we can use rsyslog
:msg, contains, "Allowed: " -/var/log/iptables-world-ports.log
& stop

sudo iptables -A TEMPORARY_ACCESS -s 192.168.1.100 -p tcp --dports 80,443 -m time --timestart 09:00 --timestop 10:00 -j LOG --log-prefix "Allowed: 192.168.1.100 "

