---
title: "Set Up Earnings Codes: Australia | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-earnings-codes-australia"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-earnings-codes-australia"
---

# Set Up Earnings Codes: Australia

Use the PR Earnings Codes form to set up earnings codes, which identify and categorize types of earnings, for example, hourly, salary, double time, and so on.
You can also use the PR Earnings Codes form to set up allowances, as well as earning codes for leave loading and RDO accruals. For more information, see [Earnings Based Routines: Australia](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-payroll-routines/earnings-based-routines-australia).
To set up earnings codes:

1. In the Earnings
 Code field, enter a number that
 uniquely identifies the earnings codeNote: The numbers you assign to earnings codes
 determine the sequence in which the system processes earnings. See [About Earnings Code Sequences](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-earnings-code-sequences) for more information.


1. In the Description field, enter a description of
 the earnings code.

1. From the Method drop-down, select the method the
 system uses to calculate earnings. See [Earnings Code Calculation Methods](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/earnings-code-calculation-methods)
 for more information.

1. In the Factor field, enter the number that the system multiplies the
 rate by when calculating this earnings code.Note: When entering the factor, enter time in
 increments of 0.5. For example, use 0.5 for half time, 1.0 for regular time,
 1.5 for time and a half, 2.0 for double time, and so on. Earnings codes with
 a factor greater than 1 are considered premium time on cost reports.

1. If this earnings code should be included in the
 basis amount for calculating automatic earnings, select the Subject to Auto
 Earnings checkbox. Example: salary.

1. If the system should include this
 earnings code in the basis amount for calculating craft and class add-on
 earnings, select the Subject to
 Craft/Class Add-ons checkbox . Example: vacation add-ons.

1. If you want this earnings code to be
 considered a true earnings on the PR Certified Payroll Transcript, PR Certified
 Payroll Transcript With Class Info, and JC Cost reports, select the True Earnings
 for Payroll Reports checkbox.

1. Tto include this earnings code in determining
 the basis for overtime calculations, select the Include in OT
 Calculations checkbox.Note: This checkbox is disabled for factors
 greater than 1.0.

1. If you selected
 A-Amount from the Method drop-down, and if you want the
 system to include this earnings code in determining salaried earnings, select the
 Include in Salary Distribution Calculations checkbox.Note: If you select this checkbox and use this code
 to post hours by job, equipment, or account, the salaried employee’s pay
 rate and amount default to zero. Once you process the PR Salary Distribution
 form, the system calculates the correct rate and amount. For more
 information, see [About the PR Salary Distribution Form](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/about-the-pr-salary-distribution-form).

1. If you want foremen or
 employees to be able to use this earnings code when entering timesheets in the PR My
 Timesheet form, select the Include in Remote Timesheet
 Entry checkbox. See [Entering Timesheets](/en/vista/vista/hr-and-payroll/payroll/time-entry/timesheets/entering-timesheets) for more information.


1. In the Earnings
 Type field, enter the earnings type that determines the GL
 account that the system expenses when updating earnings to GL. Press F4 to select from a list. See [About the HQ Earn Types Form](/en/vista/vista/administration/headquarters/payroll-related-setup/about-the-hq-earn-types-form) for more information.

1. In the JC Cost
 Type field, enter the cost type the
 system should use for interfacing earnings to JC. Press F4 to select from a list.

1. On the Additional Info
 tab, select the Australian Taxation Office category for this earnings code from
 the ATO
 Category drop-down, if necessary.

- If you select ATO Category AT - Allowance
 Taxable or ANT - Allowance Non-Taxable, then select the
 appropriate type from the Allowance Type drop-down.

- If you select Allowance Type O - Other from the
 Allowance
 Type drop-down, then select the appropriate type from
 the Other Allowance
 Type drop-down.

- Finally, if these earnings should be included within
 calculations of employee gross earnings for STP Phase 1 reporting (PAYG Items
 'INBGross' and 'HolidayGross'), select the Include in STP Gross
 Amounts checkbox.

1. For STP Phase 2 only, set up the following:

1. If you want to include earnings posted to this earnings code when calculating gross amounts for an employee, select the Include in Employee Gross Amount calculation checkbox.

1. If you want to include earnings posted to this earnings code when calculating reportable fringe benefit amounts for an employee, select the Include in Reportable Fringe Benefits Amount (RFBA) calculation checkbox.

1. From the STP Category drop-down, select the appropriate category (if any) for STP Phase 2 reporting of this earnings code.Depending on the option you select, other fields in the STP Phase 2 section are enabled. See steps below.

1. If you selected LSE as the STP Category, use the Lump Sum E Financial Year field to enter the prior financial year (YYYY) to which the arrears payment applies for this earnings code.

1. If you selected AT or ANT as the STP Category, use the Allowance Code drop-down to select the allowance code for STP Phase 2 reporting of this earnings code.

1. If you selected OD as the Allowance Code, use the Other Allowance Code drop-down to select the other allowance code for STP Phase 2 reporting of this earnings code.

1. Associate deductions and liabilities with this earnings code. See [Associate Deductions and Liabilities with Earnings Codes](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/associate-deductions-and-liabilities-with-earnings-codes) for more information.

1. If you selected
 L-Allowance from the Method field, enter the
 earnings codes that are subject to this allowance on the Subject Earnings tab.If you selected R-Routine from the Method field, enter the
 earnings codes that are subject to this earnings on the Subject Earnings
 tab.

1. Save the record.

Related information

- [PR Allowance Rule Sets Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-allowance-rule-sets-form)

- [PR Earnings Codes Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-earnings-codes-form)

- [About the PR Salary Distribution Form](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/about-the-pr-salary-distribution-form)

- [Job Cost Interface](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/about-syncing-payroll-to-job-cost/job-cost-interface)

- [About the HQ Earn Types Form](/en/vista/vista/administration/headquarters/payroll-related-setup/about-the-hq-earn-types-form)

- [About Syncing Payroll with the General Ledger](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/about-syncing-payroll-with-the-general-ledger)
