Brandon Randle
2016 November 01
Network Management Notes

### Network Testing

## Purpose of Testing
  - Pinpoint/indentify problem source
  - "What do I send?"
    - Put data on the network.
    - Create data to put on the network.
  - "What do I receive?"
    - If I have a client sending data with evidence that it's sent, but the 
      data never arrives, there's something wrong with the network.

## Purpose of Network (IT)?
  - Provide IT services
  - Support the organisation's goals

## Strategies for Testing
  - Prepare and send normal (normal-scale) data
    - "Normal" traffic is always acceptable.
  - Craft abnormal data
    - load tester
      - purpose is to be able to test the load that something can bear
      - increases bandwidth of sent data
      - concurrency (10s of 1000s of client connections)
        - can quickly saturate the network
    - port scanners
      - Port scanning is HIGHLY ILLEGAL!!!!!111one
        - Unless you own the resource and every bit of networking between
      - Intrusion detection system (IDS)
        - looks for this activity
    - why load test/port scan? 
      - to test network
