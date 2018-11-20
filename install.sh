chown -R iredadmin:iredadmin .

cp /var/www/iredadmin/settings.py .
ln -s /srv/git/iredadmin /var/www/iredadmin

service uwsgi restart 


cp -f iredadmin.tmpl /etc/nginx/templates
service nginx restart