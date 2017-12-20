---
title: "Noise and distortion"
date: "2017-11-21T21:05:00+01:00"
---

As the audio signal makes its way through the different [realms](<{{% ref "life.md" %}}>) of the system, it travels through various digital, analog, and acoustic components that alter the signal in various ways. Some of these alterations might or might not be audible, or might only be audible under certain conditions. In most scenarios relevant to this blog they are undesirable side effects from limitations in the components that make up the system, though in some specific cases they can be deliberately introduced in pursuit of a specific goal (e.g. [equalization][]).

In order to build a high quality audio system, it is necessary to keep signal degradation (i.e. unwanted alteration) under control, and this requires a good understanding of what these alterations might be, what causes them, and how to avoid or alleviate them. Ever since the invention of the audio signal more than a century ago this has always been a huge topic on which much ink has been spilled, some thoughtful and innovative, some misguided or downright counter-productive. Hopefully this blog will do more of the former and less of the latter — but for now, this post serves as a brief introduction to the issues at hand.

Signal alterations can be divided into three broad categories: *noise*, *linear distortion*, and *non-linear distortion*. {{% footnote note %}}When used by itself without qualification, the term “distortion” can refer to some or all of these categories, depending on context.{{% /footnote %}} Real-world systems exhibit all three kinds in varying amounts. Future posts will dive into these issues in much more detail.

# Noise

