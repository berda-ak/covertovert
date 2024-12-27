from CovertChannelBase import CovertChannelBase
from scapy.all import sniff,IP,ICMP,send
import time

class MyCovertChannel(CovertChannelBase):
    """
    - You are not allowed to change the file name and class name.
    - You can edit the class in any way you want (e.g. adding helper functions); however, there must be a "send" and a "receive" function, the covert channel will be triggered by calling these functions.
    """
    def __init__(self):
        """
        - You can edit __init__.
        """
        super().__init__()
        self.message = ""
        self.flag = False
        self.packet_count = 0
        self.bits=[]
        self.b_num = 0
        self.start_flag = True
        self.wait_time = 0.2
    

    def wait(self):
        time.sleep(self.wait_time )
            
    def send(self, log_file_name, first_burst_num, second_burst_num):
        """
        - In this function, you expected to create a random message (using function/s in CovertChannelBase), and send it to the receiver container. Entire sending operations should be handled in this function.
        - After the implementation, please rewrite this comment part to explain your code basically.
        """

        # 1 is 2 packets, 
        # 0 is 3 packets
        # waiting time ?
        #code for performance test
        rec_IP = "172.18.0.3"
        starting_time = time.time()
        binary_message = self.generate_random_binary_message_with_logging(log_file_name, min_length=50 ,max_length=100)
        for i in range(len(binary_message)):
            if binary_message[i] ==  '1':
                #send_two_packets change packet numbers give bigger to test the code, after ur sure u have no error proceed to smaller packet numbers
                for j in range(first_burst_num):
                    packet1 = IP(dst = rec_IP) / ICMP() 
                    super().send(packet1) 
                self.wait()
                
            else:
                #send_three_packets
                for j in range(second_burst_num):
                    packet1 = IP(dst = rec_IP) / ICMP() 
                    super().send(packet1) 
                self.wait()

        last_packet = IP(dst = rec_IP) / ICMP()
        super().send(last_packet)

        performance = 128/(time.time() - starting_time)
        print("Covert Channel Performance: ", performance)

    def receive(self, first_burst_num, second_burst_num, parameter3, log_file_name):
        """
        - In this function, you are expected to receive and decode the transferred message. Because there are many types of covert channels, the receiver implementation depends on the chosen covert channel type, and you may not need to use the functions in CovertChannelBase.
        - After the implementation, please rewrite this comment part to explain your code basically.
        """
        # biraz da error katarak idle time belirlemece slay

        def receivePacket(packet):

            if self.start_flag:
                self.start_time = time.time()
                self.start_flag = False

            

            in_time_interval = (time.time() - self.start_time ) > self.wait_time 

            #if in_time_interval and self.packet_count < 5:
            if packet and packet.haslayer(ICMP) and packet[ICMP].type == 8: # and packet[ICMP].type == 8 do we need echo messages
                #print("packet received",(time.time() - self.start_time ))
                self.packet_count+=1

            if(first_burst_num<second_burst_num):
                if in_time_interval:
                #print("packet count", self.packet_count)
                    if self.packet_count < (first_burst_num+1):
                        self.bits.append(1)
                        self.b_num+=1
                        self.packet_count = 0
                        self.start_flag = True
                    else:
                        self.bits.append(0)
                        self.b_num+=1
                        self.packet_count = 0
                        self.start_flag = True
            else:
                if in_time_interval:
                    #print("packet count", self.packet_count)
                    if self.packet_count < (second_burst_num+1):
                        self.bits.append(1)
                        self.b_num+=1
                        self.packet_count = 0
                        self.start_flag = True
                    else:
                        self.bits.append(0)
                        self.b_num+=1
                        self.packet_count = 0
                        self.start_flag = True
            
            
            

            if self.b_num == 8:
                #print("bits :", ''.join(map(str, self.bits)))
                self.message += self.convert_eight_bits_to_character(''.join(map(str, self.bits)))
                self.b_num = 0
                self.bits = []
                #print(self.message)

                if self.message[-1] == '.': 
                    #print("bitti------------------------------------")
                    #print("message", self.message) 
                    self.log_message(message = self.message, log_file_name=log_file_name)
                    self.flag = True 


        
    
        def getFlag(packet):
            return self.flag

        

        sniff(filter="icmp", prn = receivePacket, stop_filter = getFlag)  # should i put in init func???

              
