import socket

from .loggers import log_dns, log_ethernet, log_ipv4, log_tcp, log_udp
from .parsers import parse_dns, parse_ethernet, parse_ipv4, parse_tcp, parse_udp

sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0003))
sock.bind(("eth0", 0x0003))

IPV4_TEST = "ipv4_test"


while True:
    print("------------- NEW PACKET --------------")
    raw, addr = sock.recvfrom(65535)
    # Data Link Layer
    dst_mac, src_mac, ethertype, eth_data = parse_ethernet(raw)
    log_ethernet(dst_mac, src_mac, ethertype)
    # Network Layer
    if ethertype == 2048:
        # IPV4
        src_addr, dst_addr, protocol, ip_data = parse_ipv4(eth_data)
        log_ipv4(src_addr, dst_addr, protocol)
    else:
        protocol = None
    # Transport Layer
    if protocol == 17:
        # UDP
        src_port, dst_port, payload = parse_udp(ip_data)
        log_udp(src_port, dst_port)
    elif protocol == 6:
        # TCP
        src_port, dst_port, tcp_flags, payload = parse_tcp(ip_data)
        log_tcp(src_port, dst_port, tcp_flags)
    else:
        tcp_flags = None
        src_port = dst_port = payload = None
        print(" -> Unrecognized protocol.")
    # Application Layer
    if src_port == 53 or dst_port == 53:
        # DNS
        trans_id, dns_flags, question_count, answer_count, payload = parse_dns(payload)
        log_dns(trans_id, dns_flags, question_count, answer_count)
        break
