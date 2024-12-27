# Covert Storage Channel that exploits Packet Bursting using ICMP [Code: CSC-PB-ICMP]

This project uses Covert Storage Channel that exploits Packet Bursting using ICMP [Code: CSC-PB-ICMP]

## What is a Covert Storage Channel?  

>A system feature that enables one system entity to signal information to another entity by directly or indirectly writing to a storage location that is later directly or indirectly read by the second entity.
>
This information is sourced from the [NIST Computer Security Resource Center](https://csrc.nist.gov/glossary/term/covert_storage_channel#:~:text=Definitions%3A,read%20by%20the%20second%20entity.). Accessed on 27.12.2024.

There exists numerous covert storage channel types, we used Packet Bursting method. Other storage channel methods such as Packet Size Variation and Protocol Field Manipulation implemented by our peers can be found via the main branch of this repository.  

## How does Packet Bursting Work? 

In packet bursting, sender sends the packets in bursts to encode data. Amount of packets in bursts represent different meanings. After each burst there exists a waiting time. For instance: 
- To represent 0 -> 5 packets can be sent.
- To represent 1 -> 3 packets can be sent. 

As a result of waiting time after each burst, receiver can detect the number of packets in each burst. 
Determining the waiting time is crucial for this method. If the burst size is too small, the recevier might not decode the data correctly. Conversely, if it is too large performance of the covert channel will significantly decrease.

## ICMP 
>The Internet Control Message Protocol (RFC 792) was designed to provide network connectivity information to administrators and applications.
>
ICMP (Internet Message Control Protocol) is a Network Layer protocol mainly used by routers. It operates on top of IP. Since it is a Network Layer protocol, it does not utilize the concept of ports unlike Transport Layer prtocols such as UDP and TCP. Hence, pinging a port is not possible. Common Types of ICMP are as follows:
- Type  0 : Echo Reply
- Type  3 : Destination Unreachable
- Type  5 : Redirect
- Type  8 : Echo Request
- Type 11 : Time Exceeded
- Type 13 : Timestamp Request
- Type 14 : Timestamp Reply
- Type 17 : Address Mask Request
- Type 18 : Address Mask Reply
- Type 30 : Traceroute

This information is sourced from the [An ICMP Reference by Daniel Miessler](https://danielmiessler.com/study/icmp). Accessed on 27.12.2024.
In this project Type 8, echo request is used. 

## Implementation 
In the app folder there exists there exists 6 files: 

### CovertChannelBase.py
This is the base file consists mainly used methods such as 
- send() which uses send method of scapy, 
- log_message() that logs the received message
- convert_string_message_to_binary(), generate_random_binary_message(), generate_random_binary_message_with_logging(),
- sleep_random_time_ms() not used in this project since it is not a timing channel, convert_eight_bits_to_character() that converts recieved 8 bits to character.

These methods are used in MyCovertChannel.py file.
### MyCovertChannel.py

### MyCovertChannel_performance.py
This file is mainly the same with MyCovertChannel.py. It was implemented to calculate capacity of the covert channel. A 128 bits random message is created, and the time is measured. Results are given in [capacity](#capacity) section. 
### config.json
### run.py
### Makefile

## Capacity
