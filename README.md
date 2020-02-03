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
