import os
os.system("gnome-terminal -e 'bash -c \"sudo mn --custom /home/onos/dynamic_routing/mininet/SDN-Project/mininet/custom/custom_topology.py --topo create_topo --controller=remote --arp --mac; exec bash\" ' ")
