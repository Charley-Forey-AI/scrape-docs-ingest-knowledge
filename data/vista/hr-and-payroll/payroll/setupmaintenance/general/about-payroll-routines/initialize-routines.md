---
title: "Initialize Routines | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-payroll-routines/initialize-routines"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-payroll-routines/initialize-routines"
---

# Initialize Routines

You can use PR Routines to initialize (update or add) routines
 to the system.
Routines enable complex deduction, liability, and earnings calculations.
Routines identify the method used to calculate a
 deduction, liability, or earnings amount when a simple method (such as a rate of gross
 or rate per hour) is not sufficient. For example, Vista uses routines for
 federal withholding and most state/province withholding tax deductions that are based on
 tables and percentage calculations.
When you first implement Vista, you will need to initialize routines for each payroll company (and every time you add a new one); this adds the standard list of routines that the system utilizes for calculations. You will also need to re-initialize routines after loading year-end or tax update releases in order to update existing routines or add new ones to the system.
The following instructions outline how to initialize routines.

1. Select File > Initialize from PR Routines. The system will add the routine to the system and,
 for tax routines, update the associated procedure with the current tax year.Note: For example, the federal tax routine for the
 U.S. is named bspPRFWTXX, where the XX indicates the current tax year. If there
 are multiple updates to a tax routine in a single year, the routine name includes
 a sequential number which changes each time an update occurs (e.g., bspPRFWT132,
 bspPRFWT133, etc.) .

1. Once you have initialized
 routines for the first time, you may need to enter miscellaneous amounts for
 particular states/provinces in the Misc Amt fields. See [Routines](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-payroll-routines) to determine if you need to set any miscellaneous amounts in the
 Misc
 Amt fields.

1. You can now associate the routine with a deduction, liability, or earnings code (PR Deductions/Liabilities and PR Earnings Codes, respectively) if you have not done so already. For more information, see [Determining the Method of Calculation for D/L Codes](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/about-methods-of-calculation/about-determining-the-method-of-calculation-for-dl-codes) or [Determining Earnings Code Calculation Methods](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/earnings-code-calculation-methods).
