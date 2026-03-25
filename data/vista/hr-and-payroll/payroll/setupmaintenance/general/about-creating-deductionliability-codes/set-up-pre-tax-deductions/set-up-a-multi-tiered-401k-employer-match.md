---
title: "Set Up a Multi-Tiered 401(k) Employer Match | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-up-pre-tax-deductions/set-up-a-multi-tiered-401k-employer-match"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-up-pre-tax-deductions/set-up-a-multi-tiered-401k-employer-match"
---

# Set Up a Multi-Tiered 401(k) Employer Match

Instructions for setting up a multi-tiered 401(k) employer match liability, along with other required setup steps. A Safe Harbor 401(k) is an example of a multi-tiered 401(k) plan.
Before proceeding, you will need to do the following:

- [Set up a Pre-Tax Deduction Group](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-a-pre-tax-deduction-group). The system uses this group to apply limits across multiple 401(k) liabilities.

- Determine your company match and apply it to a formula for the system to process it correctly. Company matches are commonly phrased like this: "100% match of the first 3% of employee contributions and 30% match of the next 2% of employee contributions." Insert your values in the following statement:(A)_______ match of the first (B)_______ of employee contributions and (C)_______ match of the next (D)_______ of employee contributions.
For clarity, the following instructions refer to these four values as A, B, C, and D.

These instructions include specifying the earnings on which the 401(k) liability should be calculated and registering the code in the PR Federal Info form so it will calculate on all employees with a corresponding 401(k) deduction.Tiered 401(k) employer matches require use of more than one liability code because there is more than one limit. Because the system calculates both liabilities on all wages at all times up to their respective limit, the codes work in tandem to calculate the correct total match.
To view a tutorial, see [Vista Payroll Setup](https://academy.viewpoint.com/learn/course/external/view/elearning/2353/VistaPayrollSetup) in the Trimble Construction Academy

1. Set up the first Liability Code

1. Open PR Deductions/Liabilities and select New Record.

1. In the Dedn / Liab Code field, enter a number that will be assigned to this new liability code.

1. In the Description field, enter a description.

1. In the Type section, select Liability.

1. In the Calculation Category field, select E-Employee or F-Federal.If you select F-Federal, you must also select a Federal Type of 1-Withholding.

1. In the GL Account field, press F4 to select the appropriate GL liability credit account.

1. In the Method field, select G-Rate of Gross.

1. In the Rate / Amount #1 and Rate / Amount #2 fields, enter the value of (A – C) in negative decimal form in both fields. Using the sample above, the entry would be the sum of 1.00 – 0.30 (–0.70000) in both fields.

1. In the Limit section, select the Rate of Earnings option.

1. In the Rate field, enter the value of (A – C) multiplied by the value of B. Using the sample above, the entry would be the product of 0.70 x 0.03 (.021000).

1. Select the Accumulate subject amounts checkbox.

1. Select the 401k Liability checkbox.

1. In the Pre-Tax Group field, press F4 to select a pre-tax group.The system uses the pre-tax group to determine the annual compensation limit for employer match liabilities.

1. If you want the liability amounts to update automatically to an Accounts Payable invoice, on the Addl Info tab, select the Automatic Update to Accounts Payable checkbox. Then in the Vendor field, enter the vendor.

1. Add the earnings that contribute to the 401(k) liability amounts.The system bases the employee 401(k) liability amounts on the earnings codes you add to the basis of the liability.OptionDescription
Add basis codes manually

1. Select the Basis Codes tab.

1. Add each of the earnings codes here that you set up on the 401(k) deduction(s) you are matching. For each earnings codes, select the Subject Only checkbox..

1. Add each 401(k) deduction code that you are matching. Do not select the Subject Only checkbox on the 401(k) deduction code(s).

Add multiple basis codes

1. Select Add Basis Codes. The PR Add DL Basis Codes form displays.

1. In the Basis Codes section, select one of the following:

- Copy basis codes from another DL Code - Select this option to copy the basis codes from an existing deduction or liability code. Then using the DL Code to Copy From field, enter the deduction or liability code or press F4 to select from a list of existing codes.

- Add all eligible Earnings and DL Codes to basis - Select this option to apply all existing eligible earnings, deductions, and liability codes as the basis.

1. Select Add.

1. In Basis Codes grid, delete any individual earnings, deduction, or liability codes that do not apply.

1. For each earnings code in the grid, select the Subject Only checkbox.

1. For each 401(k) deduction in the grid, leave the Subject Only checkbox unselected.

1.  Set up the second Liability Code.

1. In the Dedn / Liab Code field, enter a number that will be assigned to this new liability code.

1. In the Description field, enter a description.

1. In the Type section, select Liability.

1. In the Calculation Category field, select E-Employee or F-Federal.If you select F-Federal, you must also select a Federal Type of 1-Withholding.

1. In the GL Account field, press F4 to select the appropriate GL liability credit account.

1. In the Method field, select G-Rate of Gross.

1. In the Rate / Amount #1 and Rate / Amount #2 fields, enter the value of A or C, whichever is less, in negative decimal form in both fields. Using the sample above, the entry would be –0.30000 in both fields.

1. In the Limit section, select the Rate of Earnings option.

1. In the Rate field, enter whichever is less:

- A multiplied by the value of (B + D) or

- C multiplied by the value of (B + D)

Using the sample above, the entry would be the product of 0.30 x 0.05 (.015000).

1. Select the Accumulate subject amounts checkbox.

1. Select the 401k Liability checkbox.

1. In the Pre-Tax Group field, press F4 to select a pre-tax group.The system uses the pre-tax group to determine the annual compensation limit for employer match liabilities.

1. If you want the liability amounts to update automatically to an Accounts Payable invoice, on the Addl Info tab, select the Automatic Update to Accounts Payable checkbox. Then in the Vendor field, enter the vendor.

1. Add the earnings that contribute to the 401(k) liability amounts.Repeat the instructions in Step 2, this time for the liability code you just created in Step 3. Apply the same earnings codes and deduction codes to both liability codes.

1.  Add both liability codes to the PR Federal Info form.This is required to ensure the system correctly calculates the liability. Additionally, this enables the system to calculate the liabilities for all employees, eliminating the need to set them up manually for each employee in the PR Employee Dedns/Liabs form.

1. Open the PR Federal Info form.

1. In the PR Company field, enter the appropriate payroll company or press F4 to select it from a list.

1. Select the Add'l Federal Based Dedns/Liabs tab.

1. In the DLCode column, enter the code number of the first liability code you set up or press F4 to select it from a list.

1. Repeat for the second liability code.

Related information

- [Set Up a 401(k) Employer Match](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-up-pre-tax-deductions/set-up-a-401k-employer-match)

- [PR Deductions/Liabilities Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-deductionsliabilities-form)

- [PR Employee Dedns/Liabs Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employee-dednsliabs-form)

- [Set Up a Standard 401(k) Deduction](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-up-pre-tax-deductions/set-up-a-standard-401k-deduction)
