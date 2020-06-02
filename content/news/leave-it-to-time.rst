Leave it to Time
================

:date:      2020-06-02
:author:    sfiera
:tags:      internals

It’s been a long time, so let’s talk about time.

..  image:: /news/img/ticks-7200.png
    :alt: Hera with Time condition “IF game tick time ≥ 7200”

But first, a quiz: suppose that you create a level in Hera with a `start
time`_ of 180 (three minutes of simulation before play starts) and add a
`Time condition`_ “IF game tick time ≥ 7200”. What does “7200” mean?

1. 6 minutes after start of simulation (3 after start of play)
2. 6 minutes after start of play (9 after start of simulation)
3. 2 minutes after start of simulation (1 before start of play)
4. 2 minutes after start of play (5 after start of simulation)
5. None of the above

Answer below.

Ares (and Antares) use what’s known as a fixed-step variable-FPS game
loop. The game logic updates 20 times per second (20Hz), but the frame
rate isn’t locked to it, and it can draw frames as fast as 60Hz.

Keeping the game logic at a fixed step is important, to make the game
feel consistent, but also to keep networked games synchronized. Then, on
fast machines, Ares interpolates between game ticks to make movement
appear smoother. Or, on slow machines, it skips frames to allow the game
logic to keep up.

In the game, these increments are referred to as “minor ticks” (60Hz)
and “major ticks” (20Hz). Minor ticks can be skipped, but the game logic
always runs at each major tick. This is why it’s unclear what 7200
means: is it 7200 *major* ticks (360 seconds / 20Hz) or 7200 *minor*
ticks (120 seconds / 60Hz)?

For that matter, why was the level’s start time given in seconds but the
condition time given in ticks?

Antares addresses the unit confusion by `specifying time durations with
strings`_ instead of numbers. A duration might look like ``1h15m5s30t``
(1 hour + 15 minutes + 5 seconds + 30 [minor] ticks). Each of the units
(h, m, s, t) is 60× the next. You can also write fractional amounts like
``1.5s``, but you can’t specify anything shorter than a minor tick, like
``0.01s``.

So, what is the answer to the quiz at the top? You guessed it: none of
the above. The correct answer is: 1 minute after start of play (4
minutes after start of simulation).

How does this happen? See, during simulation, before start of play, Ares
doesn’t need to draw to the screen. It executes the game logic each
major tick, and doesn’t track minor ticks at all. So, the timer counts
down at 20Hz, and at start of play, there are 3600 ticks (7200t -
180s*20Hz) left before the condition activates.

However, once play starts, Ares starts tracking minor ticks, and
counting down at 60Hz. 60 seconds (3600t/60Hz) later, the condition
activates.

You can preserve this behavior with `legacy_start_time`_, but I wouldn’t
recommend it.

.. _start time: https://hera.arescentral.org/pgs/hera_scenario_editor.html
.. _time condition: https://hera.arescentral.org/pgs/hera_condition_editor.html
.. _specifying time durations with strings: /plugins/format/types#duration
.. _legacy_start_time: /plugins/format/condition#time

.. -*- tab-width: 3; fill-column: 72 -*-
