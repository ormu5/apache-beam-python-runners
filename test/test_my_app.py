# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 <LICENSE-APACHE or
# https://www.apache.org/licenses/LICENSE-2.0> or the MIT license
# <LICENSE-MIT or https://opensource.org/licenses/MIT>, at your
# option. This file may not be copied, modified, or distributed
# except according to those terms.

# For more information on unittest, see:
#   https://docs.python.org/3/library/unittest.html

import unittest
from unittest.mock import patch
import logging

from apache_beam.testing.test_pipeline import TestPipeline
from apache_beam.testing.util import assert_that, equal_to

import my_app

# Configure the logger
logger = logging.getLogger('my_app')
logging.basicConfig(level=logging.INFO)


@patch("apache_beam.Pipeline", TestPipeline)
# @patch("logging.Logger.info", lambda x: x.getMessage())  # Patch logger.info instead of print
# @patch("builtins.print", lambda x: x)
class TestApp(unittest.TestCase):
    def test_run_direct_runner(self):
        # Note that the order of the elements doesn't matter.
        expected = ["one_string", "two_string", "three_string"]
        with self.assertLogs('my_app', level='INFO') as log:
            my_app.run(
                input_text="oneString twoString threeString",
                # Right now accounting for log methods having no output...
                # test=lambda elements: assert_that(elements, equal_to(expected)),
            )

        # ...instead, checking logs here instead of in elements
        log_messages = [record.getMessage() for record in log.records]
        for expected_message in expected:
            self.assertIn(expected_message, log_messages)


if __name__ == "__main__":
    unittest.main()
