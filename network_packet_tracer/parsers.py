import struct


def parse_ethernet(data):
    # MAC address fields are 6 bytes -> 48 bits -> 12 hex digits.
    # Type is 2 bytes -> 16 bits -> 4 hex digits
    dst = data[0:6]
    dst_mac = ":".join(f"{b:02x}" for b in dst)
    src = data[6:12]
    src_mac = ":".join(f"{b:02x}" for b in src)
    ethertype = struct.unpack("!H", data[12:14])[0]
    data = data[14:]
    return dst_mac, src_mac, ethertype, data


def parse_ipv4(data):
    version_and_ihl = data[0]
    ihl = version_and_ihl & 0x0F
    version = (version_and_ihl & 0xF0) >> 4
    header_length_bytes = ihl * 32 // 8
    protocol = data[9]
    src_addr = data[16:20]
    dst_addr = data[20:24]
    payload = data[header_length_bytes:]
    return src_addr, dst_addr, protocol, payload


def parse_udp(data):
    # UDP header: 8 bytes, 2 for each 4 fields:
    #     16 bit       16 bit
    # |------------|------------|
    # |  src port  |  dst port  |
    # |------------|------------|
    # |  length    |  checksum  |
    # |------------|------------|

    src_port = struct.unpack("!H", data[0:2])[0]
    dst_port = struct.unpack("!H", data[2:4])[0]
    length = struct.unpack("!H", data[4:6])[0]
    checksum = struct.unpack("!H", data[6:8])[0]
    payload = data[8:]
    return src_port, dst_port, payload


def parse_tcp(data):
    # TCP Header (minimum 20 bytes)
    # Byte
    # 0               1               2               3
    # +---------------+---------------+---------------+---------------+
    # |        Source Port (16 bits)  |   Destination Port (16 bits)  |
    # +---------------+---------------+---------------+---------------+
    # |                     Sequence Number (32 bits)                 |
    # +---------------+---------------+---------------+---------------+
    # |                  Acknowledgment Number (32 bits)              |
    # +---------------+---------------+---------------+---------------+
    # | Data | Res |N|C|E|U|A|P|R|S|F|           Window Size          |
    # |Off(4)| (3) |S|W|C|R|C|S|S|Y|I|             (16 bits)          |
    # +---------------+---------------+---------------+---------------+
    # |           Checksum            |        Urgent Pointer         |
    # +---------------+---------------+---------------+---------------+
    # |                    Options (0–40 bytes) + Padding             |
    # +---------------+---------------+---------------+---------------+
    src_port = struct.unpack("!H", data[0:2])[0]
    dst_port = struct.unpack("!H", data[2:4])[0]
    sqn_num = struct.unpack("!L", data[4:8])[0]
    ack_num = struct.unpack("!L", data[8:12])[0]

    # data offset -> header size reserved and flags are 2 bytes total (12:14).
    # Extract using masks
    data_offset = (data[12] & 0xF0) >> 4
    data_offset_bytes = (
        data_offset * 32 // 8
    )  # also in 32-bit words so convert to bytes
    # Extract flags
    # NS is an older, rarely-used flag. Most packet tracers focus on the 8 in byte 13.
    flags = data[13]
    tcp_flags = {
        "fin": bool(flags & 0x01),
        "syn": bool(flags & 0x02),
        "rst": bool(flags & 0x04),
        "psh": bool(flags & 0x08),
        "ack": bool(flags & 0x10),
        "urg": bool(flags & 0x20),
        "ece": bool(flags & 0x40),
        "cwr": bool(flags & 0x80),
    }

    window_size = struct.unpack("!H", data[14:16])[0]
    checksum = struct.unpack("!H", data[16:18])[0]
    urgent_ptr = struct.unpack("!H", data[18:20])[0]

    payload = data[data_offset_bytes:]
    return src_port, dst_port, tcp_flags, payload


def parse_dns(data):
    # DNS Header (12 bytes)
    # Byte
    # 0               1
    # +---------------+---------------+
    # |        Transaction ID         |
    # |           (16 bits)           |
    # +---------------+---------------+
    # |              Flags            |
    # |           (16 bits)           |
    # +---------------+---------------+
    # |             QDCOUNT           |
    # |     Number of Questions       |
    # |           (16 bits)           |
    # +---------------+---------------+
    # |             ANCOUNT           |
    # |      Number of Answers        |
    # |           (16 bits)           |
    # +---------------+---------------+
    # |             NSCOUNT           |
    # |  Number of Authority RRs      |
    # |           (16 bits)           |
    # +---------------+---------------+
    # |             ARCOUNT           |
    # |  Number of Additional RRs     |
    # |           (16 bits)           |
    # +---------------+---------------+
    trans_id = struct.unpack("!H", data[0:2])[0]
    flags = struct.unpack("!H", data[2:4])[0]
    # Multi-bit flags: opcode, z, rcode.
    dns_flags = {
        "qr": bool(flags & 0x8000),
        "opcode": (flags & 0x7800) >> 11,
        "aa": bool(flags & 0x0400),
        "tc": bool(flags & 0x0200),
        "rd": bool(flags & 0x0100),
        "ra": bool(flags & 0x0080),
        "z": (flags & 0x0070) >> 4,
        "rcode": flags & 0x000F,
    }
    question_count = struct.unpack("!H", data[4:6])[0]
    answer_count = struct.unpack("!H", data[6:8])[0]
    auth_rr_count = struct.unpack("!H", data[8:10])[0]
    addit_rr_count = struct.unpack("!H", data[10:12])[0]
    payload = data[12:]
    return trans_id, dns_flags, question_count, answer_count, payload
