# apnsend
Python script to test APNS push notifications. Defaults to sending via 
`gateway.push.apple.com`.


# background

This is a tool to send test messages using a valid APNS certificate and
device token.  For more details on how to setup push notifications for
your app and get a certificate, see my steps here:
http://steinn.org/post/apns-setup

# setup

```
$ git clone git@github.com:steinnes/apnsend.git
$ cd apnsend
$ make
```

# usage

Send a normal push notification to an ad-hoc or a distribution build:

```
$ venv/bin/apnsend apns_com.example.app_combined.pem token "hello from apnsend"
```

Send a sandbox notification to a development build:

```
$ venv/bin/apnsend apns_com.example.app_combined.pem token "hello from apnsend" --sandbox
```

