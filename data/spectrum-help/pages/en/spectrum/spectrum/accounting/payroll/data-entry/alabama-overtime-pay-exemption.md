---
title: "Alabama Overtime Pay Exemption | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/data-entry/alabama-overtime-pay-exemption"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/data-entry/alabama-overtime-pay-exemption"
---

# Alabama Overtime Pay Exemption

Process your Alabama state income tax exemption, whether for the all timecards in the pay cycle, or for a single layoff check.
Since you should run this utility only once per pay cycle, these steps should be complete for the given pay cycle before you proceed:

- All time cards for all employees are entered

- All Pre-time card batches are transferred to the pay cycle

Note: Running this utility for a layoff check affects the timecards for only the employee receiving the layoff check.

This utility computes the amount of eligible overtime and double time wages and creates a single, new timecard line for each eligible employee to offset the amount of the eligible OT wages. This effectively reduces the employee's taxable income and their state income tax deduction relative to what it would have been without the exemption.Steps 1 and 2 are setup steps. Skip to step 3 if the required setup was completed previously.

1. Take these steps to set up an Add-on code dedicated for use only for this Alabama exemption:

1. Go to Payroll > Maintenance > Deduction / Add-on Code.

1. Select New.

1. In the Type field, select Add-on.

1. In the Calculation Method field, select Fixed.

1. In the Frequency field, select ALL.

1. For the G/L Account code, choose a Miscellaneous or Clearing account.

1. Select Clear employee balance at year end?.

1. In the Tax Effects tab, add the Alabama tax code (AL) and select the Income Tax checkbox.

1. In the Add-ons tab, set the cost as Non-direct and in the Non-cash G/L account  field, enter the same account as the G/L Account code on the properties tab.The Add-on code is now ready for use by the utility.

1. Take these steps to enable use of the utility:

1. Go to Payroll > Maintenance > Tax Tables > AL OT Exemption.The Alabama Overtime Pay Exemption Maintenance window opens.

1. Select Enable this feature?.

1. Select Overtime and Double time.

1. In the Add-on code field, select the dedicated AL record created in Step 1.

1. In the Department field, select a payroll department which is non-direct.

1. Select OK.The utility can now be used by those processing payroll.

1. Take these steps to run the utility once per pay cycle (or once per layoff check):

1. From the Time Card Entry or the Layoff Check Entry screen, select the AL OT Exempt button.The Alabama Overtime Pay Exemption Utility window opens.

1. Select Continue.

The system creates a timecard line for each impacted employee, and the amount of Alabama state taxable wages for each employee which had overtime or double time wages is reduced by the amount of the OT or DT wages.Note: Each of the timecard lines created by this utility contain the message, "Overtime exemption adjustment".

If this is not the first time you've run this utility for a given pay cycle (or layoff check), delete any extra timecard lines for employee records which were created in the previous run(s).
