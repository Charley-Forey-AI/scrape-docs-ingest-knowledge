---
title: "About Benefit Deductions, Liabilities, and Earnings Codes | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/human-resources/benefits/about-benefit-deductions-liabilities-and-earnings-codes"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/human-resources/benefits/about-benefit-deductions-liabilities-and-earnings-codes"
---

# About Benefit Deductions, Liabilities, and Earnings Codes

When you add a benefit for a resource (whether manually or via
 initialization), all deductions, liabilities, and earnings defined for the benefit (in HR
 Benefit Codes) are automatically set up on the Deduction/Liability Codes and Earnings Codes
 tabs (respectively).
You can add other deductions, liabilities, and/or earnings codes as desired; however, manually added deductions, liabilities, and/or earnings will not be updated to the benefit in HR Benefit Codes.
Note: The Deduction/Liability Codes and Earnings Codes tabs are
 read-only for all dependent sequences other than 0 (zero).
Deductions and liabilities assigned a frequency code in HR Benefit Codes are automatically flagged as 'employee-based' and are assigned a processing sequence of '1', which may be overridden. You will typically want to assign a higher processing sequence to those employee deductions that calculate as a rate of net.
If the deduction/liability is assigned a rate/amount in PR Deductions/Liabilities (i.e. Rate/Amount #1), that rate displays in the PR Rate/Amt #1 column in the grid. The column is display only, but is useful in determining whether you need to override the rate/amount for the employee. The rates also update when you update benefit codes to this form using HR Benefit Update.
The Ready checkbox available for each
 deduction and liability is used in combination with the Update PR
 checkbox in HR Benefit Codes to indicate whether the specified deduction, liability, or
 earnings code is ready to be updated to PR. If you do not select this checkbox, the
 deduction, liability, or earnings code will be skipped during the update. However, you
 can update the deduction, liability, or earnings code at a later date. For more
 information, see [Update PR](/en/vista/vista/hr-and-payroll/human-resources/benefits/about-the-hr-benefit-codes-form/field-definitions-hr-benefit-codes-form#ID-000104ca--en).
Note: You can track changes to benefit information by checking the
 Benefits option in the Employment History Event Option section of HR Company Parameters.
