# Welcome to Smart-Home project
<div style="display: flex; gap: 10px; align-items: center;">
<img src="../_resources/Connected-Together-and-Work-Rear-Transparent.png" width="450"/>

<img src="../_resources/RPi-Wired-to-house-2.png" width="450"/>
</div>
## 🏡 Project Overview

This is a school project where we modified a dollhouse from the Sylvanian Families series to enable connectivity with a Raspberry Pi.

Using a photoresistor from the Sunfounder Da Vinci Kit for Raspberry Pi, we implemented a smart lighting system. A Python program controls the dollhouse's internal lighting based on the brightness levels detected by the photoresistor installed inside.

This project is detailed further in my Medium article:
[Building a Smart Dollhouse with My First-Grader: A Journey into DIY Tech.](https://medium.com/@max.v.zaikin/building-a-smart-dollhouse-with-my-first-grader-a-journey-into-diy-tech-a7a0ac40fe4a)

## 🔍 Key Features

1. **Understanding Analog-to-Digital Conversion with ADC0834:**
    ❤️ The heart of our project is the ADC0834, an 8-bit microelectronic component that converts analog inputs into digital values ranging from 0 to 255.  
      - It doesn't interpret data but translates it into numbers for our Raspberry Pi program to process.
      - It supports up to 4 simultaneous connections and can operate in two modes:
           - Single-ended mode: Converts analog inputs to values between 0 and 255.
           - Differential mode: Outputs the difference between inputs.

    🔗 We encourage you to reed following documentation Resources:
      - [Texas Instruments ADC0834-N](https://www.ti.com/product/ADC0834-N)
      - [SPI Protocol Overview](https://en.wikipedia.org/wiki/Serial_Peripheral_Interface)

    🚀 The ADC0834 communicates via the SPI protocol, which defines how to activate, communicate with, and receive data from devices.
        Our Raspberry Pi interaction with the ADC0834 is handled in the module: [adc0834.py.](https://github.com/maxzaikin/Raspberry-PI/blob/main/Smart-Home/src/core/adc0834.py)
        For detailed insights, refer to the *"Figure 21. ADC0838-N Timing" diagram"* on page 11 of the official [ADC0834-N](https://www.ti.com/product/ADC0834-N) documentation.

2. **Custom Application Architecture for Extendability**:

    Unlike the Sunfounder-provided software, our project emphasizes scalability.

    We aimed to design a modular system where adding new components in the future wouldn’t require altering the core application logic.

    This approach focuses development efforts on the new modules rather than the existing foundation.

```
    📁 Project Structure:
    Smart-Home/
    ├── main.py
    ├── src/
    │   ├── core/
    │   │   ├── adc0834.py
    │   │   ├── device.py
    │   │   ├── light.py
    │   │   ├── smart_home.py
    └──────── __init__.py
```

🌟 Project Description (English Version) 🌟
🏡 Project Overview

This is a school project where we modified a dollhouse from the Sylvanian Families series to enable connectivity with a Raspberry Pi.

Using a photoresistor from the Sunfounder Da Vinci Kit for Raspberry Pi, we implemented a smart lighting system. A Python program controls the dollhouse's internal lighting based on the brightness levels detected by the photoresistor installed inside.

This project is detailed further in my Medium article:
Building a Smart Dollhouse with My First-Grader: A Journey into DIY Tech.
🔍 Key Features

    Understanding Analog-to-Digital Conversion with ADC0834
    The heart of our project is the ADC0834, an 8-bit microelectronic component that converts analog inputs into digital values ranging from 0 to 255.
        It doesn't interpret data but translates it into numbers for our Raspberry Pi program to process.
        Supports up to 4 simultaneous connections and can operate in two modes:
            Single-ended mode: Converts analog inputs to values between 0 and 255.
            Differential mode: Outputs the difference between inputs.

    🔗 Documentation Resources:
        Texas Instruments ADC0834-N
        SPI Protocol Overview

    The ADC0834 communicates via the SPI protocol, which defines how to activate, communicate with, and receive data from devices.
        Our Raspberry Pi interaction with the ADC0834 is handled in the module:
        adc0834.py.
        For detailed insights, refer to the "Figure 21. ADC0838-N Timing" diagram on page 11 of the official ADC0834-N documentation.

    Custom Application Architecture for Extendability
    Unlike the Sunfounder-provided software, our project emphasizes scalability.
        We aimed to design a modular system where adding new components in the future wouldn’t require altering the core application logic.
        This approach focuses development efforts on the new modules rather than the existing foundation.

    📁 Project Structure:

    Smart-Home/
    ├── main.py
    ├── src/
    │   ├── core/
    │   │   ├── adc0834.py
    │   │   ├── device.py
    │   │   ├── light.py
    │   │   ├── smart_home.py
    └──────── __init__.py

    View Project Structure on GitHub

🤝 Call to Action 🛠️

We understand that this project and its structure are works in progress and may contain inaccuracies. We invite you to join us in improving and expanding this initiative.