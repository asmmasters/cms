#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Contest Management System - http://cms-dev.github.io/
# Copyright © 2016 Stefano Maggiolo <s.maggiolo@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Assembly ibm language definition."""

from cms.grading import CompiledLanguage

import os


__all__ = ["ASM_ibm"]


class ASM_ibm(CompiledLanguage):
    """This defines the Assembly ibm language, assembled with qemu-s390x (the
    version available on the system).

    """

    @property
    def name(self):
        """See Language.name."""
        return "Assembly_ibm"

    @property
    def source_extensions(self):
        """See Language.source_extensions."""
        return [".s"]

    @property
    def header_extensions(self):
        """See Language.source_extensions."""
        return [".h", ".c", ".inc", ".sh"]

    @property
    def object_extensions(self):
        """See Language.source_extensions."""
        return [".o"]

    @property
    def requires_multithreading(self):
        """See Language.requires_multithreading."""
        return True

    def get_compilation_commands(self,
                                 source_filenames, executable_filename,
                                 for_evaluation=True):
        """See Language.get_compilation_commands.
            a bash grader should be added to managers
            with library object files.
        """
        command = ["/bin/ibm-compile" ]
        for i in range(len(source_filenames)):
            source_filenames[i] = os.path.splitext(source_filenames[i])[0]
        command += source_filenames
        command += [executable_filename]
        return [command]

    def get_evaluation_commands(
            self, executable_filename, main=None, args=None):
        """See Language.get_evaluation_commands."""

        return [["/bin/ibm-eval", executable_filename]]

