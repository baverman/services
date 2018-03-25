## Build

    docker build -t baverman/collectd:5.7.2 -t baverman/collectd:latest .

## Run:

    docker run -d --name collectd --restart always --userns=host --pid=host --network=host \
               -u $UID:$GROUPS -v $PWD:/conf baverman/collectd -C /conf/collectd.conf -f
