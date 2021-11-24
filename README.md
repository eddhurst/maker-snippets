# maker-snippets

This project is here to house a small collection of random projects and snippets of code as I learn, develop and play with hardware.

These will vary broadly between the languages that these devices support, but most likely:

- C
- Micropython
- ASM

Projects will be managed in a folder structure to identify the hardware being developed on

---

## Project: Plasma

This project has examples of how to interact with the Plsama2040, a device to control LED strips and RGB LED wires. The Plasma comes with several buttons we can use for extended control as well as an easy to use API for interacting directly with the LEDs.

Hardware:
- [Pimoroni Plasma2040](https://shop.pimoroni.com/products/plasma-2040)
- [5m RGB LED wire](https://shop.pimoroni.com/products/rgb-led-wire)

Requirements:
- [Pimoroni release of Micropython](https://github.com/pimoroni/pimoroni-pico/releases), which comes bundled with their extended libraries for the Plama2040

---

## Installation

Installation steps for specific examples will be covered in project-specific README's, but this will cover most everything I publish here.

For a full guide, you can look through the [Getting Started with the Raspberry Pi Pico](https://learn.pimoroni.com/article/getting-started-with-pico) guide.

In general though it's relatively straight forward:

### Setting up Micropython
- Download the `.u2f` file with Micropython on it from either [RaspberryPi](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html#drag-and-drop-micropython) directly, or if your vendor has extra libraries available they'll bundle the same micropython plus all the libs i.e. [Pimoroni](https://github.com/pimoroni/pimoroni-pico/releases)
- Push the Boot + Reset buttons together on your device. The reset button causes a reset the device power, the boot button forces the device to boot into storage mode. This allows your device to be accessible as if it were an external harddrive.
- Drag + Drop the `.u2f` file into the RPi2040 drive
- It will reboot automatically, and disappear from your drive list. This is normal. It means it worked.

### Setting up your environment

#### Drag and Drop
You can do this in a number of different ways, but the most straight forward way is effectively the similar to above. Press the two buttons to switch into storage mode, then drag your code into the device.

Once you have dropped your code, push the boot button to cycle it back into normal powered mode.

If at least one of your files is called `main.py` then the device will auto-run thjis on boot, and do whatever it is your instructions tell it to do.

#### Thonny

An alternative to the above is to use an IDE such as Thonny. Thonny will allow you to auto-connect your device without all the button faff.

You can download it from the [Thonny website](https://thonny.org/) and once running, make sure to set the interpreter to your device

`Run > Select Interpreter`

Set the first dropdown to `Micropython (Raspberry Pi Pico)` or `Micropython (BBC micro:bit)` depending on where you're running it and you should see the Shell automatically switch at the bottom of your screen.

Plug in your USB and it should automatically connect and allow you to use the Play and Stop tray buttons.
