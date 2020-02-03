# Watchme Sensors

Let's create a simple task to watch sensors (temperatures) on this laptop!
Install and initialize watchme:

```bash
pip install watchme[psutils]
```

I didn't feel like creating an official watcher (with scheduled cron)
so instead I wrote a small script, [monitor_sensors.py](monitor_sensors.py)
to do the work and save to [results.json](results.json). I ran this interactively, 
however you can also do this from the command line.

```bash
python monitor_sensors.py
```

The output data is written to a results file that we can then parse and plot
(will write this after!)

## What if the temperature is too high?

The reason I want to inspect this data is because the computer seems to run a bit
hot. The maximum (warning temperature) is up at 100 degrees C, however it's a warning
sign if the computer at idle is close to 80. If this turns out to be the
case, I can disable turbo, and turn down the max CPU percent usage to 90%:

```bash
echo "1" | sudo tee /sys/devices/system/cpu/intel_pstate/no_turbo
echo "90" | sudo tee /sys/devices/system/cpu/intel_pstate/max_perf_pct
```

I don't want to do this until I have evidence over the day that the computer
is always hot.
