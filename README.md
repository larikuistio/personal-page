# personal-page

My personal website
https://kuistio.me

## run locally

```shell
python3 -m venv env
source env/bin/activate
pip install -r requirements
export FLASK_APP=app.py
flask run
```

## deploy on server

Reverse proxy with nginx to 127.0.0.1:50000

systemd service
```shell
[Unit]
Description = kuistio.me
After = network.target

[Service]
PermissionsStartOnly = true
PIDFile = /run/kuistio.me/kuistio.me.pid
User = lari
Group = lari
WorkingDirectory = /home/lari/personal-page
Environment = /home/lari/personal-page/env/bin
ExecStartPre = /bin/mkdir /run/kuistio.me
ExecStartPre = /bin/chown -R lari:lari /run/kuistio.me
ExecStart = /home/lari/personal-page/env/bin/gunicorn wsgi:app --bind=127.0.0.1:50000 --workers=4 --pid /run/kuistio.me/kuistio.me.pid
ExecReload = /bin/kill -s HUP $MAINPID
ExecStop = /bin/kill -s TERM $MAINPID
ExecStopPost = /bin/rm -rf /run/kuistio.me
PrivateTmp = true

[Install]
WantedBy = multi-user.target
```
