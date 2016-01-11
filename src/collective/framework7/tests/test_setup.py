# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from collective.framework7.testing import COLLECTIVE_FRAMEWORK7_INTEGRATION_TESTING  # noqa
from plone import api

import unittest2 as unittest


class TestSetup(unittest.TestCase):
    """Test that collective.framework7 is properly installed."""

    layer = COLLECTIVE_FRAMEWORK7_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if collective.framework7 is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('collective.framework7'))

    def test_browserlayer(self):
        """Test that ICollectiveFramework7Layer is registered."""
        from collective.framework7.interfaces import ICollectiveFramework7Layer
        from plone.browserlayer import utils
        self.assertIn(ICollectiveFramework7Layer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = COLLECTIVE_FRAMEWORK7_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['collective.framework7'])

    def test_product_uninstalled(self):
        """Test if collective.framework7 is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled('collective.framework7'))
