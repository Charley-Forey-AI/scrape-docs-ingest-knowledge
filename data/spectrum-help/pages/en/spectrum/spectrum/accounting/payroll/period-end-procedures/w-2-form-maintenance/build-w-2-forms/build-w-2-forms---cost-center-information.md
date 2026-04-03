---
title: "Build W-2 Forms - Cost Center Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/period-end-procedures/w-2-form-maintenance/build-w-2-forms/build-w-2-forms---cost-center-information"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/period-end-procedures/w-2-form-maintenance/build-w-2-forms/build-w-2-forms---cost-center-information"
---

# Build W-2 Forms - Cost Center Information

If cost centers are being used in this company, then when
 the W-2 form update is performed, you need to have cost center security for all employees to
 proceed, otherwise an error message will display.
Spectrum compares the cost center assigned to each employee
 included in the starting screen selection with cost centers in your operator's assigned
 cost center scheme, and if any cost center is not included, then the update will not be
 allowed.If entity tracking is enabled for the current company in
 the Enterprise Installation screen, this update will allow an employee to receive
 multiple forms using different 'Payer tax ID numbers'. The update will break employee
 earnings onto separate W-2 Forms based on 'Entity code' stored in the Payroll Check
 History Table. The software will first look to find the particular state or locality's
 tax code for the entity code and if found will then look for whether it has an assigned
 Payer tax ID number. If the state or locality does not have a tax code present, the
 taxpayer ID will be assigned from the tax table.
