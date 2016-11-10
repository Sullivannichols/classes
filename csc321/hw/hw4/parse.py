#!/usr/bin/env python3

import csv
import socket
import networkx as nx
import matplotlib.pyplot as plt

class DNSGraph:

    def __init__(self):
        self.domainfile = 'domains.tsv'
        self.graph = nx.Graph()
        
    def domains(self):
        ''' This function extracts domain names from a .tsv file, performs 
            a forward DNS lookup for the domain, then performs a reverse 
            DNS lookup for each IP gained from the forward DNS lookup, then
            stores the information in a FORMAT TO BE DETERMINED.
        '''
        with open(self.domainfile, newline='') as tsvfile:
            tsvin = csv.DictReader(tsvfile, delimiter='\t')
            for line in tsvin:
                # Forward Lookup
                # ADD NODE FOR DOMAIN
                try:
                    ips = socket.gethostbyname_ex(line['domain'])            
                except:
                    print('FORWARD DNS ERROR') 
                    continue

                # Reverse Lookup
                try:
                    for item in ips[2]:
                        result = socket.gethostbyaddr(item)
                        # PARSE RESULT
                        # ADD NODES FOR EACH DOMAIN ASSOCIATED WITH IP
                except:
                    print('REVERSE DNS ERROR')
                    continue

    def graph():
        ''' This function graphs the data gained from domains() '''
        nx.draw(G)
        plt.show()

if __name__ == '__main__':
    g = DNSGraph()
    g.domains()
    g.graph
