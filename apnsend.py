import sys
import json
import click
import socket
import struct

import OpenSSL
from OpenSSL import SSL, crypto


def encode_notification(token, notification):
    notification = json.dumps(notification, ensure_ascii=False).encode('utf-8')
    wire_format = "!BH32sH%ds" % len(notification)
    packed = struct.pack(
        wire_format,
        0,
        32,
        token.decode('hex'),
        len(notification),
        notification)
    return packed


def send(ctx, notification):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)
    connection = SSL.Connection(ctx, sock)
    connection.connect(("gateway.sandbox.push.apple.com", 2195))
    connection.setblocking(1)

    try:
        connection.do_handshake()
    except OpenSSL.SSL.WantReadError:
        print "Timeout"
        sys.exit(1)

    expected = len(notification)
    sent = connection.send(notification)
    if sent < expected:
        print "Whoops, notification len=%d sent=%d\n" % (expected, sent)
    else:
        print "Looks like everything got sent!"


@click.command()
@click.argument('pem_file')
@click.argument('token')
@click.argument('message')
def main(pem_file, token, message):
    notification = encode_notification(
        token, {'aps': {'alert': message, 'sound': 'default'}}
    )

    with open(pem_file) as f:
        pem_file_data = f.read()

        ssl_ctx = SSL.Context(SSL.TLSv1_METHOD)
        cert = crypto.load_certificate(crypto.FILETYPE_PEM, pem_file_data)
        pkey = crypto.load_privatekey(crypto.FILETYPE_PEM, pem_file_data)
        ssl_ctx.use_certificate(cert)
        ssl_ctx.use_privatekey(pkey)

        send(ssl_ctx, notification)


if __name__ == "__main__":
    main()
