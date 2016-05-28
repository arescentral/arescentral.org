Energizing
==========

:date:      2015-05-04
:author:    sfiera
:tags:      internals

Let’s start with the basics of energy in Ares:

*   The base amount of energy for most cruisers is 1000 energy.
*   All ships have 5× their base energy level in battery.
*   A destroyed ship will release one energy pod per 500 energy it has.
*   A picked-up energy pod will provide 150 energy to its recipient.

Now, when a ship picks up energy, the recipient’s energy meter is first
replenished.  If that fills up, the ship’s battery is next.  If that
fills up too, where does the surplus go?  It turns out that it will go
to the owner’s cash reserves.

Unfortunately, every tick of money is equivalent to 51200 energy, or
about 342 energy pulses, so you’re not likely to benefit from picking
the spillover (it seems that there may have been a unit mismatch;
this is `Ares’s representation of "200.000"`_ and isn't really intended
to mean 51200).

A ship’s battery is also replenished when leaving warp; all of the
energy spent warping flows back into the battery.  In theory, a ship
could burn all of its energy repeatedly entering and leaving warp, which
would resupply almost 4× the ship's base energy as money.  For a
cruiser, that would be 4000 money, or about 1.5% of its purchase cost.

For obvious reasons, this is not recommended.

..  _ares’s representation of "200.000": {filename}/news/the-human-advantage.rst

..  -*- tab-width: 4; fill-column: 72 -*-
