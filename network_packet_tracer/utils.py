ETHERTYPES = {2048: "IPv4"}
IP_PROTOCOLS = {7: "TCP", 17: "UDP"}


# For saving and loading packets.
def save_packet(filepath, data):
    with open(filepath, "wb") as f:
        f.write(data)


def load_packet(filepath):
    with open(filepath, "rb") as f:
        return bytes(f.read())
