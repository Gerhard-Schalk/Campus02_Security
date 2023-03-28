REM Input file format: pem
openssl x509 -in %1 -outform der -out %1.der