---
title: "Correcting State Income Tax Deductions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/maintenance-overview/tax-table-maintenance/correcting-state-income-tax-deductions"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/maintenance-overview/tax-table-maintenance/correcting-state-income-tax-deductions"
---

# Correcting State Income Tax Deductions

If any of your employees' records indicate that they are
 being taxed SIT, SDI, and/or unemployment in the wrong state, you will want to correct this
 for quarterly and annual reports.
The following instructions will correct state income tax.
To solve the problem of the wrong state's state income taxes being deducted, there are two figures you need to correct: 'subject to' wages for the work state and the actual income tax deduction on employee checks and W-2s. These figures are corrected by transferring the earnings to a dummy state code or to the correct state code.
Important: We recommend you print the state tax history
 report during the payroll cycle and the state, county and local quarterly tax report
 afterwards to confirm a successful outcome.

## Correcting Income Tax Amounts

1. In Tax Table Maintenance, correct the tax table and create a new 'dummy' state tax. [Tax Table Maintenance Procedure](/en/spectrum/spectrum/accounting/payroll/maintenance-overview/tax-table-maintenance/correcting-state-income-tax-deductions/tax-table-maintenance-procedure)

1. On the Site Map, click Payroll  >  Maintenance  >  Worker's Compensation to display the Worker's Compensation Code Maintenance screen.

1. Click the Base Code button and create a worker's compensation base code. Click OK to save and return to the main screen.

1. Create a worker's compensation code for the state code XX or ZZ that was created in step #1. This will have $0 liability and deductions calculated; it is created simply to bypass the Time Card Entry screen protections.

1. In Time Card Entry, enter this next week's regular payroll cycle for these employees, creating a time card line with an SA pay type. The department should be a non-job department. You may wish to set up a special 'dummy' payroll tax department in General Ledger  >  Maintenance  >  Master File Maintenance with the direct cost field set to No direct cost. This allows you to keep a record in one payroll department.
Note: The use of a 'dummy' payroll department is optional, but
 using a non-job department is mandatory. During Time Card Entry, press F4 or
 double-click on the wage/tax field and enter the incorrect work state code that
 was used as the work state. The rate should be a negative dollar amount equal to
 the work state earnings tax that was collected in error. In essence, you are
 creating a negative earning for the work state in the amount of the year-to-date
 to be reversed.

1. Enter another line in Time Card Entry mirroring the line above. Using the same department in Time Card Entry, create another time card line using SA as the pay type and enter positive dollars equal to the negative amount entered in step #5.

1. Press F4 or double-click on the tax field and enter the 'dummy' state tax code and workers compensation code. The employee's hours and earnings should now read 0 at the top right of the screen if these are the only lines entered for the employee.

1. Continue with regular payroll processing. After running the Payroll  >  Data Entry  >  Payment Processing  >  Check Calculation, select Check Adjustment. Call up each employee for which you performed steps #5 and #6.

1. Click the SIT button, select the appropriate state tax line, and enter a negative tax amount for the total amount of income tax deducted in error from the employee's checks. By entering the work state tax as a negative amount, you will be adding a dollar amount to the net check. Press F3.

1. Complete the Payroll processing.
