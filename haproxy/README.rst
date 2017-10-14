HAProxy rolling deployment configs
----------------------------------

Basic idea: you have predifined map ``cur-backend`` and frontend check current
value for every request. That allows to set new map entry without haproxy
reload.
