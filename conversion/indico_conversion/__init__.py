# This file is part of the CERN Indico plugins.
# Copyright (C) 2014 - 2020 CERN
#
# The CERN Indico plugins are free software; you can redistribute
# them and/or modify them under the terms of the MIT License; see
# the LICENSE file for more details.

from __future__ import unicode_literals

from indico.legacy.common.cache import GenericCache
from indico.util.i18n import make_bound_gettext


_ = make_bound_gettext('conversion')
cache = GenericCache('pdf-conversion')
