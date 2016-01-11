# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import collective.framework7


class CollectiveFramework7Layer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=collective.framework7)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.framework7:default')


COLLECTIVE_FRAMEWORK7_FIXTURE = CollectiveFramework7Layer()


COLLECTIVE_FRAMEWORK7_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_FRAMEWORK7_FIXTURE,),
    name='CollectiveFramework7Layer:IntegrationTesting'
)


COLLECTIVE_FRAMEWORK7_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_FRAMEWORK7_FIXTURE,),
    name='CollectiveFramework7Layer:FunctionalTesting'
)


COLLECTIVE_FRAMEWORK7_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        COLLECTIVE_FRAMEWORK7_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='CollectiveFramework7Layer:AcceptanceTesting'
)
