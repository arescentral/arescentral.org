The Human Advantage
===================

:date:      2013-03-08
:author:    sfiera
:tags:      internals

Think back for a moment to 1999.  If you played Ares online, you might
remember that in version 1.1.1, when your selected race was Human, your
advantage was "1.40".  After Hera came out, it became "1.398".  What
happened?

Part of the answer is that 1.398 was a more accurate way of writing it
all along.  Usually, when Ares works with fractions it uses something
called "`fixed-point arithmetic`_" with an exponent of -8.  What that
means is that numbers are treated as being 2⁻⁸, or 1/256, of what they
actually are [#scale]_.

If you looked at the raw data in the "Ares Scenarios" file, the number
you'd find is "358"; (358/256) is 1.3984375.  We'd like to represent 1.4
more accurantely, but we can't.  The smallest amount we could add is
(1/256), and that would give us 1.40234375, which is further away
(∆=0.0023 instead of 0.0016).  So, (358/256) is the best we can do.

We only need to write three digits after the decimal point---that's
enough to represent 999 different values between 0.000 and 1.000, and we
only need to represent 255 different values between (0/256) and
(256/256).

But, what should we do with those other values?

1.398 is a the most accurate way to write (358/256), but 1.4 is a
nicer way.  Suppose we came at this from a different direction: instead
of writing the value that most accurately represents (358/256), we write
a value that (358/256) most accurately represents.  Well, as we saw
above, 1.3984375 is the value closest to 1.4.  If we write 1.4, then we
must mean (358/256), even if it's not the most accurate way to write it.

After I realized that, I went through all the numbers from 0.000 to
1.000 yesterday [#cpu]_ and figured out where we could use shorter
numbers.  That resulted in a table of 256 different values, one for each
fraction.  Now, whenever it's sufficiently accurate, Antares will print
just one or two digits after the decimal point.

So now, when Antares finally has multiplayer, the Human advantage will
be 1.4 again [#floor]_.

This is the first in what will hopefully be a decent series of posts on
Antares's internals.  There's more to say about fixed-point arithmetic,
but this is enough for now.  Join us next time, when we talk about…
evil.

..  rubric:: Footnotes

..  [#scale] A similar case is zooming, where 4096 (that's 2¹²) is
    treated as 1:1 scale.  So, scaling is done in fixed-point arithmetic
    with an exponent of -12.

..  [#cpu] Fine, *I* didn't go through them.  I had a computer program
    go through them for me.

..  [#floor] Unfortunately, it looks like a lot of the Ares data rounded
    down instead of than rounding to the nearest value.  For example,
    many ships have thrust (25/256), and Antares will still write that
    as 0.098.  0.1 is (25.6/256), so we write that for (26/256),
    because that's what you get from rounding-to-nearest instead of
    rounding down.

..  _fixed-point arithmetic: https://en.wikipedia.org/wiki/Fixed-point_arithmetic

..  -*- tab-width: 4; fill-column: 72 -*-
