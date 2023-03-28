REM Print Elliptic Curve Keys in keyfile
REM Input file format: pem
openssl pkey -in %1 -text -noout
pause