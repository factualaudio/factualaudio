---
title: "Life of an audio signal"
date: "2017-11-21T21:02:00+01:00"
---

In the [previous post](<{{% ref "anatomy.md" %}}>), I described how an audio signal is represented. Now, let’s discuss the various physical forms that audio signals take as they travel through each stage of an audio playback system.

For the sake of this discussion, I am going to assume the most common and straightforward use case: playing a *digital stream* over loudspeakers (or headphones). By “digital stream” I mean any audio signal that is processed by a computer or computer-like system; that can be anything including a MP3 file, online video, online music streaming, the soundtrack of a Blu-ray disc, etc. This does not include analogue media such as vinyl discs or cassette tapes.

Before this digital content can reach your eardrums, it has to go through a series of steps. Between these steps, the audio signal is materialized in different ways depending on which part of the audio “pipeline” we are looking at. In this post I refer to these concrete representations as *realms* {{% footnote note %}}“realm” is not a widely used term — the term “domain” is normally used. However, I felt that this could create confusion with *time domain* and *frequency domain*, which are completely unrelated concepts.{{% /footnote %}}. I am going to start at the source and then make my way through to the listener.

To keep things clear and simple, the example signal I’ll use throughout this post is a monophonic (one channel) 1 kHz sine wave. For all intents of purposes, each additional channel can be assumed to act like a completely separate audio signal that takes a similar path through the system.

{{% figure "diagrams/realms" %}}

# The digital realm

It all starts within the digital device, which can be any computer or computer-like gadget (PC, smartphone, Bluetooth receiver, etc.). Most devices read or receive audio data in *digitally compressed* form. Popular digital compression algorithms include [MP3][], [AAC][] and [FLAC][].

