# AWS Example - Tools Installation

## Tools - download and installation
### Open SSL
- Download
  - OpenSSL Windows Binary: https://slproweb.com/products/Win32OpenSSL.html<br>
  - OpenSSL MAC installation guide https://macappstore.org/openssl/<br>
  - OpenSSL Linux installation: ```sudo apt install openssl```<br>
  
- OpenSSL Tutorials:
  - https://www.madboa.com/geek/openssl/
  - https://www.sslshopper.com/article-most-common-openssl-commands.html
  - https://www.golinuxcloud.com/openssl-generate-ecc-certificate/
  - https://gist.github.com/p3t3r67x0/5313b0d7abc25e06c2d78f8b767d4bc3

- OpenSSL Online Tool (CrypTool):
  - https://www.cryptool.org/en/cto/openssl/
  
### Wireshark
- Download  https://www.wireshark.org/download.html<br>

### MQTT Explorer
- Download (portable): http://mqtt-explorer.com/<br>

## Test OpenSSL Installation
```
openssl version
```

```
openssl help
```

```
openssl s_client -connect www.nxp.com:443 -tls1_2
```
