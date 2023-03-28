# MQTT client authentication using TLS

## Step 1: Tools - download and installation
OpenSSL Windows Binary: https://slproweb.com/products/Win32OpenSSL.html

MQTT Explorer (portable): http://mqtt-explorer.com/ 

## Step 2: Create the MQTT Client certificate
### Create a working folders
Open the Command Prompt in Windows 10

```
mkdir Raspi_MQTT_Demo
```
```
cd Raspi_MQTT_Demo
```
```
mkdir certs
```
```
cd certs
```
```
mkdir ca
```
```
cd ca
```
### Downlaod the ca files
Download the ca files ```ca.crt``` and ```ca.key``` into the folder ```\Raspi_MQTT_Demo\certs\ca```.


### Create certificates for the MQTT clients using OpenSSL 
Create a working folder:
```
cd ..
```
```
mkdir client
```
```
cd client
```
Generate a client RSA key
```
openssl genrsa -out client.key 2048
```
Now, we create a signing request file from this key.

(Wikipedia https://de.wikipedia.org/wiki/Certificate_Signing_Request)
```
openssl req -out client.csr -key client.key -new
```
**Note:**  The Common Name (CN) needs to match the hostname of your broker!
          For your example we need to use "192.168.0.100".

Output:
```
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [AU]:AT
State or Province Name (full name) [Some-State]:Austria
Locality Name (eg, city) []:Graz
Organization Name (eg, company) [Internet Widgits Pty Ltd]:Campus 02 AT
Organizational Unit Name (eg, section) []:
Common Name (e.g. server FQDN or YOUR name) []:192.168.0.100
Email Address []:

Please enter the following 'extra' attributes
to be sent with your certificate request
A challenge password []:
An optional company name []:
```

Now we can pass the Certificate Signing Request (csr) file to our validation authority:
**Note:** CA key pass phrase = ```1234```
```
openssl x509 -req -in client.csr -CA ../ca/ca.crt -CAkey ../ca/ca.key -CAcreateserial -out client.crt -days 2000
```

# Certificaton - Overview
By now you should have all these files:
```
|-- ca
|   |-- ca.crt
|   |-- ca.key
|   `-- ca.srl
`-- client
    |-- client.crt
    |-- client.csr
    `-- client.key
```

## Step 3: Setup MQTT Explorer
Copy the ```MQTT-Explorer-0.4.0-beta1.exe``` into the ```Raspi_MQTT_Demo``` folder.

***MQTT Connection settings:***

![MQTT_Explorer_Connection_Settings.png](/images/MQTT_Explorer_Connection_Settings.png)

***Advance MQTT Connection settings:***
![MQTT_Explorer_Connection_Settings2.png](/images/MQTT_Explorer_Connection_Settings2.png)

***TLS Certification settings:***
![MQTT_Explorer_Connection_Settings3.png](/images/MQTT_Explorer_Connection_Settings3.png)

***Receiving MQTT messages:***
![MQTT_Explorer_ReceivingCAN_Messages](/images/MQTT_Explorer_ReceivingCAN_Messages.png)



