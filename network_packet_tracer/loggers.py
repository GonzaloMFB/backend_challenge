from .utils import ETHERTYPES, IP_PROTOCOLS


def format_ipv4_address(data: bytes):
    return ".".join([str(b) for b in data[:4]])


def log_ethernet(dst_mac, src_mac, ethertype):
    _ethertype = ETHERTYPES.get(ethertype)
    print(f"[Ethernet]\n src: {src_mac} | dst: {dst_mac} | type: {_ethertype}")


def log_ipv4(src_addr, dst_addr, protocol):
    tp_protocol = IP_PROTOCOLS.get(protocol)
    print(
        f"[IPv4]\n src: {format_ipv4_address(src_addr)} | dst: {format_ipv4_address(dst_addr)} | protocol: {tp_protocol}"
    )


def log_dns(id, flags, q_count, a_count):
    rcode = flags.get("rcode")
    print(
        f"[DNS]\n id: {id} | rcode: {rcode} | q_count: {q_count} | a_count: {a_count}"
    )


def log_udp(src_port, dst_port):
    print(f"[UDP]\n src: {str(src_port)} | dst: {str(dst_port)}")


def log_tcp(src_port, dst_port, tcp_flags):
    active_flags = [flag for flag in tcp_flags if tcp_flags[flag]]
    active_flags = ", ".join(active_flags)
    print(f"[TCP]\n src: {src_port} | dst: {dst_port} | flags: {active_flags}")
