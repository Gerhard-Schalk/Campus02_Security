# AWS Example

## Tools - download and installation
OpenSSL Windows Binary: https://slproweb.com/products/Win32OpenSSL.html<br>
OpenSSL MAC installation guide https://macappstore.org/openssl/<br>
OpenSSL Linux installation: ```sudo apt install openssl```<br>

Wireshark https://www.wireshark.org/download.html<br>

MQTT Explorer (portable): http://mqtt-explorer.com/<br>

## Create AWS credentials (keys and certificates)

Generate a client RSA key
```
openssl genrsa -out aws_demo_device.key 2048
```
Now we can check the private RSA Key

```
openssl rsa -in aws_demo_device.key -check
```

To view the key's details, you can use the following OpenSSL command:

```
openssl rsa -in aws_demo_device.key -noout -text
```

Next, we create a signing request file for the for private RSA key

(Wikipedia https://de.wikipedia.org/wiki/Certificate_Signing_Request)

**Note:**  The Common Name (CN) needs to match the hostname of your broker!
          For your example we need to use **"10.0.0.1"**.
```
openssl req -out aws_demo_device.csr -key aws_demo_device.key -new
```
```
Use the following OpenSSL command to check and print the the Certificate Signing Request (CSR) in text form:

```
openssl req -text -verify -in aws_demo_device.csr -noout
```

Now we can upload our Certificate Signing Request (csr) file to AWS IoT and create the device certificate.

Use OpenSSL to print the device certificate in text form:

```
openssl x509 -in aws_demo_device.crt -text -noout
```
Now you can use the AWS credentials (keys and certificates) to run the aws_basicPubSub.py example to connect to AWS via MQTT and TLS. 

## Wireshark Example
Task: Use Wireshark to analyze the connection.

Wireshark filter setting:

```
tcp.port == 8883 && tls
```
