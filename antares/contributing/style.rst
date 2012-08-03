..  _style guidelines:

Style Guidelines
================

..  highlight:: c++

The Antares style guide adheres to the `Python style guide`_ where doing
so makes sense in C++.  In places where it does not, it draws some of
its inspiration from the `Google C++ style guide`_.

Much of the Antares code does not follow this style guide, since it was
developed by different authors over a long period of time.  When making
a change to a file that does not follow this style, it is discouraged to
make style changes in unrelated code, to avoid distraction from the
intended change.

.. _Python style guide: http://www.python.org/dev/peps/pep-0008/
.. _Google C++ style guide: http://google-styleguide.googlecode.com/svn/trunk/cppguide.xml

Formatting
----------

*   Lines should not be too long.  100 characters is definitely too
    long.  Comments should be shorter so they are easier to read--72
    characters is a good width.

*   Indent with four spaces, never tabs::

        int main(int argc, char* argv[]) {
            if (argc) {
                return 1;
            }
            return 0;
        }

*   Each header should have include guards.  The symbol should begin
    with ``ANTARES_``, end with ``_``, and have its name between, in
    all-caps and with ``_`` replacing non-alphanumberic characters.  The
    ``#endif`` should reference the symbol::

        #ifndef ANTARES_OBISH_AMBASSADOR_THRNTZ_HPP_
        #define ANTARES_OBISH_AMBASSADOR_THRNTZ_HPP_

        // content of "obish/ambassador-thrntz.hpp"

        #endif  // ANTARES_OBISH_AMBASSADOR_THRNTZ_HPP_

*   After the copyright header and include guards, all files should
    start with ``#include`` directives: first the corresponding header,
    then system includes, then project includes; with each group sorted
    and separated by blank lines::

        #include "obish/ambassador-thrntz.hpp"

        #include <stdint.h>
        #include <string>

        #include "game/globals.hpp"
        #include "obish/obiard.hpp"

        // content of "obish/ambassador-thrntz.cpp"

*   Don't indent namespace blocks.  Add a matching comment at the close
    of each namespace::

        namespace antares {
        namespace {

        const char kOrigin[] = "Los Ran";

        }  // namespace
        }  // namespace antares

*   Put open-braces on the same line as the function or control
    statement they provide the body for.  If the body is empty, the
    close-brace can go there too::

        while (true) {
            if (should_exit()) {
                break;
            }
        }

        void do_nothing() { }

*   Always put the body of a control statement on a separate line, with
    curly braces, even if it is one line::

        if (player_won) {
            ++wins;
        } else {
            ++losses;
        }

*   With initializer lists, put the colon with the close-parenthesis,
    and indent the initializers two levels::

        Grolk::Grolk():
                _appearance("panda"),
                _gullible(true) {
            // This will not end well.
        }

Naming
------

*   Use the following patterns when picking identifiers::

        namespace exns
        class ExampleClass
        void free_function()
        int local_variable
        void ExampleClass::member_function()
        int _private_member_variable
        int struct_member_variable
        const int kConstantVariable
        enum ExampleEnum
        ENUM_VALUE = 0

    If following a pre-existing pattern, use its naming scheme.  For
    example, STL-like types (``iterator``, ``value_type``) should be
    named using that pattern.

*   Files should have a suffix as appropriate for their language:

    -   For C++, ``.hpp`` for headers and ``.cpp`` for source files
    -   For C, ``.h`` for headers and ``.c`` for source files
    -   For Objective-C, ``.h`` for headers and ``.m`` for source files

Comments
--------

*   Prefer ``//`` comments to ``/* */`` comments.  This makes it easier
    to comment out a block temporarily using ``/* */`` comments.

*   For comments at the end of a line, add at least two spaces before
    the comment::

        const int kTimeDilation = 30;  // 5 years onboard; 150 years outside.
                                     ^^

*   TODO comments should include the email address or GitHub name of the
    person most knowledgeable about the issue that needs to be resolved.
    Such a comment is not a commitment on behalf of that person to
    resolve the issue.  Example::

        // TODO(bob@arescentral.org): do a barrel roll.
        // TODO(sfiera): write a style guide.

*   Each file should start with the standard Antares copyright header::

        // Copyright (C) 1997, 1999-2001, 2008 Nathan Lamont
        // Copyright (C) 2008-2012 The Antares Authors
        //
        // This file is part of Antares, a tactical space combat game.
        //
        // Antares is free software: you can redistribute it and/or modify it
        // under the terms of the Lesser GNU General Public License as published
        // by the Free Software Foundation, either version 3 of the License, or
        // (at your option) any later version.
        //
        // Antares is distributed in the hope that it will be useful, but
        // WITHOUT ANY WARRANTY; without even the implied warranty of
        // MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
        // Lesser General Public License for more details.
        //
        // You should have received a copy of the GNU Lesser General Public
        // License along with Antares.  If not, see http://www.gnu.org/licenses/

    This should be the very first thing in all files, before even the
    include guards or includes.

Language Features
-----------------

*   Use references for mutable parameters.  When ordering parameters to
    a function, it is generally better to put in parameters first and
    out parameters last.  However, when a free function is method-like,
    the logical target of the function should be first::

        void swap(Admiral& x, Admiral& y) { ... }
        void activate(Device& device, const Object& parent, Point location) { ... }

*   Avoid bare pointers.  Wrap pointers in a smart pointer class such as
    ``sfz::scoped_ptr`` or ``sfz::scoped_array`` as soon as possible
    (don't use ``std::auto_ptr``, though).  Instead of documenting where
    ownership transfers occur, it's easiest to have functions take smart
    pointers as out parameters::

        bool create_thing(sfz::scoped_ptr<Object>& thing) {
            sfz::scoped_ptr<Object> result(new Object);
            // initialize result
            if (result.ok()) {
                thing.reset(result.release());
                return true;
            }
            return false;
        }

*   Throw an ``Exception`` if programmer error has been detected, such
    as using an out-of-bounds array index.  Don't throw exceptions in
    code paths that are expected be followed during normal execution::

        bool build_at(const Object& base, int object_id) {
            if ((object_id < 0) || (max_object <= object_id)) {
                throw Exception(format("invalid object {0}", object_id);
            }
            if (base.is_building()) {
                return false;
            }
            ...
        }

..  -*- tab-width: 4; fill-column: 72 -*-
