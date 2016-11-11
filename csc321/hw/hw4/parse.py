#!/usr/bin/env python3

import csv
import socket
<<<<<<< HEAD
import pygraphviz as pgv
=======
import networkx as nx
import matplotlib.pyplot as plt

# LOOK AT urllib.parse for parsing the urls from the reverse lookups
# Add database functionality. Check if a database exists, if not, then create
# one, run the lookups, and populate the databse. If the database already
# exists, pull the lookup data from the database and populate the graph with
# the information.
>>>>>>> aa7d81b4bce280210d93c4c06843372cfd53e390

def domains():
    ''' This function extracts domain names from a .tsv file, performs a
        forward DNS lookup on each domain, performs a reverse DNS lookup on
        each returned IP, then adds all of the info to a graph.
    '''
    g = pgv.AGraph()
    with open('domains.tsv', newline='') as tsvfile:
        tsvin = csv.DictReader(tsvfile, delimiter='\t')
        print("domains.tsv loaded into dictionary") 
        for line in tsvin:
            # Forward Lookup
            domain = line['domain']
            g.add_node(domain)
            print("node added for " + domain)
            try:
                ips = socket.gethostbyname_ex(domain)            
            except socket.gaierror:
                print("socket.gaierror: nodename nor servname provided")
                continue

            # Reverse Lookup
            for item in ips[2]:
                noerror = True
                try:
                    result = socket.getfqdn(item)
                except:
                    print('REVERSE DNS ERROR for ' + result)
                    noerror = False
                    continue
                if noerror:
                    # parse domain names
                    result = result.split(".")
                    result = ".".join(len(result[-2]) < 4 and\
                        result[-3:] or result[-2:])
                    # add nodes
                    g.add_node(result)
                    g.add_edge(domain, result)
                    print("node added for " + result)
                    print("edge added between " + domain + " and " + result)
    g.layout(args='-Goverlap=false')
    g.draw('simple.png')

if __name__ == '__main__':
    domains()
