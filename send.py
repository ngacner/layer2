from winpcapy import WinPcapUtils
# Build a packet buffer
# This example-code is built for tutorial purposes, for actual packet crafting use modules like dpkt
arp_request_hex_template = "%(dst_mac)s%(src_mac)s08060001080006040001" \
                           "%(sender_mac)s%(sender_ip)s%(target_mac)s%(target_ip)s" + "00" * 18
packet = arp_request_hex_template % {
    "dst_mac": "aa"*6,
    "src_mac": "bb"*6,
    "sender_mac": "bb"*6,
    "target_mac": "cc"*6,
    # 192.168.0.1
    "sender_ip": "c0a80001",
    # 192.168.0.2
    "target_ip": "c0a80002"
}
# Send the packet (ethernet frame with an arp request) on the interface
WinPcapUtils.send_packet("*Ethernet*", packet.decode("hex"))