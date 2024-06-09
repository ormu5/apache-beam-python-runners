# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 <LICENSE-APACHE or
# https://www.apache.org/licenses/LICENSE-2.0> or the MIT license
# <LICENSE-MIT or https://opensource.org/licenses/MIT>, at your
# option. This file may not be copied, modified, or distributed
# except according to those terms.

from apache_beam.options.pipeline_options import PipelineOptions

from my_app import app, CustomOptions

if __name__ == "__main__":
    import argparse
    import logging

    logging.basicConfig(level=logging.INFO)

    parser = argparse.ArgumentParser()
    args, beam_args = parser.parse_known_args()

    beam_options = PipelineOptions(
        # PortableRunner:
        # Use below for running with available beam server / spark dependencies available
        # save_main_session=True,
        # setup_file="./setup.py",
        # runner="PortableRunner",
        # job_endpoint="localhost:8099",
        # artifact_endpoint="localhost:8098",
        # environment_type="EXTERNAL",
        # environment_config="beam-python-workers:50000"
        # DirectRunner: comment above and uncomment below
        runner="DirectRunner",
        environment_type="LOOPBACK"
    )
    custom_options = PipelineOptions(beam_args).view_as(CustomOptions)
    app.run(
        custom_options.input_text,
        beam_options=beam_options
    )
