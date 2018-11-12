from lettuce import step
from Framework.pages.cviPage import CreateCvi
from Framework.pages.dashboardPage import Dashboard


dashboard = Dashboard()
#this is a comments
@step('I click on \[(.*)\]')
