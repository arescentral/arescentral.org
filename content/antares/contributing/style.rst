Style Guidelines
================

The Antares style guide adheres to the `Python style guide`_ where doing
so makes sense in C++.  In places where it does not, it draws some of
its inspiration from the `Google C++ style guide`_.

Much of the Antares code does not follow this style guide, since it was
developed by different authors over a long period of time.  When making
a change to a file that does not follow this style, it is discouraged to
make style changes in unrelated code, to avoid distraction from the
intended change.

.. _Python style guide: https://www.python.org/dev/peps/pep-0008/
.. _Google C++ style guide: https://google.github.io/styleguide/cppguide.html

Formatting
----------

Antares includes a ``.clang-format`` file. Run clang-format on your code
before committing, in order to follow the formatting rules.

Naming
------

*   Use the following patterns when picking identifiers:

    ..  code-block:: c++

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

*   TODO comments should include the email address or GitHub name of the
    person most knowledgeable about the issue that needs to be resolved.
    Such a comment is not a commitment on behalf of that person to
    resolve the issue.  Example:

    ..  code-block:: c++

        // TODO(bob@arescentral.org): do a barrel roll.
        // TODO(sfiera): write a style guide.

*   Each file should start with the standard Antares copyright header:

    ..  code-block:: c++

        // Copyright (C) 1997, 1999-2001, 2008 Nathan Lamont
        // Copyright (C) 2008-2020 The Antares Authors
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
        // License along with Antares.  If not, see https://www.gnu.org/licenses/

    This should be the very first thing in all files, before even the
    include guards or includes.

Language Features
-----------------

*   Each header should have include guards.  The symbol should begin
    with ``ANTARES_``, end with ``_``, and have its name between, in
    all-caps and with ``_`` replacing non-alphanumberic characters:

    ..  code-block:: c++

        #ifndef ANTARES_OBISH_AMBASSADOR_THRNTZ_HPP_
        #define ANTARES_OBISH_AMBASSADOR_THRNTZ_HPP_

        // content of "obish/ambassador-thrntz.hpp"

        #endif  // ANTARES_OBISH_AMBASSADOR_THRNTZ_HPP_

*   If a function body is empty, use ``= default`` if possible, and
    ``{}`` if not:

    ..  code-block:: c++

        void do_nothing() {}
        Spark::~Spark() = default;

*   Use pointers for mutable parameters.  When ordering parameters to
    a function, it is generally better to put in parameters first and
    out parameters last.  However, when a free function is method-like,
    the logical target of the function should be first:

    ..  code-block:: c++

        void destroy(const Object& killer, Object* killed) { ... }
        void activate(Device* device, const Object& parent, Point location) { ... }

*   Avoid bare pointers.  Wrap pointers in a smart pointer class such as
    ``std::unique_ptr`` as soon as possible. Use ``nullptr`` (not
    ``NULL`` or ``0``).

    ..  code-block:: c++

        std::unique_ptr<Object> create_thing() {
            std::unique_ptr<Object> result(new Object);
            // initialize result
            if (result->ok()) {
                return result;
            }
            return nullptr;
        }

*   In general, avoid copyable classes (movable classes are fine,
    though). Declare the constructor and assignment as ``= delete``:

    ..  code-block:: c++

        class Gateship {
          public:
            // There can only be one:
            Gateship::Gateship(const Gateship&) = delete;
            Gateship& operator=(const Gateship&) = delete;
        };

*   Throw ``std::runtime_error`` if programmer error has been detected,
    such as using an out-of-bounds array index.  Don't throw exceptions
    in code paths that are expected be followed during normal execution:

    ..  code-block:: c++

        bool build_at(const Object& base, int object_id) {
            if ((object_id < 0) || (max_object <= object_id)) {
                throw std::runtime_error(
                    pn::format("invalid object {0}", object_id).c_str());
            }
            if (base.is_building()) {
                return false;
            }
            ...
        }

..  -*- tab-width: 4; fill-column: 72 -*-
