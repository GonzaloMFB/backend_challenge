HEADERS_SPLITTER = b":"


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
