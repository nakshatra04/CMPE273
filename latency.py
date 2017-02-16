"""
Question:
Pick one IP from each region, find network latency from via the below code snippet
(ping 3 times), and finally sort regions by the average latency.
http://ec2-reachability.amazonaws.com/
Sample output:
1. us-west-1 [50.18.56.1] - Smallest average latency
2. xx-xxxx-x [xx.xx.xx.xx] - x
3. xx-xxxx-x [xx.xx.xx.xx] - x
...
15. xx-xxxx-x [xx.xx.xx.xx] - Largest average latency
"""
import subprocess,re

class Instances :
    def __init__(self, hostname, ip, avglatency):
        self.hostname = hostname
        self.ip = ip
        self.avglatency = avglatency

"""
hosts = {'us-east-1':'23.23.255.255',
        'us-west-1':'50.18.56.1',
        'eu-west-1':'34.248.60.213',
        'us-west-2':'35.160.63.253',
        'eu-central-1':'35.156.63.252',
        'eu-west-2':'52.56.34.0',
        'us-east-2':'52.14.64.0',
        'us-gov-west-1':'52.222.9.163',
        'ca-central-1':'52.60.50.0',
        'ap-northeast-1':'13.112.63.251',
        'ap-northeast-2':'52.78.63.252',
        'ap-southeast-1':'46.51.216.14',
        'ap-southeast-2':'13.54.63.252',
        'ap-south-1':'35.154.63.252',
        'sa-east-1':'52.67.255.254'}
"""

hosts = [Instances("us-west-1","50.18.56.1", 0),
         Instances("us-east-1", "23.23.255.255", 0),
         Instances("eu-west-1","34.248.60.213", 0),
         Instances("us-west-2","35.160.63.253", 0),
         Instances("eu-central-1","52.28.63.252", 0),
         Instances("eu-west-2","52.56.34.0", 0),
         Instances("us-gov-west-1","52.222.9.163", 0),
         Instances("us-east-2","52.14.64.0", 0),
         Instances("ca-central-1","52.60.50.0", 0),
         Instances("ap-northeast-1","52.68.63.252", 0),
         Instances("ap-northeast-2","52.78.63.252", 0),
         Instances("ap-southeast-1","46.51.216.14", 0),
         Instances("ap-southeast-2","52.64.63.253", 0),
         Instances("ap-south-1","52.66.66.2", 0),
         Instances("sa-east-1","54.94.0.66", 0)]

for host in hosts:
    ping = subprocess.Popen(
    ["ping","-n","3", host.ip],
    stdout = subprocess.PIPE,
    stderr = subprocess.PIPE
                            )
    out, error = ping.communicate()
    """
    output = out.split("Average = ")
    avgoutput = output[1].split("ms")
    host.avglatency = avgoutput[0]"""
    average = int(re.findall(r"Average = (\d+)", out)[0])
    host.avglatency = average


hosts.sort(key=lambda x: x.avglatency, reverse=False)
counter=1
for host in hosts:
    if (counter == 1):
        print str(counter) + ". " + host.hostname + " [" + host.ip + "] -  Smallest Average Latency : " + str(host.avglatency) + " ms"
    if(counter == 15):
         print str(counter) + ". " + host.hostname + " [" + host.ip + "] -  Highest Average Latency : " + str(host.avglatency) + " ms"
    if(counter !=1 and counter !=15):
         print str(counter) + ". " + host.hostname + " [" + host.ip + "] -  Average Latency : " + str(host.avglatency) + " ms"
    counter += 1
