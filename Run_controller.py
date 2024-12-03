import os 
os.system("gnome-terminal -e 'bash -c \"PYTHONPATH=. /home/onos/dynamic_routing/mininet/ryu/bin/ryu-manager /home/onos/dynamic_routing/mininet/ryu/ryu/app/simple_switch.py; exec bash\" ' ")

