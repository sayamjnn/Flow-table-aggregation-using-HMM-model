import os
os.system("gnome-terminal -e 'bash -c \"PYTHONPATH=. /home/onos/dynamic_routing/mininet/ryu/bin/ryu-manager --verbose --observe-links /home/onos/dynamic_routing/mininet/ryu/ryu/app/bestpath.py /home/onos/dynamic_routing/mininet/ryu/ryu/app/ofctl_rest.py; exec bash\" ' ")


