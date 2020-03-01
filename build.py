#!/bin/env python
import os
import json

with open('config.json', 'r') as f:
    config = json.load(f)
    version = config['version']
    git_rev = config['git_tag']
    distro = config['distribution']
    path = os.path.realpath(__file__) 
    print('poller ' + version + ' using git rev ' + git_rev + ' on ' + distro)
    print('working dir : ' + path)

    for proj in config['build']:
        print(proj)
