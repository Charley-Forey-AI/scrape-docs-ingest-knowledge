---
title: "Build T4 Slips | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/year-end/year-end-for-canada-payrolls/processing/year-end-processing-screen-can/build-t4-slips"
fetched_at: "2026-04-03T20:47:07.463050+00:00"
menu_path: "/en/spectrum/spectrum/year-end/year-end-for-canada-payrolls/processing/year-end-processing-screen-can/build-t4-slips"
---

# Build T4 Slips

The Build T4 Slips screen clears the T4 file and calculates
 T4 information based on the payroll earnings history file.
Employees should be prevented from printing their T4 Slips from their
 Dashboard app (if installed) until the Payroll Department completes its review of the
 current year's forms. Do this by clearing the Allow employees to print year end tax statements? checkbox in the Employee Kiosk
 Installation screen until after the build is complete.
One row displays for every deduction and add-on code in the current company.
The current CPP/QPP earnings limits display. The default value is determined by what is entered in the Payroll Installation screen, in this order:

1. The value in the Employee second tier limit field. If blank, it uses:

1. The value in the Employee first tier limit field.Note: If a zero appears here, it's because both field values are blank in the Payroll Installation screen; this should be corrected.

Note:You can override these default values if needed.If you are calculating T4s for a prior year, you can modify the values on this screen and perform the build for the prior year, without affecting the current year's already-calculated amounts.

- The previous T4 for each employee is stored each time this update is performed. This allows you to restore a T4 if you discover later that a needed T4 record has been lost due to re-running the update after purging.

- After reviewing this screen and making any necessary changes, select Continue to run the update. During the update, a number of values (taxes, earnings, add-ons, deductions) will be allocated across the employee's T4 Slips whenever multiple provinces are present.Note: T4 Processing is not provided through Confidential Payroll
 because the Canadian Revenue Agency permits more than one electronic file from the
 same employer.

If doing year-end processing, see [T4 Slip Maintenance](/en/spectrum/spectrum/year-end/year-end-for-canada-payrolls/processing/year-end-processing-screen-can/t4-slip-maintenance).

Related information

- [Year End Processing Screen (CAN)](/en/spectrum/spectrum/year-end/year-end-for-canada-payrolls/processing/year-end-processing-screen-can)
