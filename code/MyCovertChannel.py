from CovertChannelBase import CovertChannelBase
from scapy.all import sniff,IP,ICMP,send
import time

class MyCovertChannel(CovertChannelBase):
    """
    - You are not allowed to change the file name and class name.
    - You can edit the class in any way you want (e.g. adding helper functions); however, there must be a "send" and a "receive" function, the covert channel will be triggered by calling these functions.
    """
    def _init_(self):
        """
        - You can edit _init_.
        """
        self.message = ""
        self.flag = False
        self.packet_count = 0
    

    def wait(self):
        time.sleep(0.5)
            
    def send(self, log_file_name, parameter1, parameter2):
        """
        - In this function, you expected to create a random message (using function/s in CovertChannelBase), and send it to the receiver container. Entire sending operations should be handled in this function.
        - After the implementation, please rewrite this comment part to explain your code basically.
        """

        # 1 is 2 packets, 
        # 0 is 3 packets
        # waiting time ?
        
        binary_message = self.generate_random_binary_message_with_logging(log_file_name)
        
        rec_IP = "172.18.0.3"
        
        for i in range(len(binary_message)):
            if binary_message[i] ==  '1':
                #send_two_packets change packet numbers give bigger to test the code, after ur sure u have no error proceed to smaller packet numbers
                packet1 = IP(dst = rec_IP) / ICMP() 
                packet2 = IP(dst = rec_IP) / ICMP()
                send(packet1) 
                send(packet2) #send kontrol et
                self.wait()
            else:
                #send_three_packets
                packet1 = IP(dst = rec_IP) / ICMP() 
                packet2 = IP(dst = rec_IP) / ICMP() 
                packet3 = IP(dst = rec_IP) / ICMP() 
                send(packet1)
                send(packet2)
                send(packet3)
                self.wait()

        
        

    
        
    def receive(self, parameter1, parameter2, parameter3, log_file_name):
        """
        - In this function, you are expected to receive and decode the transferred message. Because there are many types of covert channels, the receiver implementation depends on the chosen covert channel type, and you may not need to use the functions in CovertChannelBase.
        - After the implementation, please rewrite this comment part to explain your code basically.
        """
        # biraz da error katarak idle time belirlemece slay


        def receivePacket(packet):

            print("packet received")

            in_time_interval = True

            if in_time_interval and self.packet_count < 4:
                if packet and packet.haslayer(ICMP) : # and packet[ICMP].type == 8 do we need echo messages
                    self.packet_count+=1
            else:
                if self.packet_count < 4:
                    print("if")
                    bits.append(0)
                    b_num+=1
                    self.packet_count = 0
                else:
                    print("else")
                    bits.append(1)
                    b_num+=1
                    self.packet_count = 0
            
            print("bits :", bits)

            if b_num == 8:
                self.message += convert_to_char(bits)
                b_num = 0
                print("bits 8----:", bits)
                bits = []
        
    
        def getFlag(packet):
            print("flag " , self.flag)
            return self.flag


        sniff(filter="icmp", prn = receivePacket, stop_filter = getFlag)  # should i put in init func???
              
        if self.message and self.message[-1] == '.':
	        self.flag = True 


        if self.flag:
            self.log_message(self.message, log_file_name)
            self.message = ""
            self.flag = False
