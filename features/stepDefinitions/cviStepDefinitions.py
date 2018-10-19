from lettuce import step
from Framework.pages.cviPage import CreateCvi
from Framework.pages.dashboardPage import Dashboard

createCvi = CreateCvi()
dashboard = Dashboard()

@step("I create a new cvi")
def createNewCvi(step):
    createCvi.createCvi()


@step("the new cvi is successfully created")
def verifyCviCreated(step):
    createCvi.verifyCviCreated()


@step("a new menu create a new cvi shows up")
def inManageAdditionalTestResults(step):
    assert createCvi.verifyCreateANewCvi()


@step("I look for the cvi \[(.*)\]")
def lookForCvi(step, cviName):
    dashboard.typeSearch(cviName)


@step("I expand the details of the cvi \[(.*)\]")
def expandDetailsCvi(step, cviStatus):
    createCvi.expandDetailsCvi(cviStatus)


@step("I click on the plus icon to add a custom cvi")
def plusIconCustomCvi(step):
    createCvi.clickPlusIcon()


@step("I change the impact to \[(.*)\]")
def changeImpactCvi(step, impact):
    createCvi.addImpactToCvi(None, impact)


@step("I change the cvi name to \[(.*)\]")
def changeNameCvi(step, cviNameNew):
    createCvi.addNameToCvi(None, cviNameNew)
