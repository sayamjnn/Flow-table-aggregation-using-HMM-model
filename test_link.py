class ShortestPath(ControllerBase):
    def __init__(self, req, link, data, **config):
        super(ShortestPath, self).__init__(req, link, data, **config)
        self.dpset = data['dpset']
        self.waiters = data['waiters']
        self.topology_api_app = data['linkapi']  # The app passed here
    
    def get_link_status(self, dpid1, dpid2):
        # Get all links using self.topology_api_app as the app parameter
        links = get_link(self.topology_api_app)
        
        if links is None:
            return Response(status=404)
        
        # Check if a link exists between dpid1 and dpid2
        for link in links:
            src_dpid = dpid_lib.str_to_dpid(link.to_dict()['src']['dpid'])
            dst_dpid = dpid_lib.str_to_dpid(link.to_dict()['dst']['dpid'])
            
            # If the link is between dpid1 and dpid2 (either direction)
            if (src_dpid == dpid1 and dst_dpid == dpid2) or (src_dpid == dpid2 and dst_dpid == dpid1):
                return Response(content_type='application/json', body=json.dumps(link.to_dict()))
        
        # If no link exists between dpid1 and dpid2
        return Response(status=404)

# Example usage:
# To get the link status between two switches (dpid1, dpid2)
dpid1 = "000000000001"  # Example DPID
dpid2 = "000000000002"  # Example DPID
link_status = self.get_link_status(dpid1, dpid2)

