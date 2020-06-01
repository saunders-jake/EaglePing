# EaglePing

Employer requested a script that 
  - Continuously pinged various ips/domains taken from user input every x amount of seconds
  - Can operate on Windows and Linux operating systems.
  
  
# Dependencies


```
pip install pythonping
```



# TODO
- Add logging capibility (DONE)
- Allow an option to customize a certain amount of time for the script to run instead of relying on user input
- Ping subnets
- Add round to log output

Note: While TCP/UDP packets can be freely created on unprivileged processes, crafting ICMP packets requires root/administrator privilege. Therefore, this program MUST BE ROOT in order to function properly.

Working as of Python 3.8.3
