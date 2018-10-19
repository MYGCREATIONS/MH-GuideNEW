# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 08:13:39 2018

@author: mdcayoglu
"""

from lettuce import step
from Framework.pages.adminPortalPage import Adminportal

admin = Adminportal()


@step('I go to the \[(.*)\]')
def goToEditor(step, action):
    if action == "Lab Editor":
        admin.goToLabEditor()
        admin.verifyLabEditorTab()

    if action == "User Editor":
        admin.goToUserEditor()
        admin.verifyUserEditorTab()

    if action == "Labtest Editor":
        admin.goToUserEditor()
        admin.verifyLabtestEditorTab()

    if action == "OrgUnit Editor":
        admin.goToOrgUnitEditor()
        admin.verifyOrgUnitEditorTab()
