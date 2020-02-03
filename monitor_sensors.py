#!/usr/bin/env python3

from watchme.watchers.psutils.tasks import sensors_task
from datetime import datetime
import time
import json

# Seconds delay between runs
seconds = 60    # interval of seconds to check at
total_time = 0  # total accumulated time
max_time = 1440 # when to stop (1440 == one day)
results = []

def save_json(json_obj, filename):
    with open(filename, 'w') as filey:
        filey.writelines(json.dumps(json_obj, indent=4))

while total_time <= total_time: # one day is 1440 seconds
    print("Running %s complete." %(total_time/max_time))
    result = sensors_task()
    result['time'] = str(datetime.now())
    results.append(result)
    # Save intermediate to file
    save_json(results, 'results.json')
    time.sleep(seconds)
    total_time += seconds
