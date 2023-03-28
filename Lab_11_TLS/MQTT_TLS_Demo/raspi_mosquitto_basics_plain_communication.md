# Install mosquitto brocker on Raspberry Pi

```
sudo apt-get update
```

```
sudo apt-get upgrade
```

```
sudo apt-get install mosquitto mosquitto-clients 
```
# Test plain communication
Create a mosquitto config file ``` mosquitto_plain.config``` with the following content:
```
listener 1883
allow_anonymous true
```

Create a shell script ```mosquitto_start_plain_service.sh``` with the following content:
```
#!/bin/bash
mosquitto -c mosquitto_plain.config
```

Allowing everyone to execute the script, enter:
```
chmod +x mosquitto_start_plain_service.sh
```

Start the mosquitto broker:

```
.\mosquitto_start_plain_service.sh
```
# Usefull Mosquitto commands:
```
sudo service mosquitto status
```

```
sudo service mosquitto stop
```

```
mosquitto_sub -t "TestTopic"
```

```
mosquitto_pub -t "TestTopic" -m "Hello Word"
```


# Install Python paho-mqtto
```
sudo apt-get install python-pip 
```
```
sudo pip3 install paho-mqtt
```