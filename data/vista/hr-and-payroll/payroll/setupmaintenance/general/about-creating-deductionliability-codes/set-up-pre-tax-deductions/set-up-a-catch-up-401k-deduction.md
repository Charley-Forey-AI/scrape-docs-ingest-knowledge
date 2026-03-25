---
title: "Set Up a Catch-Up 401(k) Deduction | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-up-pre-tax-deductions/set-up-a-catch-up-401k-deduction"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-up-pre-tax-deductions/set-up-a-catch-up-401k-deduction"
---

# Set Up a Catch-Up 401(k) Deduction

Instructions for setting up a catch-up 401(k) pre-tax deduction, commonly used to accommodate employees over age 50 who wish to withhold amounts beyond the normal limit.
Prior to creating a 401(k) deduction, you must set up a
 pre-tax deduction group. The system uses the group to apply limits across multiple
 401(k) deductions. For more information, see [Set up a Pre-Tax Deduction Group](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-a-pre-tax-deduction-group) .
 These instructions include specifying the earnings to which the 401(k) deduction applies, setting up employee-specific elections for the deduction, and guidance making the deduction pretax for employees.To view a tutorial, see [Vista Payroll Setup](https://academy.viewpoint.com/learn/course/external/view/elearning/2353/VistaPayrollSetup) in the Trimble Construction Academy.
Important: The Secure 2.0 Act allows for an increased catch-up limit for employees in a specified minimum/maximum age range. The increased limit and age requirements are designated in PR Pre-Tax Deduction Groups; however, there is no need to set up a separate deduction code for this catch-up deduction. The system automatically applies the second catch-up limit when the employee reaches the specified age range. For more information, see [PR Pre-Tax Deduction Groups Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-pre-tax-deduction-groups-form).

1. Open the PR Deductions/Liabilities form and select the New Record icon.

1.  In the Dedn / Liab Code field, enter an unused number.

1.  In the Description field, enter a description.

1. In the Type field, select Deduction.

1. In the Calculation Category field, select E-Employee .

1. In the GL Account field, press F4 to select the appropriate GL liability account.

1. In the Method field, select A-Amount .

1. In the Rate / Amount #1 and Rate / Amount #2 fields, enter 0.00000.

1. In the Limit section, select the Calculated Amount option.

1. The Amount field defaults to 0.00; accept the default. The catch-up limit is specified in the PR Pre-Tax Deduction Groups form.

1. In the Applied field, select  A-Annually.

1. Select the Accumulate subject amounts checkbox.

1. Select the Pre-Tax Deduction checkbox.

1. Select the Catch up Deduction checkbox.

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

1. Enter employee-specific elections for the 401(k) catch-up deduction.

1. Open the PR Employee Dedns / Liabs form and select the New Record icon.

1. In the Employee field, enter the employee or press F4 to select an employee.

1. In the Dedn / Liab Code field, enter the 401(k) catch-up deduction code or press F4 to select the deduction code.

1. Select the Employee-Based checkbox.

1. In the Frequency field, enter the applicable frequency code or press F4 to select from a list of valid frequency codes.

1. In the Processing Seq# field, enter a number to indicate the order in which this deduction should be calculated. Important: The processing sequence assigned to catch-up deductions should match the processing sequence assigned to the standard deduction. For example, if you assign processing sequence #1 to the 401(k) deduction, you would assign processing sequence #1 to the 401(k) catch-up deductions. For more information, see [Processing Seq#](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employee-dednsliabs-form/field-definitions-pr-employee-dednsliabs-form#ID-000377a2--en).

1. In the Calculations section select one of the following:

- If the employee election is a set amount, select Override Standard Rate/Amount and enter the amount in the Rate / Amount field.

- If the employee election is a percentage, select Override Method - Use Rate of Gross and enter the rate as a decimal in the Rate / Amount field.

Important: Do not select Override Standard Limit as a method to override 401(k) limits. The pre-tax deduction group determines the limit.

1. Repeat the steps above for each applicable employee.

1. Make the Deduction Code Pre-Tax.Since this 401(k) deduction code is pre-tax, you need to add it to the basis for each of the deductions and liabilities where the subject and eligible amount should be reduced by the pre-tax deduction amount.

1. Open the PR Deductions and Liabilities form, select the applicable code, and select the Basis Codes tab.

1. In the EDL Type column, select Deduction.

1. In the EDL Code column, enter the code number for the applicable 401(k) deduction.

1. Repeat steps for each applicable deduction/liability code whose subject and eligible amount should be reduced by the pre-tax deduction amount.

Related information

- [Set Up a Standard 401(k) Deduction](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-up-pre-tax-deductions/set-up-a-standard-401k-deduction)

- [Set Up a Roth 401(k) Deduction](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-up-pre-tax-deductions/set-up-a-roth-401k-deduction)

- [PR Pre-Tax Deduction Groups Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-pre-tax-deduction-groups-form)

- [Set Up Pre-Tax Deductions](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-up-pre-tax-deductions)

- [PR Deductions/Liabilities Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-deductionsliabilities-form)

- [PR Employee Dedns/Liabs Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employee-dednsliabs-form)

- [Assigning Deductions and Liabilities](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/assigning-deductions-and-liabilities)
