# -*- coding: utf-8 -*-
#
# This file is part of DoJSON
# Copyright (C) 2015 CERN.
# Copyright (C) 2020 Graz University of Technology.
#
# DoJSON is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

"""ToMarc21 module for DoJSON to_marc21."""

from __future__ import absolute_import

from .model import to_marc21, to_marc21_authority

__all__ = (
    "to_marc21",
    "to_marc21_authority",
)
