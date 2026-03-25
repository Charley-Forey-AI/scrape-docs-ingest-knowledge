---
title: "Set Up a 401(k) Employer Match | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-up-pre-tax-deductions/set-up-a-401k-employer-match"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-up-pre-tax-deductions/set-up-a-401k-employer-match"
---

# Set Up a 401(k) Employer Match

Instructions for setting up a 401(k) company / employer match (liability), along with other required setup steps.
 These instructions include specifying the earnings on which the 401(k) liability should be calculated and registering the code in the PR Federal Info form so it will calculate on all employees with a corresponding 401(k) deduction.To view a tutorial, see [Vista Payroll Setup](https://academy.viewpoint.com/learn/course/external/view/elearning/2353/VistaPayrollSetup) in the Trimble Construction Academy

1. Open the PR Deductions/Liabilities form and select the New Record icon.

1. In the Dedn / Liab Code field, enter an unused number.

1. In the Description field, enter a description.

1. In the Type section, select Liability.

1. In the Liability Type field, enter the applicable liability type or press F4 to select from a list of liability types.

1. In the Calculation Category field, select Employee or Federal. If you select F-Federal, you must also select a Federal Type of 1-Withholding.

1. In the GL Account field, press F4 to select the appropriate GL liability credit account.

1. In the Method field, select G-Rate of Gross.

1. In the Rate / Amount #1 and Rate / Amount #2 fields, enter the same match percentage rate in negative decimal form in both fields. For example, if the employer match is 50%, enter –0.50000 in both fields.

1. In the Limit section, select Rate of Earnings.

1. In the limit Rate field, enter the result of the company match rate multiplied by the percentage limit. For example, if the company match rate is 50% of up to 7% of total regular earnings, the rate limit would be the product of 0.50 x 0.07 (.035000).

1. Select the Accumulate subject amounts checkbox.

1. Select the 401k Liability checkbox.The Pre-Tax Group field is enabled.

1. In the Pre-Tax Group field, enter the pre-tax deduction group assigned to the 401(k) deduction.The system uses the pre-tax group to determine the annual compensation limit for employer match liabilities.

1. If you want the liability amounts to update automatically to an Accounts Payable invoice:

1. Select the Addl Info tab.

1. Select the Automatic Update to Accounts Payable checkbox.

1. In the Vendor field, enter the vendor for the AP invoice.

1. Add applicable codes to the basis of the deduction.The system bases the employee 401(k) liability amounts on both the earnings codes and the 401(k) deduction code(s) you add to the basis of the liability. Add codes to the basis using one of the following methods:
OptionDescription
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

1.  Add the liability code to the PR Federal Info form.This is required to ensure the system correctly calculates the liability. Additionally, this enables the system to calculate the liability for all employees, eliminating the need to set it up manually for each employee in the PR Employee Dedns/Liabs form.

1. Open the PR Federal Info form.

1. In the PR Company field, enter the appropriate payroll company or press F4 to select it from a list.

1. Select the Add'l Federal Based Dedns/Liabs tab.

1. In the DLCode column, enter the code number of the liability code you just set up or press F4 to select it from a list.

Related information

- [Set Up a Multi-Tiered 401(k) Employer Match](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-up-pre-tax-deductions/set-up-a-multi-tiered-401k-employer-match)

- [Set Up a Standard 401(k) Deduction](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-up-pre-tax-deductions/set-up-a-standard-401k-deduction)

- [PR Employee Dedns/Liabs Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employee-dednsliabs-form)

- [PR Deductions/Liabilities Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-deductionsliabilities-form)
