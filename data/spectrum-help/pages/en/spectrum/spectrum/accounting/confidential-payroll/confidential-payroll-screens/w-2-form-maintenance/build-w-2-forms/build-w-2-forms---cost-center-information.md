---
title: "Build W-2 Forms - Cost Center Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/confidential-payroll/confidential-payroll-screens/w-2-form-maintenance/build-w-2-forms/build-w-2-forms---cost-center-information"
fetched_at: "2026-04-03T20:43:54.261868+00:00"
menu_path: "/en/spectrum/spectrum/accounting/confidential-payroll/confidential-payroll-screens/w-2-form-maintenance/build-w-2-forms/build-w-2-forms---cost-center-information"
---

# Build W-2 Forms - Cost Center Information

If cost centers are being used in this company, then when the W-2 form update is performed, the operator performing the update must have security authorization for all affected employees in order to perform the update. For employees in the current company, Spectrum compares the cost center assigned to each employee included in the starting screen selection with cost centers in the operator's assigned scheme; if any cost center is not included, then the update will not be allowed.
For employees in other companies, cost center validation is performed based on settings in each included company. If the cost center feature is enabled in the Enterprise Installation screen for the non-confidential company, then the cost center assigned to each employee in each non-confidential company must be included in the list of valid cost centers for the operator's schemes of those non-confidential companies. If any cost center is not included, then the update will be disallowed. If the cost center feature is disabled in the Enterprise Installation screen for the non-confidential company, then cost center validation will not occur for those employees.
If entity tracking is enabled for the current company in the Enterprise Installation screen, this update will allow an employee to receive multiple forms using different 'Payer tax ID numbers'. The update will break employee earnings onto separate W-2 Forms based on 'Entity code' stored in the Payroll Check History Table. The software will first look to find the particular state or locality's tax code for the entity code and if found will then look for whether it has an assigned Payer tax ID number. If the state or locality does not have a tax code present, the taxpayer ID will be assigned from the tax table.
