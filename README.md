# COVERTOVERT
Open source implementation of "network" covert channels.

## What is a Covert Storage Channel?  

>A system feature that enables one system entity to signal information to another entity by directly or indirectly writing to a storage location that is later directly or indirectly read by the second entity.
>
This definition is sourced from the [NIST Computer Security Resource Center](https://csrc.nist.gov/glossary/term/covert_storage_channel#:~:text=Definitions%3A,read%20by%20the%20second%20entity.). Accessed on 27.12.2024.

There exists numerous covert storage channel types, we used Packet Bursting method. Other storage channel methods such as Packet Size Variation and Protocol Field Manipulation implemented by our peers can be found via the main branch of this repository.  

## How does Packet Bursting Work? 

In packet bursting, sender sends the packets in bursts to encode data. Amount of packets in bursts represent different meanings. After each burst there exists a waiting time. For instance: 
- To represent 0 -> 5 packets can be sent.
- To represent 1 -> 3 packets can be sent. 

As a result of waiting time after each burst, receiver can detect the number of packets in each burst. 
Determining the waiting time is crucial for this method. If the burst size is too small, the recevier might not decode the data correctly. Conversely, if it is too large performance of the covert channel will significantly decrease.

## ICMP 

## Implementation 

## Capacity
