---
title: "Decibels, explained"
date: "2017-11-21T21:03:00+01:00"
---

In the [previous post](<{{% ref "life.md" %}}>), I introduced a number of physical quantities that are used to describe the *[amplitude](<{{% ref "anatomy.md" %}}>)* of an audio signal:

-   In the digital domain, it is a *sample value*;
-   In the analog domain, it is voltage in *volts* (V);
-   In the acoustic domain, it is a pressure difference in *pascals* (Pa).

However, in the audio literature, marketing materials and equipment specifications, these are not the units that are typically used. Instead, one often finds such quantities expressed in *decibels* (dB) or a related unit. There are good reasons for this, and they have to do with how we humans perceive loudness.

# On the usefulness of ratios

In audio, we care more about *ratios* of quantities (e.g. "×2") than absolute values (e.g. "3 V"). To understand why, here’s an example:

-   The difference in loudness between 0.1 Pa and 0.2 Pa is very noticeable.
-   The difference in loudness between 1.0 Pa and 1.1 Pa is barely noticeable.

In both cases the absolute difference is the same: 0.1 Pa. However, the ratio is very different; in the former case it’s ×2, in the latter case it’s ×1.1. This makes a compelling case for using ratios, not differences, when comparing amplitudes.

There is another advantage to using ratios. Remember that all three quantities (sample value, voltage, and sound pressure) are *proportional* to each other when the audio signal moves from one realm to the next. {{% footnote note %}}Assuming ideal conditions, i.e. no [noise or distortion](<{{% ref "distortion.md" %}}>).{{% /footnote %}} This means that a given ratio applies in all three domains: twice the sample value is also twice the voltage and twice the sound pressure. This is very convenient because it means that a given ratio (often called [gain][]) has the same meaning regardless of context.

Now, if only there was a unit that made working with ratios easier…

# Enter the decibel

The *decibel* (dB) is, in its purest form, a *[dimensionless unit][]* that represents a ratio between two quantities, just like “×” or “%”. What sets the decibel apart is that it is also a *[logarithmic unit][]*, meaning that its value is proportional to the *[logarithm][]* of the ratio, not the ratio itself. This will be clearer with examples:

| Amplitude ratio | Decibel equivalent |
| --------------- | ------------------ |
| ×0.01           | -40 dB             |
| ×0.1            | -20 dB             |
| ×0.5            | -6 dB              |
| ×1              | 0 dB               |
| ×2              | +6 dB              |
| ×4              | +12 dB             |
| ×8              | +18 dB             |
| ×10             | +20 dB             |
| ×100            | +40 dB             |

Because the decibel is a logarithmic unit, it behaves differently from more conventional linear units. The trick is to not fight their logarithmic nature, but embrace it. Here’s how:

-   The most useful ratios to keep in mind are +6 dB (×2) and +20 dB (×10).
-   To invert the ratio, just change the sign: for example, -6 dB is the same as dividing by 2.
-   When combining ratios, decibels don’t multiply; they add up. For example, ×4 (2×2) is 12 dB (6+6), not 36. This might seem strange, but this property makes decibels very convenient to use in practice — it’s easier to add than to multiply.
-   0 dB means ×1, i.e. no change in amplitude.
-   ×0 is -∞ dB (negative infinity). You might have seen this as the “mute” position on some volume knobs.
-   For less trivial cases, [online calculators][dbcalc] are available.

{{% caution %}}All of the above assumes decibels are used to express ratios of [field quantities](https://en.wikipedia.org/wiki/Field,_power,_and_root-power_quantities). Digital sample value, voltage, and sound pressure are examples of field quantities. When dealing with *power* quantities (i.e. watts), however, there is a catch: in that case, +6 dB is ×4, not ×2, which is +3 dB. This might seem strange and confusing, but once again there is an explanation: in practice power is proportional to the *square* of the field quantity. So, for example, when voltage is doubled, power quadruples. Or, said differently, if voltage is increased by 6 dB, then power increases by… 6 dB — which is why the rules makes sense.{{% /caution %}}

# Using decibels for absolute values

In theory, one could stick with linear units when dealing with absolute values (e.g. 2 V), and use decibels when dealing with ratios (e.g. ×2). However, when a calculation involves both, the mental gymnastics can be challenging. {{% footnote note %}}Not convinced? Try calculating 2 V × -11 dB by hand.{{% /footnote %}}

It would make more sense to use decibels for everything, including absolute quantities. Fortunately, that’s easy: we just need to agree on a reference, and then express in decibels the ratio between that reference and the quantity we wish to convey. The resulting decibel value is called *[level][]*. For example, if the reference is 1 V, then the level of 2 V is +6 dB. {{% footnote note %}}And the calculation from the previous note becomes 6 dB - 11 dB = -5 dB. Much easier!{{% /footnote %}}

In practice, the reference value is indicated by a suffix affixed to the unit. Here are some references commonly used in the three audio realms:

| Quantity       | Reference  | Equivalent level                                                                                                                                                                                                                                                                                                                                                                                       |
| -------------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Sound pressure | 20 µPa     | 0 [dB SPL][]                                                                                                                                                                                                                                                                                                                                                                                           |
| Voltage        | 1 V        | 0 [dBV][]                                                                                                                                                                                                                                                                                                                                                                                              |
| Voltage        | ~0.77 V    | 0 [dBu][] {{% footnote note %}}Yes, there are two different references in common use for voltages. That’s sad, but that’s the way it is. To convert from one to the other, add or subtract ~2.2 dB.{{% /footnote %}}                                                                                                                                                                                   |
| Sample value   | Full scale | 0 [dBFS][] {{% footnote note %}}In other words, 0 dBFS is the maximum level before digital clipping (truncation) occurs. Thus valid amplitudes have negative dBFS values. Or at least that’s how it’s supposed to work. The definition of dBFS can be quite fuzzy and ambiguous, as [explained](https://en.wikipedia.org/wiki/DBFS#RMS_levels) in that Wikipedia page. Caveat emptor.{{% /footnote %}} |

Sometimes the suffix is omitted and has to be inferred from the context. For example, it is fairly common to find “dB SPL” written as simply “dB”, especially in mainstream publications. This is best avoided as it can lead to confusion between ratios and levels. Conversely, “dBr” ("relative") is sometimes used to make it explicit that decibels are used to express a ratio, not a level.

Additional suffixes and variants are often used to convey additional information. The most common examples include “peak” or “RMS”, which denote [different ways](<{{% ref "amplitude.md" %}}>) of looking at the amplitude of the signal, and “dBA”, which indicates the use of [A-weighting][]. More on these in later posts.

[a-weighting]: https://en.wikipedia.org/wiki/A-weighting

[dbcalc]: http://www.sengpielaudio.com/calculator-db.htm

[dbfs]: https://en.wikipedia.org/wiki/DBFS

[db spl]: https://en.wikipedia.org/wiki/Sound_pressure#Sound_pressure_level

[dbv]: https://en.wikipedia.org/wiki/Decibel#Voltage

[dbu]: https://en.wikipedia.org/wiki/Decibel#Voltage

[dimensionless unit]: https://en.wikipedia.org/wiki/Dimensionless_quantity

[gain]: https://en.wikipedia.org/wiki/Gain_%28electronics%29

[level]: https://en.wikipedia.org/wiki/Level_%28logarithmic_quantity%29

[logarithm]: https://en.wikipedia.org/wiki/Logarithm

[logarithmic unit]: https://en.wikipedia.org/wiki/Logarithmic_scale
