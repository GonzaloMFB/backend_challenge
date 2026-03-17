def http_parser(input: bytes):
    main_splitter = b"\r\n\r\n"

    is_crlf = input.find(main_splitter) != -1
    if not is_crlf:
        main_splitter = b"\n\n"
    header_section, body = input.split(main_splitter)

    subsplitter = b"\r\n" if is_crlf else b"\n"
    header_section = header_section.split(subsplitter)
    req_type = header_section[0]
    headers = header_section[1:]

    return {"method": req_type, "headers": headers, "body": body}
