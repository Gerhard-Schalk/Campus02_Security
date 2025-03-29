# Create AWS credentials (keys and certificates)

## Generate a client RSA key:
```
openssl genrsa -out aws_demo_device.key 2048
```
Now we can check the private RSA Key:

```
openssl rsa -in aws_demo_device.key -check
```
**Note:** ```aws_demo_device.key``` contains the RSA key pair (the private and the public key). **Never share this file!**<br/>
          We will only share the public key as part of the Certification Signing Request (CRS) with AWS IoT core.<br/>
To view the key's details, you can use the following OpenSSL command:
```
openssl rsa -in aws_demo_device.key -noout -text
```
## Create a Certificate Signing Request (CSR)
Next, we create a Certificate Signing Request (CSR) file for the public RSA key.<br> 
(for more details see: https://azure.github.io/IoTTrainingPack/modules/Certificates101/02_x509.html)

```
openssl req -out aws_demo_device.csr -key aws_demo_device.key -new
```

Use the following OpenSSL command to check and print the the Certificate Signing Request (CSR) in text form:

```
openssl req -text -verify -noout -in aws_demo_device.csr
```

## Upload our Certificate Signing Request (CSR) file to AWS IoT Core
Now you can upload our Certificate Signing Request (csr) file to AWS IoT Core (www.aws.com), create a new IoT device ("Thing") and create the IoT device ("Thing" ) certificate.
AWS IoT Core will check the CSR Signature and create a certificate (convert CRS into a X.509 certificate and sign it with the AWS private key).


## Downlaod all credentials (keys and certificates) from AWS.
Download your device ("Thing") certificate.

Use OpenSSL to print the device ("Thing") certificate in text form:

```
openssl x509 -text -noout -in <your file name>.crt
```

Downlaod the Amazon RSA Root Certificate - Amazon Root CA1 using the following command:
```
curl https://www.amazontrust.com/repository/AmazonRootCA1.pem -o AmazonRootCA1.pem
```

Use OpenSSL to print the Amazon Root CA1.

```
openssl x509 -text -noout -in AmazonRootCA1.pem 
```


# Setup and execute AWS examples 
Now you can use the AWS credentials (keys and certificates) to run the python aws_basicPubSub.py example to connect to AWS via MQTT and TLS. 

# Wireshark Example
Task: Use Wireshark to analyze the TLS connection.

Wireshark filter setting:

```
tcp.port == 8883 && tls
```
