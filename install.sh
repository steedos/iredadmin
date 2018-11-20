chown -R iredadmin:iredadmin .

rm -f /var/www/iredadmin
ln -s /srv/git/iredadmin /var/www/iredadmin

service uwsgi restart 