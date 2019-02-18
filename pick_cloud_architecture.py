import platform
import time
import os

if 'ec2' in platform.node() or 'aws' in platform.platform():
   print('Architecture: AWS')
   time.sleep(5)
   # Run code for cloud resource information generation on AWS

elif 'azure' in platform.platform():
    print('Architecture: Azure')
    time.sleep(5)
    # Run code for cloud resource information generation on Azure
