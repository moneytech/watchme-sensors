#!/usr/bin/env python

import os
import json
import numpy as np

from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib

here = os.path.dirname(os.path.abspath(__file__))

# Helper Functions


def plot_arrays(content_arrays, show=False, prefix=None):

    dates = content_arrays["dates"]
    datelist = matplotlib.dates.date2num(dates)

    for key in content_arrays:
        _prefix = None
        if key.startswith("sensors"):
            if prefix != None:
                _prefix = "%s-%s" % (prefix, key)
                _prefix = _prefix.replace(":", "").replace(" ", "")
            values = content_arrays[key]

            # Don't make a plot of all empty values.
            if not any(values):
                continue

            # Can't plot strings, so skip them.
            if any([isinstance(v, str) for v in values]):
                continue

            plt.figure(figsize=(20, 6))
            plt.plot_date(datelist, values, linestyle='solid', marker=',')
            plt.title(key)

            # Does the user want to show the plot?
            if show == True:
                plt.show()

            # Does the user want to save it?
            if _prefix != None:
                save_as = _prefix + ".png"
                print("Saving figure to %s" % save_as)
                plt.savefig(save_as)

            plt.close()


def date_to_npdate(date):
    day, time = date.split()
    return day + "T" + time


def process_arrays(data):
    dates = [x["time"] for x in data]

    ## Use a different formatting for the dates.
    npdates = np.array(list(map(date_to_npdate, dates)), dtype="datetime64").astype(
        datetime
    )

    contents = {}
    contents["sensors_temp_acpitz_current"] = [
        x["sensors_temperatures"]["acpitz"][0]["current"] for x in data
    ]
    contents["sensors_temp_pch_cannonlake"] = [
        x["sensors_temperatures"]["pch_cannonlake"][0]["current"] for x in data
    ]
    contents["sensors_temp_pch_cannonlake"] = [
        x["sensors_temperatures"]["pch_cannonlake"][0]["current"] for x in data
    ]
    contents["sensors_temp_thinkpad"] = [
        x["sensors_temperatures"]["thinkpad"][0]["current"] for x in data
    ]
    contents["sensors_temp_iwlwifi"] = [
        x["sensors_temperatures"]["iwlwifi"][0]["current"] for x in data
    ]

    # Make sure we index by name of core or package
    lookup = []
    for item in data:
        entry = {}
        for core in item["sensors_temperatures"]["coretemp"]:
            entry[core["label"]] = core["current"]
        lookup.append(entry)

    contents["sensors_temp_coretemp_core0"] = [x["Core 0"] for x in lookup]
    contents["sensors_temp_coretemp_core1"] = [x["Core 1"] for x in lookup]
    contents["sensors_temp_coretemp_core2"] = [x["Core 2"] for x in lookup]
    contents["sensors_temp_coretemp_core3"] = [x["Core 3"] for x in lookup]
    contents["sensors_temp_coretemp_core0"] = [x["Package id 0"] for x in lookup]
    contents["sensors_fans"] = [
        x["sensors_fans"]["thinkpad"][0]["current"] for x in data
    ]
    contents["sensors_battery_percent"] = [
        x["sensors_battery"]["percent"] for x in data
    ]
    contents["dates"] = npdates
    return contents


def main():

    # Create an output folder (for GitHub pages)
    image_folder = os.path.join(here, "docs")
    if not os.path.exists(image_folder):
        os.mkdir(image_folder)

    # Generate for results.json
    json_file = "results.json"
    filename, ext = os.path.splitext(os.path.basename(json_file))
    print("file: %s" % json_file)
    with open(os.path.join(here, json_file)) as f:
        data = json.load(f)
    arrays = process_arrays(data)
    plot_arrays(arrays, prefix=os.path.join(image_folder, filename))


if __name__ == "__main__":
    main()
