#!/usr/bin/env python3
# Copyright 2023 Dave
# See LICENSE file for licensing details.

"""Charm the application."""

import logging

from ops.charm import CharmBase
from ops.main import main
from ops.model import ActiveStatus

logger = logging.getLogger(__name__)


class TestCharmDgCharm(CharmBase):
    """Charm the application."""

    def __init__(self, *args):
        super().__init__(*args)
        self.framework.observe(self.on.start, self._on_start)

    def _on_start(self, event):
        """Handle start event."""
        self.unit.status = ActiveStatus()


if __name__ == "__main__":  # pragma: nocover
    main(TestCharmDgCharm)
