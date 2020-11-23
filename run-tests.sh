#!/bin/sh
#
# This file is part of DoJSON
# Copyright (C) 2015, 2016 CERN.
# Copyright (C) 2020 Graz University of Technology.
#
#
# DoJSON is free software; you can redistribute it and/or modify
# it under the terms of the Revised BSD License; see LICENSE file for
# more details.
pydocstyle --match-dir='dojson' dojson && \
check-manifest --ignore ".travis-*"
python -m sphinx.cmd.build -qnNW docs docs/_build/html
python -m pytest
exit "$?" 