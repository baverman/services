HAProxy rolling deployment configs
----------------------------------

Basic idea: you have predifined map ``cur-backend`` and frontend check current
value for every request. That allows to set new map entry without haproxy
reload.

Switch::

    ~$ echo 'set map cur-backend cur-backend bob' | sudo socat /tmp/haproxy.sock stdio

    ~$ echo 'get map cur-backend cur-backend' | sudo socat /tmp/haproxy.sock stdio
    type=str, case=sensitive, found=yes, idx=tree, key="cur-backend", value="bob", type="str"

    ~$ echo 'set map cur-backend cur-backend alice' | sudo socat /tmp/haproxy.sock stdio

    ~$ echo 'get map cur-backend cur-backend' | sudo socat /tmp/haproxy.sock stdio
    type=str, case=sensitive, found=yes, idx=tree, key="cur-backend", value="alice", type="str"
