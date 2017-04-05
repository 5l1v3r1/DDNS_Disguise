# DDNS Disguise
Change your No-IP's DDNS IPv4 Settings to any IP Address in a matter of seconds.

## Description
DDNS Disguise is a tool that allows you to redirect your No-IP DDNS to any IPv4 Address of your choice. This lets you instantly change your DDNS redirection settings in a matter of seconds, without the need of constantly dealing with the web version which is slow and time-consuming.
For pentesters, DDNS Disguise can often be used as a protection against reverse engineering. As you set your LHOST to host.ddns.net in your payload, your IP Address is "hidden" behind your DDNS. With a simple PING to your Hostname, your IP Address is exposed and you can easily be tracked down.

DDNS Disguise is compatible with Python 2.x.

## Preview
![Preview](http://i.imgur.com/nkgg5ao.png)

## Installation
```git clone https://github.com/0xCoto/DDNS_Disguise```

### Usage

```
cd DDNS_Disguise
python DDNS_Disguise.py
```

## Credits
DDNS Disguise was created by [@0xCoto](https://github.com/0xCoto).
