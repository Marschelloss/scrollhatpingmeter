# Scroll(P)HatPingMeter

Small utility to use Pimoroni's [Scroll HAT](https://shop.pimoroni.com/products/scroll-hat-mini?variant=31552633503827) or [Scroll pHAT](https://shop.pimoroni.com/products/scroll-phat-hd?variant=2380803768330) as a ping meter.

## Usage

Install required python libraries:

```bash
pip3 install -r requirements.txt
```

Make the script executeable:

```bash
chmod +x ./scrollhatpingmeter.py
```

Execute the script:

```bash
./scrollhatpingmeter.py
```

## Configuration

Some options can be set via additional flags:

```bash
./scrollhatpingmeter.py --help
usage: scrollhatpingmeter.py [-h] [--disabledisplay] [-H HOST] [-t TIMER] [-b BRIGHTNESS] [-v] [--version]

optional arguments:
  -h, --help            show this help message and exit
  --disabledisplay      Add flag to disable display output
  -H HOST, --host HOST  Host to ping. Default: 8.8.8.8
  -t TIMER, --timer TIMER
                        Time in seconds between pings. Default: 10
  -b BRIGHTNESS, --brightness BRIGHTNESS
                        Sets brightness of display. Use range between 1 and 10. Default: 10
  -v, --verbose         Verbosity (-v, -vv, etc)
  --version             show program's version number and exit
```
