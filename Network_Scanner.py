import scapy.all as scapy
import optparse

#1) arp request
#2) broadcast
#3) response

def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i" , "--ipaddress" ,dest="ip_address",help="ENTER IP ADDRESS")

    (user_input,arguments) = parse_object.parse_args()

    if not user_input.ip_addrees:
        print("ENTER IP ADDRESS")

    return user_input

def arp_rep_pack(arp_ip):

    arp_request_packet = scapy.ARP(pdst=arp_ip)
    #scapy.ls(scapy.ARP()) ---> bu komut bilgi verir. arp hakkında

    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    #scapy.ls(scapy.Ether()) ---> bu komut bilgi verir.

    combined_packet = broadcast_packet/arp_request_packet
    (answered_list,unanswered_list) = scapy.srp(combined_packet,timeout=1)
    answered_list.summary()


    user_ip_address =get_user_input()
    arp_rep_pack(user_ip_address.ip_address)