[Digital compression][] {{% footnote note %}}Not to be confused with *[dynamic range compression](https://en.wikipedia.org/wiki/Dynamic_range_compression)*, which is completely unrelated.{{% /footnote %}} is a complicated subject, which I won’t dig into further in this post. In any case, the data first goes through a *decoder* which converts the compressed signal into uncompressed form, which looks like this:

{{% figure "plots/1khz-sine-wave-digital" %}}

This plot shows that, in the digital realm, audio is not represented by a continuous, smoothly changing signal — instead, all we have are regularly-spaced “snapshots” that indicate what the signal amplitude is at some point in time. This is called a *[discrete signal][]*, and the “snapshots” are called *samples*. In this example, we have 44100 samples every second, or more formally, the *sample rate* is 44.1 kHz. Such a sample rate is standard for music — other types of content, such as movies or games, use a slightly higher rate, 48 kHz, for mostly historical reasons.

Because memory is not infinite, each sample value has a finite precision. In practice, each sample is typically converted to a signed integer with a precision, or *[bit depth][]*, of 16 bits. This process is called *[quantization][]*. A 16-bit signed integer can take a value from -32768 to +32767. Samples outside of this range cannot be represented, and will be clamped to the nearest possible value; this is called *digital [clipping][]*, and is best avoided as it sounds quite bad. A signal that peaks at the highest possible amplitude without clipping is called a *full-range* or *full-scale* signal{{% footnote ref %}}[IEC 61606–1:2009](https://webstore.iec.ch/publication/5664), *Digital audio parts — Basic measurement methods of audio characteristics — General*, §3.1.10{{% /footnote %}}.

Finally, the signal is physically represented simply by transmitting the value of each point, or *sample*, one after the other. For example, the above signal is transmitted as 4653, 9211, 13583, etc. in the form of binary numbers. This way of transmitting the signal is called *[pulse-code modulation][]*.

This section just skirted the surface of how digital audio works. The details of how sampled signals behave in practice are often counter-intuitive; as a result, misrepresentation of digital audio phenomena is quite commonplace in the audiophile community, leading to confusion and misguided advice. Digital audio expert [Chris Montgomery][] produced a [series of videos][xiphvideo] that explains these complex phenomena with very clear and straightforward examples — it is a highly recommended resource if you wish to learn more about the digital realm.

# The analog realm

Loudspeakers and headphones cannot receive a digital signal; it has to be converted to an *analog* signal first. This conversion is done in an electronic circuit appropriately named the *[digital-to-analog converter][]*, or DAC. This is where computer engineering ends and electrical engineering begins. The main task of the DAC is to take each sample value and convert it to some electrical *[voltage][]* on its output pins. The resulting signal looks like the following:

{{% figure "plots/1khz-sine-wave-analog" %}}

It is important to realize that in the plot above, the unit used for the vertical scale is the *[volt][]*. In other words, the amplitude of the audio signal in the analog domain is defined by its *voltage*. It is *not* defined by [current][] nor [power][]. Even when the signal is used as the input of a loudspeaker, it is still voltage that determines the sound that comes out; power dissipation is a *consequence*, not a *cause*, of the audio signal flowing through the loudspeaker. As Pat Brown [elegantly puts it][patbrown]: "power is *drawn*, not applied". {{% footnote note %}}Another way to state this is to say that properly engineered analog audio devices act as *[voltage sources](https://en.wikipedia.org/wiki/Voltage_source)* (or sinks), which are connected to each other by way of *[impedance bridging](https://en.wikipedia.org/wiki/Impedance_bridging)*.{{% /footnote %}} This is a frequent source of confusion.

The DAC took our discrete signal and converted it into a continuous electrical signal, whose voltage is (hopefully) *proportional* to the digital sample value. The central (mean) value of the signal, called the *[DC offset][]*, is zero volts; the signal swings around that central value, *[alternating][]* between positive and negative voltage. In this example, our full-scale digital stream was converted to an analog signal that swings between -1.41 V and +1.41 V. Depending on the specific model of DAC used, its volume control setting (if any) and the signals involved, these numbers can vary — typical peak amplitude can go as low as 0.5 V {{% footnote ref %}}Wikipedia, *[Nominal levels](https://en.wikipedia.org/wiki/Line_level#Nominal_levels)*, peak amplitude for consumer audio{{% /footnote %}} or as high as 2.8 V {{% footnote ref %}}[IEC 61938:2013](https://webstore.iec.ch/publication/6142), *Guide to the recommended characteristics of analogue interfaces to achieve interoperability*, §8.2.1{{% /footnote %}}.

The amount of *current* or *power* transferred from the source of an analog signal (e.g. a DAC) to the equipment plugged in at the other end of the cable (the *[load][]*, e.g. a loudspeaker) is determined by the *[impedance][]* of the load, also known as the *[input impedance][]*. According to [Ohm’s law][], the lower the impedance, the more current, and therefore power, will be required to sustain a given voltage.

DACs, as well as most other types of analog audio equipment (such as filters or mixers), are not designed to provide significant amounts of power. Instead, they are meant to be connected to a high-impedance load, normally 20 kΩ or higher {{% footnote ref %}}[IEC 61938:2013](https://webstore.iec.ch/publication/6142), *Guide to the recommended characteristics of analogue interfaces to achieve interoperability*, §8.2.1{{% /footnote %}}. This means that the load is acting much like a [voltmeter][] or oscilloscope — it is “peeking” at the input voltage without drawing significant power from it. Such a signal that carries some voltage but very little power is called a *[line-level][]* signal.

On the other hand, loudspeakers (and headphones to a lesser extent) are low-impedance devices — often between 4 Ω and 8 Ω in the case of speakers. This is because they operate under a relatively low voltage, but require a lot of power. For example, most speakers will happily produce comfortably loud sound with as little as 5 V, but might consume as much as 6 [watts][] while doing so {{% footnote note %}}From the numbers given a keen eye will [deduce](http://www.sengpielaudio.com/calculator-ohm.htm) that this example speaker has an impedance of 4 Ω. One thing to note is that loudspeaker impedance is highly dependent on the frequency of the signal, making the use of one number an oversimplification. The impedance that manufacturers advertise, called the *rated impedance*, is 1.25 times the *minimum* impedance of the speaker across its rated frequency range. (see [IEC 60268–5:2003](https://webstore.iec.ch/publication/1223), *Loudspeakers*, §16.1){{% /footnote %}}. Line-level equipment is not designed to provide such a large amount of power.

This problem is solved by using a *[power amplifier][]*. This is a component that conveniently provides a high-impedance input for connecting line-level equipment, while exposing an output that is capable of providing large amounts of power, such as 10W or more, to a low-impedance load. {{% footnote note %}}In practice, most amplifiers are also capable of increasing the voltage (amplitude) of the signal; this is called the [gain](https://en.wikipedia.org/wiki/Gain_%28electronics%29) of the amplifier. This is because most loudspeakers require voltages that are somewhat higher than line level in order to play loud enough. Still, the primary goal of a power amplifier is to provide power, not to increase voltage.{{% /footnote %}} Such outputs provide so-called *speaker-level signals*.

In some home audio systems, the DAC and the amplifier are integrated into one single device, which is called an *integrated amplifier* or more commonly an *[AV receiver][]* (AVR).

# The acoustic realm

Finally, in order to reach your ears, the analog signal must be converted to an *acoustic* signal, that is, actual [sound waves][]. This is accomplished using a device called an *electroacoustic [transducer][]*, or *driver*. The output of a driver when excited with our example signal, as measured at some point in front of it, might look like the following:

{{% figure "plots/1khz-sine-wave-acoustic" %}}

Note the change of vertical scale. We’re not dealing with voltage anymore — amplitude takes the form of *[sound pressure][]* instead. Indeed, sound is a physical phenomenon in which transient changes in pressure (*compression*, *rarefaction*) produced by the vibration of a *sound source* propagate through the space around it. In other words, it is a *[longitudinal wave][]*. Sound pressure, expressed in *[Pascals][]* (Pa), quantifies the difference between normal atmospheric pressure and some local, dynamic change in pressure, at a given point in time and space. The human ear is equipped to detect these changes, which are then — finally! — perceived as sound by the human brain.

An ideal transducer will produce sound pressure *proportional* to the voltage applied to it, like in the above waveform. However, it is difficult to design a driver that is capable of doing that across the entire range of audible frequencies. Consequently, a number of transducer types are available, which are commonly referred to as *[subwoofers][]*, *[woofers][]*, *[midranges][]* and *[tweeters][]*.

In order to reproduce the entire range of human hearing, several of these drivers — often two or three — are assembled inside a single “box”, called the *enclosure*. In most designs the drivers are mounted flush with one side of the box, which is called the *front baffle*. An electrical circuit called a *[crossover][]* splits the input signal into the frequency ranges appropriate for each driver. The resulting device is called a *[loudspeaker][]*.

What I’ve described here is called a *passive* loudspeaker, which is the most common type in consumer “Hi-Fi” systems. Sometimes the amplifier and speaker are integrated into the same device; this is called an *active* or *[powered][]* speaker. Examples include professional “studio monitor” speakers, which have line-level inputs. Other products, such as “Bluetooth speakers”, go one step further and throw in a DAC as well for a completely integrated solution.

*[Headphones][]* are a special case and typically only have one driver per channel, which makes them simpler. Conceptually, a headphone is akin to a miniature loudspeaker. Because of their proximity to the ear, they don’t have to produce as much sound pressure; therefore they require much less power to operate (often less than 1 mW).

One notable aspect of the acoustic realm is that sound propagates in all three dimensions — the audio signal (sound pressure) is not the same at every point in space. In particular, speakers exhibit *radiation patterns* that vary with angle and frequency, and the sound they emit can bounce off surfaces (*[reflection][]*). This in turn means that they interact with their environment (the listening room, or, in the case of headphones, the listener’s head) in ways that are complex and difficult to predict but nonetheless have an enormous impact on how the radiated sound will be perceived by a human listener. This makes choosing and configuring a speaker system quite the challenge. Hopefully, future posts on this blog will provide some pointers.

[aac]: https://en.wikipedia.org/wiki/Advanced_Audio_Coding

[alternating]: https://en.wikipedia.org/wiki/Alternating_current

[av receiver]: https://en.wikipedia.org/wiki/AV_receiver

[bit depth]: https://en.wikipedia.org/wiki/Audio_bit_depth

[crossover]: https://en.wikipedia.org/wiki/Audio_crossover

[current]: https://en.wikipedia.org/wiki/Electric_current

[flac]: https://en.wikipedia.org/wiki/FLAC

[headphones]: https://en.wikipedia.org/wiki/Headphones

[mp3]: https://en.wikipedia.org/wiki/MP3

[chris montgomery]: https://en.wikipedia.org/wiki/Chris_Montgomery

[clipping]: https://en.wikipedia.org/wiki/Clipping_%28signal_processing%29

[dc offset]: https://en.wikipedia.org/wiki/DC_bias

[digital-to-analog converter]: https://en.wikipedia.org/wiki/Digital-to-analog_converter

[digital compression]: https://en.wikipedia.org/wiki/Data_compression

[discrete signal]: https://en.wikipedia.org/wiki/Discrete-time_signal

[impedance]: https://en.wikipedia.org/wiki/Electrical_impedance

[input impedance]: https://en.wikipedia.org/wiki/Input_impedance

[line-level]: https://en.wikipedia.org/wiki/Line_level

[load]: https://en.wikipedia.org/wiki/Electrical_load

[longitudinal wave]: https://en.wikipedia.org/wiki/Longitudinal_wave

[loudspeaker]: https://en.wikipedia.org/wiki/Loudspeaker

[midranges]: https://en.wikipedia.org/wiki/Mid-range_speaker

[ohm’s law]: https://en.wikipedia.org/wiki/Ohm's_law

[pascals]: https://en.wikipedia.org/wiki/Pascal_%28unit%29

[patbrown]: http://www.prosoundtraining.com/site/author/pat-brown/meaningful-metrics-the-use-and-abuse-of-loudspeaker-power-ratings/

[power]: https://en.wikipedia.org/wiki/Electric_power

[powered]: https://en.wikipedia.org/wiki/Powered_speakers

[power amplifier]: https://en.wikipedia.org/wiki/Audio_power_amplifier

[pulse-code modulation]: https://en.wikipedia.org/wiki/Pulse-code_modulation

[quantization]: https://en.wikipedia.org/wiki/Quantization_%28signal_processing%29

[reflection]: https://en.wikipedia.org/wiki/Reflection_%28physics%29#Sound_reflection

[sound pressure]: https://en.wikipedia.org/wiki/Sound_pressure

[sound waves]: https://en.wikipedia.org/wiki/Sound

[subwoofers]: https://en.wikipedia.org/wiki/Subwoofer

[transducer]: https://en.wikipedia.org/wiki/Transducer

[tweeters]: https://en.wikipedia.org/wiki/Tweeter

[volt]: https://en.wikipedia.org/wiki/Volt

[voltmeter]: https://en.wikipedia.org/wiki/Voltmeter

[voltage]: https://en.wikipedia.org/wiki/Voltage

[watts]: https://en.wikipedia.org/wiki/Watt

[woofers]: https://en.wikipedia.org/wiki/Woofer

[xiphvideo]: https://xiph.org/video/
