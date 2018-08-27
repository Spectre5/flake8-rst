import os
import sys

from flake8 import utils
from flake8.checker import FileChecker, Manager, LOG
from flake8.processor import FileProcessor

from flake8_rst.rst import find_sourcecode


class RstManager(Manager):

    def make_checkers(self, paths=None):
        # type: (List[str]) -> NoneType
        """Create checkers for each file."""
        if paths is None:
            paths = self.arguments

        if not paths:
            paths = ['.']

        filename_patterns = self.options.filename
        running_from_vcs = self.options._running_from_vcs
        running_from_diff = self.options.diff

        # NOTE(sigmavirus24): Yes this is a little unsightly, but it's our
        # best solution right now.
        def should_create_file_checker(filename, argument):
            """Determine if we should create a file checker."""
            matches_filename_patterns = utils.fnmatch(
                filename, filename_patterns
            )
            is_stdin = filename == '-'
            file_exists = os.path.exists(filename)
            # NOTE(sigmavirus24): If a user explicitly specifies something,
            # e.g, ``flake8 bin/script`` then we should run Flake8 against
            # that. Since should_create_file_checker looks to see if the
            # filename patterns match the filename, we want to skip that in
            # the event that the argument and the filename are identical.
            # If it was specified explicitly, the user intended for it to be
            # checked.
            explicitly_provided = (not running_from_vcs and not running_from_diff and (argument == filename))
            return ((file_exists and (explicitly_provided or matches_filename_patterns)) or is_stdin)

        checks = self.checks.to_dictionary()

        checkers = []

        for argument in paths:
            for filename in utils.filenames_from(argument, self.is_path_excluded):
                if should_create_file_checker(filename, argument):
                    checker = RstFileChecker(filename, checks, self.options)

                    if checker.should_process:
                        lines = checker.processor.read_lines()

                        for code, indent, line_number in find_sourcecode(''.join(lines)):
                            checker = RstFileChecker(filename, checks, self.options,
                                                     lines=[line + '\n' for line in code.split('\n')],
                                                     start=line_number, indent=indent)
                            checkers.append(checker)
        self.checkers = checkers
        assert checkers
        LOG.info('Checking %d files', len(self.checkers))


class RstFileChecker(FileChecker):
    def __init__(self, filename, checks, options, lines=None, start=None, indent=0):
        self.lines = lines
        self.start = start
        self.indent = indent
        super(RstFileChecker, self).__init__(filename, checks, options)

    def _make_processor(self):
        try:
            return FileProcessor(self.filename, self.options, lines=self.lines)
        except IOError:
            # If we can not read the file due to an IOError (e.g., the file
            # does not exist or we do not have the permissions to open it)
            # then we need to format that exception for the user.
            # NOTE(sigmavirus24): Historically, pep8 has always reported this
            # as an E902. We probably *want* a better error code for this
            # going forward.
            (exc_type, exception) = sys.exc_info()[:2]
            message = '{0}: {1}'.format(exc_type.__name__, exception)
            self.report('E902', 0, 0, message)
            return None

    def report(self, error_code, line_number, column, text, line=None):
        return super(RstFileChecker, self).report(error_code, line_number + self.start,
                                                  column + self.indent, text, line=line)
