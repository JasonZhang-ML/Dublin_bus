## /etc/mysql.cnf
c.NotebookApp.ip = '*' #
c.NotebookApp.port = 6666 #
c.NotebookApp.open_browser = False #
c.NotebookApp.notebook_dir = '/root/jupyter_projects' #
c.NotebookApp.allow_root = True #
c.NotebookApp.allow_remote = True

firewall-cmd --zone=public --remove-port=6666/tcp --permanent

### mysql
iptables -I INPUT -p tcp --dport 3306 -j ACCEPT
iptables-save

mysql -h 127.0.0.1 -P 3306 -u root -p
mysql -h 127.0.0.1 -P 23333 -u root -p 168c026afa49a6ff

## Errors in mysql may faced
ERROR 1148 (42000): The used command is not allowed with this MySQL version” when doing LOAD DATA LOCAL FILE with MySQL8.0.18

Error Code: 1292. Truncated incorrect date value: '23-NOV-18 00:00:00'

ERROR 1290 (HY000): The MySQL server is running with the --secure-file-priv option so it cannot execute this statement

Error Code: 1292. Incorrect datetime value: '23-NOV-18 00:00:00' for column 'DAYOFSERVICE' at row 1

Error Code: 1406. Data too long for column 'DataSource' at row 1

Error Code: 1366. Incorrect integer value: '' for column 'ACTUALTIME_DEP' at row 2

Error Code: 1206. The total number of locks exceeds the lock table size

Edit /etc/my.cnf file, and add the following under the [mysqld] heading.
innodb_buffer_pool_size=256M
service mysqld restart

## Errors in linux
ERROR 2002 (HY000): Can't connect to local MySQL server through socket '/tmp/mysql.sock' (2)


### turn off strict mode
vim /etc/my.cnf

sql_mode=NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION

/etc/init.d/mysql restart


## Author
- Jiansheng Zhang