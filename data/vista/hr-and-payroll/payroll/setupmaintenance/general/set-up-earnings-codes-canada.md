---
title: "Set up Earnings Codes: Canada | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-earnings-codes-canada"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-earnings-codes-canada"
---

# Set up Earnings Codes: Canada

Use the PR Earnings Codes form to set up earnings codes, which identify and categorize types of earnings (for example, hourly, salary, double time, and so on).
Note: You can also use this form to set up negative earnings codes for salary reductions (for example, Registered Retirement Savings Plans). For more information, see [Setting Up Negative Earnings: Canada](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-earnings-codes-canada/set-up-negative-earnings-canada). The preferred way to set up salary reductions is to use pre-tax deductions. For more information on this method, see [Setting Up Pre-Tax Deductions](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-up-pre-tax-deductions).

To set up earnings codes:

1. In the PR Earnings Codes form, in the Earnings
 Code field, enter a number that uniquely identifies the earnings
 code.Note: The numbers you assign to earnings codes
 determine the sequence in which the system processes earnings. See [Determining Earning Code Sequences](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-earnings-code-sequences) for more information.

1.  In the Description field, enter a description of
 the earnings code.

1. From the Method drop-down, select the method the system users to
 calculate earnings. See [Determining Earnings Code Calculation Methods](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/earnings-code-calculation-methods) for more information.Note: If you select L-Allowance:

- on the Subject Earnings tab, enter the
 earnings codes that are subject to this allowance

- save the record

- skip all remaining steps.

1. In the Factor field, enter the number that the system multiplies the
 rate by for calculating this earnings code. Note: When entering the factor, enter time in
 increments of 0.5. For example, use 0.5 for half time, 1.0 for regular time,
 1.5 for time and a half, 2.0 for double time, and so on. Earnings codes with
 a factor greater than 1 are considered premium time on cost reports.

1.  If this earnings code should be included in
 the basis amount for calculating automatic earnings (for example, salary or
 RRSP), select the Subject to Auto
 Earnings checkbox.

1.  If this
 earnings code should be included in the basis amount for calculating craft and class add-on
 earnings (for example, vacation add-ons), select the Subject to
 Craft/Class Add-ons checkbox.

1. If you want this earnings code to
 be considered a true earnings on the PR Certified Payroll Transcript, PR
 Certified Payroll Transcript With Class Info, and JC Cost reports, select the True Earnings
 for Payroll Reports checkbox. The system
 disables the Include in Liability
 Distributions checkbox.
Note: Do not select this checkbox for negative
 earnings codes (earnings reductions). In this case, the earnings code
 displays as a deduction on the specified report.

1. Select the Include in OT
 Calculations checkbox to include this earnings code in
 determining the basis for overtime calculations.Note: This checkbox is disabled for factors
 greater than 1.0.

1. If you selected A-Amount
 from the Method drop-down, select the Include in
 Salary Distribution Calculations checkbox to include this
 earnings code in determining salaried earnings. Note: If you select this checkbox and use
 this code to post hours by job, equipment, or account, the salaried
 employee’s pay rate and amount default to zero. When you process the PR
 Salary Distribution form, the system calculates the correct rate and amount.
 For more information, see [About the PR Salary Distribution Form](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/about-the-pr-salary-distribution-form).

1. If you want foremen or
 employees to be able to use this earnings code when entering timesheets in the PR My
 Timesheet form, select the Include in Remote Timesheet
 Entry checkbox. See [Entering Timesheets](/en/vista/vista/hr-and-payroll/payroll/time-entry/timesheets/entering-timesheets) for more information.

1. In the Earnings
 Type field, enter the earnings type that determines the GL
 account that the system expenses when updating earnings to GL. Press F4
to select from a list of available earnings types. See [About the HQ Earn Types Form](/en/vista/vista/administration/headquarters/payroll-related-setup/about-the-hq-earn-types-form) for more information.

1. In the JC Cost
 Type field, enter the cost type the system uses for interfacing
 earnings to JC. Press F4 to select from a list of available
 cost types.

1. [Set up automatic updates to Accounts Payable](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-earnings-codes-canada/set-up-automatic-ap-updates-canada).

1. If this earnings code should be reported on the Record of Employment report, set up the appropriate [separation payment](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-earnings-codes-canada/set-up-separation-payments) or [special payment](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-earnings-codes-canada/set-up-special-payments-earnings-codes) information.

1. [Associate deductions and liabilities with the earnings code](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/associate-deductions-and-liabilities-with-earnings-codes).

1. Save the record.

Related information

- [PR Occupational Categories Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-occupational-categories-form)

- [Set Up Negative Earnings: Canada](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-earnings-codes-canada/set-up-negative-earnings-canada)

- [PR Earnings Codes Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-earnings-codes-form)

- [About the HQ Earn Types Form](/en/vista/vista/administration/headquarters/payroll-related-setup/about-the-hq-earn-types-form)

- [About the PR Salary Distribution Form](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/about-the-pr-salary-distribution-form)

- [About Earnings Code Sequences](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-earnings-code-sequences)

- [About Syncing Payroll with the General Ledger](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/about-syncing-payroll-with-the-general-ledger)

- [Job Cost Interface](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/about-syncing-payroll-to-job-cost/job-cost-interface)

- [About Payroll Allowances](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-payroll-allowances)

- [Earnings Code Calculation Methods](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/earnings-code-calculation-methods)
