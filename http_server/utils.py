HEADERS_SPLITTER = b":"
HTTP_STATUS = {
    100: b"Continue",
    101: b"Switching Protocols",
    102: b"Processing",
    103: b"Early Hints",
    200: b"OK",
    201: b"Created",
    202: b"Accepted",
    203: b"Non-Authoritative Information",
    204: b"No Content",
    205: b"Reset Content",
    206: b"Partial Content",
    207: b"Multi-Status",
    208: b"Already Reported",
    226: b"IM Used",
    300: b"Multiple Choices",
    301: b"Moved Permanently",
    302: b"Found",
    303: b"See Other",
    304: b"Not Modified",
    305: b"Use Proxy",
    307: b"Temporary Redirect",
    308: b"Permanent Redirect",
    400: b"Bad Request",
    401: b"Unauthorized",
    402: b"Payment Required",
    403: b"Forbidden",
    404: b"Not Found",
    405: b"Method Not Allowed",
    406: b"Not Acceptable",
    407: b"Proxy Authentication Required",
    408: b"Request Timeout",
    409: b"Conflict",
    410: b"Gone",
    411: b"Length Required",
    412: b"Precondition Failed",
    413: b"Payload Too Large",
    414: b"URI Too Long",
    415: b"Unsupported Media Type",
    416: b"Range Not Satisfiable",
    417: b"Expectation Failed",
    418: b"I'm a teapot",
    421: b"Misdirected Request",
    422: b"Unprocessable Entity",
    423: b"Locked",
    424: b"Failed Dependency",
    425: b"Too Early",
    426: b"Upgrade Required",
    428: b"Precondition Required",
    429: b"Too Many Requests",
    431: b"Request Header Fields Too Large",
    451: b"Unavailable For Legal Reasons",
    500: b"Internal Server Error",
    501: b"Not Implemented",
    502: b"Bad Gateway",
    503: b"Service Unavailable",
    504: b"Gateway Timeout",
    505: b"HTTP Version Not Supported",
    506: b"Variant Also Negotiates",
    507: b"Insufficient Storage",
    508: b"Loop Detected",
    510: b"Not Extended",
    511: b"Network Authentication Required",
}


def http_parser(input: bytes):
    main_splitter = b"\r\n\r\n"

    is_crlf = input.find(main_splitter) != -1
    if not is_crlf:
        main_splitter = b"\n\n"
    header_section, body = input.split(main_splitter)

    subsplitter = b"\r\n" if is_crlf else b"\n"
    header_section = header_section.split(subsplitter)
    firstline = parse_firstline(header_section[0])
    headers = parse_headers(header_section[1:])

    return {"firstline": firstline, "headers": headers, "body": body}


def parse_firstline(input: bytes):
    method, req_uri, version = input.split(b" ")
    return {"method": method, "req_uri": req_uri, "version": version}


def parse_headers(input: list):
    headers = {}
    for h in input:
        splitter_idx = h.find(HEADERS_SPLITTER)
        if splitter_idx in (-1, len(h) - 1):
            print("Bad header:", h)
            continue
        a = h[0:splitter_idx]
        b = h[splitter_idx + 1 :]
        headers[a.strip()] = b.strip()
    return headers


def response_formatter(status, body, headers={}, is_crlf=True):
    response = []
    joiner = "\r\n" if is_crlf else "\n"
    if status not in HTTP_STATUS:
        print("Unknown code")
        return

    # first line
    firstline = f"HTTP/1.1 {status} {HTTP_STATUS[status]}"
    response.append(firstline)
    # Headers
    for key, val in headers.items():
        header_line = f"{key}: {val}"
        response.append(header_line)
    # Blank line
    response.append("")
    # body
    response.append(body)

    response = joiner.join(response)
    return bytes(response, encoding="utf-8")
