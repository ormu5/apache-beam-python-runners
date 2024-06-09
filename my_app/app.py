# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 <LICENSE-APACHE or
# https://www.apache.org/licenses/LICENSE-2.0> or the MIT license
# <LICENSE-MIT or https://opensource.org/licenses/MIT>, at your
# option. This file may not be copied, modified, or distributed
# except according to those terms.
import logging
from typing import Callable, Optional

import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
import humps  # Excuse to use an external lib to confirm dependency staging

logger = logging.getLogger(__name__)


class CustomOptions(PipelineOptions):
    @classmethod
    def _add_argparse_args(cls, parser):
        parser.add_argument(
            "--input-text",
            default="Default input text",
            help="Input text to print.",
        )


def run(
        input_text: str,
        beam_options: Optional[PipelineOptions] = None,
        test: Callable[[beam.PCollection], None] = lambda _: None,
) -> None:
    with beam.Pipeline(options=beam_options) as pipeline:
        elements = (
                pipeline
                # | "Create snake_case strings" >> beam.Create(input_text.split(' '))
                | "Create snake_case strings" >> beam.Create(['oneString', 'twoString', 'threeString'])
                | "Print snake_case strings" >> beam.Map(lambda x: logger.info(humps.decamelize(x)))
        )

        # Used for testing only.
        test(elements)
