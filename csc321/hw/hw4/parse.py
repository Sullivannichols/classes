#!/usr/bin/env python3

import csv
import socket
import pygraphviz as pgv

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