*[Noise][]* describes an alteration of the signal in which a separate, *unrelated* signal is added (i.e. mixed in, superposed) to the original signal. {{% footnote note %}}This is the definition I’ll use throughout this blog, pursuant to [IEC 60268–2](https://webstore.iec.ch/publication/1219). In other contexts noise might be used in a more specific way (e.g. broadband noise only), or in a more general way (e.g. signal differences introduced by non-linear distortion are considered to be part of the noise signal).{{% /footnote %}} That additional signal has its own [characteristics](<{{% ref "anatomy.md" %}}>) including amplitude and frequency content (spectrum), which are combined with the characteristics of the original signal. Noise is often quantified by comparing the amplitude of the noise to the amplitude of the signal, a metric known as the *[signal-to-noise ratio][]* (the higher the better).

Noise can appear in all three of the audio realms:

-   In the digital realm it can take the form of [dithering noise][] for example, though modern digital systems provide good enough performance that noise sits comfortably below the threshold of audibility.
-   The analog realm is where noise problems are the most common, the most objectionable, and the most pernicious. They are often the result of complex [electromagnetic interference][] phenomena, subtle hardware defects, or compatibility issues.
-   The acoustic realm is rife with often overlooked sources of noise from ordinary life, from the rumbling of an air conditioning unit to the occasional car driving down the street.

Depending on amplitude and frequency content, noise might or might not constitute a problem in practice. For example, low-level broadband *[colored noise][]* (such as *[white noise][]*) will often go unnoticed because its spectrum is roughly similar to typical ambient noise that we are all continuously subjected to in our daily lives. {{% footnote ref %}}See Albert Donald G., Decato Stephen N., "[Acoustic and seismic ambient noise measurements in urban and rural areas](http://www.sciencedirect.com/science/article/pii/S0003682X16306120)", Applied Acoustics, 119, 135–143, (2017) for examples of ambient noise spectra.{{% /footnote %}} The same cannot be said of narrowband noise concentrated in specific frequencies. {{% footnote note %}}Unfortunately that distinction is lost when noise measurements are condensed into a single number (such as signal-to-noise ratio), discarding spectral distribution in the process.{{% /footnote %}} Furthermore, narrowband noise is more likely to affect the perception of minute detail in the original signal, due to an auditory phenomenon known as *[masking][]*.

{{% figure "plots/noisy-sine-wave" "Noisy sine waveform" %}}
{{% figure "plots/noisy-sine-spectrum" "Noisy sine spectrum" %}}

{{% legend %}}Waveform and spectrum of a sine wave affected by white noise. The noise spectrum, circled in red, is often called the “noise floor”. {{% footnote note %}}From that spectrum plot you might be tempted to conclude that the signal-to-noise ratio is about 50 dB. That would be wrong — it’s actually much worse, around 17 dB. You can’t read it directly from the graph because the noise is spread across multiple frequencies. This is a very common mistake when reading spectrum plots, which I might describe in more detail in a future post.{{% /footnote %}}{{% /legend %}}

In a real-world scenario, noise is only really noticeable when the original signal is relatively quiet, such as when there is a break in a piece of music, because all that remains is the noise itself. Conversely, noise is inaudible when a significantly loud signal is playing, again because of masking (but this time in reverse). In practice, I tend to abide by the following rule of thumb: if you can’t hear anything when playing a silent signal, then your system is probably fine as far as noise is concerned.

# Linear distortion

A system might modify the signal in ways that do not depend on the amplitude of the signal. That is, all else being equal, if the amplitude of the original signal as a whole is changed, the amplitude of the resulting signal as a whole will change by the same amount. This is referred to as a *[linear system][]*.

So far this seems like a somewhat arbitrary distinction, but bear with me for a moment. It so happens that, mathematically, linear systems have a lot of useful properties that makes the concept useful and easy to work with. Specifically, the above means that, when a linear system is excited at a given frequency, it will always amplify (or attenuate) that frequency by the same constant ratio; in other words, it has a well-defined, constant *[frequency response][]*. This means we can quantify the amount of gain that will be applied by the system at any given frequency, and plot that data on a graph, called a *frequency response graph* (or, more technically, a *[Bode plot][]*). Mathematically, the function that is being plotted is called the *[transfer function][]* of the system, and that function is sufficient to completely describe the behavior of a linear system; hence the term *linear distortion* to describe frequency response variations. {{% footnote note %}}One thing that I’ve omitted to keep things simple is that a linear system is not just allowed to apply gain at a particular frequency, it can also apply a constant *time delay* to specific frequencies. This is known as the *[group delay](https://en.wikipedia.org/wiki/Group_delay_and_phase_delay)*. *[Phase response](https://en.wikipedia.org/wiki/Phase_response)* is another way to convey the same information. Technically the term “frequency response” encompasses both *magnitude response* and *phase response*, though the latter is often dismissed for lack of relevance in most audio discussions.{{% /footnote %}}

{{% figure "plots/peak-frequency-response" "Frequency response with 1 kHz 6 dB resonance" %}}

{{% legend %}}The frequency response of a system that amplifies frequencies around 1 kHz by about 6 dB. This particular type of linear distortion is called a [resonance](https://en.wikipedia.org/wiki/Resonance).{{% /legend %}}

How is this useful? Well, [remember](<{{% ref "anatomy.md#the-frequency-domain" %}}>) that the frequency domain is often more useful than the time domain when it comes to understanding how audio signals are perceived. Frequency response tells us how a system alters the frequency components of the signal that flows through it. That makes it one the most powerful tools in the audio engineer’s toolbox.

Studies show that frequency response is extremely important when it comes to assessing audio quality in real-world scenarios. For example it has been shown that the human auditory system is capable of detecting frequency response variations as tiny as 0.1 dB {{% footnote ref %}}Toole, F. and Olive. S., "[The Modification of Timbre by Resonances: Perception and Measurement](http://www.aes.org/e-lib/browse.cfm?elib=5163)", J. Audio Eng. Soc., 36(3), 122–141, (1988). From Fig. 9: coherent sum of 0 dB and -40 dB sources is ~0.1 dB.{{% /footnote %}}, and that it is by far the most important criterion when it comes to assessing the quality of a loudspeaker {{% footnote ref %}}Olive, Sean, “[A Multiple Regression Model For Predicting Loudspeaker Preference Using Objective Measurements: Part 1 — Listening Test Results](http://www.aes.org/e-lib/browse.cfm?elib=12794)”, presented at the 116th AES Convention, Berlin, Germany, preprint 6113, (May 2004).{{% /footnote %}}. Make no mistake: this metric is a *huge deal*, and I expect most posts on this blog will make use of it in one way or another.

The digital and analog realms typically contribute very little in the way of linear distortion. Virtually all of it is found in the acoustic realm, as even the best loudspeakers and headphones struggle to keep their frequency response within a few dB of the intended target {{% footnote ref %}}Many examples can be found in the [SoundStage database](http://www.soundstagenetwork.com/index.php?option=com_content&view=article&id=16&Itemid=18) (loudspeakers) and the [InnerFidelity database](https://www.innerfidelity.com/headphone-measurements) (headphones).{{% /footnote %}}. It gets worse: the acoustics of home listening rooms ([room modes][] especially) can result in low frequency alterations in the order of 10 dB or more! {{% footnote ref %}}Literally any frequency response measurement made in a small room will show this phenomenon. One example can be found in Leduc Michel, 2009, “[How Does Listening Room Acoustics Affect Sound Quality?](http://www.audioholics.com/room-acoustics/listening-room-acoustics#ftn3)“, Audioholics (graph under "Standing waves” section). A series of representative examples can be found in Toole, Floyd E., *[Sound Reproduction: Loudspeakers and Rooms](https://books.google.co.uk/books?id=sGmz0yONYFcC)*, figure 13.9.{{% /footnote %}} No wonder why these are often said to be the “weakest links” of the audio chain…

# Non-linear distortion

This third category includes any kind of signal alteration that is not covered by the other two categories. Specifically, it includes any scenario in which the signal is altered in a way that is contingent on its shape (thus excluding noise) and behaves differently depending on the amplitude of the signal (thus excluding linear distortion). Due to the latter, this is also known as *[amplitude distortion][]*.

This definition makes this a very open-ended category, as indeed a signal can be distorted in an infinite variety of ways. Since it is not possible to run an infinite number of tests, measuring and quantifying the non-linear behavior of a system can be quite challenging. That said, most non-linear distortion comes in well-known shapes and forms, so a few standard measurements are usually good enough to characterize the performance of an audio system.

One important aspect of non-linear distortion is that, contrary to linear distortion, it can cause new frequencies to appear that weren’t present in the original signal. By far the most well-known type of non-linear distortion is *harmonic distortion*, where new frequencies appear that are whole multiples ([harmonics][]) of the frequencies in the original signal. It is often summarized in a single number, *[total harmonic distortion][]* (THD), which indicates the total amplitude of the introduced harmonics relative to the original signal (more precisely, the [fundamental][]). A related phenomenon is *[intermodulation distortion][]*, where multiple frequency components in the signal interact with each other to create new frequencies in a specific pattern.

{{% figure "plots/clipped-sine-wave" "Clipped sine waveform" %}}

{{% figure "plots/clipped-sine-spectrum" "Clipped sine spectrum" %}}

{{% legend %}}Waveform and spectrum of a 1 kHz sine wave showing symptoms of “hard clipping”, which produces odd-order harmonics (circled in red). The THD in this example is about 7%. {{% footnote note %}}Here’s how this number is calculated. First, take the [RMS amplitude](<{{% ref "amplitude.md" %}}>) of the harmonics: 3 kHz -26 dB (0.051) 5 kHz -32 dB (0.025) 7 kHz -46 dB (0.0047) 9kHz -47 dB (0.0043)… the [total RMS amplitude](https://en.wikipedia.org/wiki/Root_mean_square#In_waveform_combinations) of the harmonics is 0.057. The RMS amplitude of the fundamental is 0.78. The THD is the ratio of these two numbers, which is 0.073, or 7.3%.{{% /footnote %}}{{% /legend %}}

Ideally, audio components should be able to accurately track the input signal, such that the output is precisely proportional to the input. Of course that is not the case in practice; consider, for example, that the driver inside a loudspeaker is made from imperfect materials that have imperfect physical properties, so its movement will not perfectly track the signal, instead giving rise to non-linear distortion. One example in the analog realm is [crossover distortion][] that can occur in certain types of amplifiers.

So far I’ve been describing examples of non-linear distortion that can occur during normal system operation. However, the most egregious, obvious, and audible non-linear distortion issues occur when the system is driven beyond its limits; that is, signal amplitude is pushed too far and the system is unable to keep up. When this happens the peaks of the waveform cannot be reproduced faithfully and the system “bottoms out”, a phenomenon known as *[clipping][]*. To mention a few examples, this can happen in the digital realm (which is otherwise immune from most other forms of non-linear distortion) due to overflowing the largest possible sample value; in the analog realm due to exceeding the power limits of an amplifier; or in the acoustic realm due to exceeding the movement limits of a driver ([excursion][]).

So how audible is non-linear distortion? Well, that depends. Because non-linear distortion can take many forms, there is no simple answer. For example, distortion in the lower frequencies is less audible than in higher frequencies, and it is less audible if the newly introduced frequencies are close to the fundamental (thanks, once again, to masking). {{% footnote ref %}}Temme, Steve, "[Application Note: Audio Distortion Measurements](https://www.bksv.com/media/doc/BO0385.pdf)“, Brüel & Kjær, 1992.{{% /footnote %}} Condensing non-linear distortion measurements into a single, simplistic THD number, as is often done, certainly doesn’t help. With that in mind, real-world examples tend to suggest that a THD of 10% is likely to be audible, 1% is borderline, and 0.1% is unlikely to be audible. {{% footnote ref %}}Audioholics, ”[Human Hearing - Distortion Audibility Part 3](http://www.audioholics.com/room-acoustics/human-hearing-distortion-audibility-part-3)", 2005.{{% /footnote %}}

[amplitude distortion]: https://en.wikipedia.org/wiki/Amplitude_distortion

[bode plot]: https://en.wikipedia.org/wiki/Bode_plot

[dithering noise]: https://en.wikipedia.org/wiki/Dither#Digital_audio

[clipping]: https://en.wikipedia.org/wiki/Clipping_(audio)

[colored noise]: https://en.wikipedia.org/wiki/Colors_of_noise

[crossover distortion]: https://en.wikipedia.org/wiki/Crossover_distortion

[equalization]: https://en.wikipedia.org/wiki/Equalization_(audio)

[electromagnetic interference]: https://en.wikipedia.org/wiki/Electromagnetic_interference

[excursion]: https://en.wikipedia.org/wiki/Excursion_(audio)

[intermodulation distortion]: https://en.wikipedia.org/wiki/Intermodulation

[frequency response]: https://en.wikipedia.org/wiki/Frequency_response

[fundamental]: https://en.wikipedia.org/wiki/Fundamental_frequency

[harmonics]: https://en.wikipedia.org/wiki/Harmonic

[linear system]: https://en.wikipedia.org/wiki/Linear_system

[masking]: https://en.wikipedia.org/wiki/Auditory_masking

[noise]: https://en.wikipedia.org/wiki/Noise

[room modes]: https://en.wikipedia.org/wiki/Room_modes

[signal-to-noise ratio]: https://en.wikipedia.org/wiki/Signal-to-noise_ratio

[total harmonic distortion]: https://en.wikipedia.org/wiki/Total_harmonic_distortion

[transfer function]: https://en.wikipedia.org/wiki/Transfer_function

[white noise]: https://en.wikipedia.org/wiki/White_noise
