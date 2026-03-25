---
title: "Set Up a Roth 401(k) Deduction | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-up-pre-tax-deductions/set-up-a-roth-401k-deduction"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-up-pre-tax-deductions/set-up-a-roth-401k-deduction"
---

# Set Up a Roth 401(k) Deduction

Instructions for setting up a Roth 401(k) after-tax deduction, along with other required setup steps.
Prior to creating a Roth 401(k)
 deduction, you must set up a pre-tax deduction group; the system uses the group to apply
 limits across multiple 401(k) deductions. For more information, see [Set up a Pre-Tax Deduction Group](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-a-pre-tax-deduction-group).
 These instructions include specifying the earnings to which the 401(k) deduction applies, setting up employee-specific elections for the deduction, and guidance making the deduction pretax for employees.To view a tutorial, see [Vista Payroll Setup](https://academy.viewpoint.com/learn/course/external/view/elearning/2353/VistaPayrollSetup) in the Trimble Construction Academy

1. Open the PR Deductions/Liabilities form and select the New Record icon.

1. In the Dedn / Liab Code field, enter an unused number.

1. In the Description field, enter a description.

1. In the Type field, select Deduction.

1. In the Calculation Category field, select E-Employee .

1. In the GL Account field, press F4 to select the appropriate GL liability account.

1. In the Method field, select A-Amount .

1. In the Rate / Amount #1 and Rate / Amount #2 fields, enter 0.00000.

1. In the Limit section, select the No Limit option.

1. Select the Accumulate subject amounts checkbox.

1. Select the Pre-Tax Deduction checkbox.Note: Although this is an after-tax deduction, you need to select this checkbox to enable the Pre-Tax Group field. The system uses the specified Pre-Tax Group to determine the standard annual contribution limit.

1. In the Pre-Tax Group field, press F4 to select a pre-tax group.

1. If you want the deduction amounts to update automatically to an Accounts Payable invoice, select the Automatic Update to Accounts Payable checkbox on the Addl Info tab.

1. Add applicable codes to the basis of the deduction.The system bases the employee 401(k) contribution amounts on the earnings codes you add to the basis of the deduction. Add codes to the basis using one of the following methods:
OptionDescription
Add basis codes manually

1. Select the Basis Codes tab.

1. In the EDL Type field, select E-Earnings, D-Deduction, or L-Liability.

1. In the EDL Code field, enter the code or press F4 to select from a list of valid codes.

1. Add any other applicable EDL codes to the basis.

Add multiple basis codes

1. Select Add Basis Codes. The PR Add DL Basis Codes form displays.

1. In the Basis Codes section, select one of the following:

- Copy basis codes from another DL Code - Select this option to copy the basis codes from an existing deduction or liability code. Then using the DL Code to Copy From field, enter the deduction or liability code or press F4 to select from a list of existing codes.

- Add all eligible Earnings and DL Codes to basis - Select this option to apply all existing eligible earnings, deductions, and liability codes as the basis.

1. Select Add.

1. In Basis Codes grid, delete any individual earnings, deduction, or liability codes that do not apply.

1. Enter employee-specific elections for the Roth 401(k) deduction.

1. Open the PR Employee Dedns / Liabs form and select the New Record icon.

1. In the Employee field, enter the employee or press F4 to select an employee.

1. In the Dedn / Liab Code field, enter the Roth 401(k) deduction code or press F4 to select the deduction code.

1. Select the Employee-Based checkbox.

1. In the Frequency field, enter the applicable frequency code or press F4 to select from a list of valid frequency codes.

1. In the Processing Seq# field, enter a number to indicate the order in which this deduction should be calculated. Important: When an employee has both 401(k) and Roth deductions, it is suggested that you assign different processing sequences to each. Be mindful that the processing sequence chosen can affect, or be affected by, other deductions like garnishments. For more information, see the [Processing Seq#](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employee-dednsliabs-form/field-definitions-pr-employee-dednsliabs-form#ID-000377a2--en) F1 Help.

1. In the Calculations section select one of the following:

- If the employee election is a set amount, select Override Standard Rate/Amount and enter the amount in the Rate / Amount field.

- If the employee election is a percentage, select Override Method - Use Rate of Gross and enter the rate as a decimal in the Rate / Amount field.

Important: Do not select Override Standard Limit as a method to override 401(k) limits. The pre-tax deduction group determines the limit. If you need to accommodate employees over age 50 who wish to withhold amounts beyond the normal limit, see [Setting up a catch-up 401(k) Deduction](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-up-pre-tax-deductions/set-up-a-catch-up-401k-deduction).

1. Repeat the steps above for each applicable employee.

Related information

- [Set Up a Standard 401(k) Deduction](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-up-pre-tax-deductions/set-up-a-standard-401k-deduction)

- [Set Up a Catch-Up 401(k) Deduction](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-up-pre-tax-deductions/set-up-a-catch-up-401k-deduction)

- [PR Pre-Tax Deduction Groups Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-pre-tax-deduction-groups-form)

- [PR Deductions/Liabilities Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-deductionsliabilities-form)

- [Set Up Pre-Tax Deductions](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-up-pre-tax-deductions)

- [PR Employee Dedns/Liabs Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employee-dednsliabs-form)

- [Assigning Deductions and Liabilities](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/assigning-deductions-and-liabilities)
