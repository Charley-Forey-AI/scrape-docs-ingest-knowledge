---
title: "Set up Earnings Codes: United States | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-earnings-codes-united-states"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-earnings-codes-united-states"
---

# Set up Earnings Codes: United States

You will use the PR Earnings Codes form to set up earnings codes, which identify and categorize types of earnings (such as hourly, salary, double time, etc.).
Note: You can also use this form to set up negative
 earnings codes for salary reductions (for example, 401(k) and cafeteria plans). For more
 information, see [Setting Up Negative Earnings: United States](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-earnings-codes-united-states/set-up-negative-earnings-united-states). The
 preferred way to set up salary reductions is to use pre-tax deductions; for more
 information on this method, see [Setting Up Pre-Tax Deductions](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-up-pre-tax-deductions).
The following instructions detail how to set up earnings codes.

1. In the Earnings
 Code field, enter a number that uniquely identifies the earnings
 code. Note: The numbers you assign to earnings codes
 determine the sequence in which the system processes earnings. For more information, see [About Earnings Code Sequences](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-earnings-code-sequences).

1. In the
 Description field, enter a description of the
 earnings code.

1. In the Method field, select the method the system users to calculate
 earnings. See [Determining Earnings Code Calculation Methods ](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/earnings-code-calculation-methods)for more information.  If you select L-Allowance, skip to the next
 several steps and resume with the instructions about the Earnings
 Type field.

1. In the Factor field, enter the number that the system multiplies the
 rate by for calculating this earnings code. Note: When entering the factor, enter time in
 increments of 0.5. For example, use 0.5 for half time, 1.0 for regular time,
 1.5 for time and a half, 2.0 for double time, and so on. Earnings codes with
 a factor greater than 1 are considered premium time on cost reports.

1. If this earnings code
 should be included in the basis amount for calculating automatic earnings,
 select the Subject to Auto Earnings checkbox. For
 example, salary, 401(k), and section 125 plans.

1. If the system should
 include this earnings code in the basis amount for calculating craft and class
 add-on earnings, select the Subject to Craft/Class
 Add-ons checkbox. For example, vacation add-ons.

1. If this earnings code is
 considered a true earnings on the PR Certified Payroll Transcript, PR Certified
 Payroll Transcript With Class Info, and JC Cost reports, select the
 True Earnings for Payroll Reports checkbox. The
 system disables the Include in Liability Distributions
 checkbox. Note: For negative earnings codes (earnings
 reductions), leave this checkbox unselected. In this case, the earnings
 code displays as a deduction on the specified report. See [Setting Up Negative Earnings: United States](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-earnings-codes-united-states/set-up-negative-earnings-united-states)
 for more information.

1. If you are tracking
 hours for the Affordable Care Act (ACA) on the PR ACA 1095 Employees and HR Look
 Back Analysis reports, select the Track Hours for ACA check
 box.

1. If this earnings code should be included in supplemental wage calculations, select the Supplemental Earnings checkbox. For more information, see [Supplemental Earnings](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-earnings-codes-form/field-definitions-pr-earnings-codes-form#concept-242af983-4b5f-423b-a2b2-0db6c45c0dd2--en).

1. If this earnings code
 should be used in the determining the basis for overtime calculations, select
 the Include in OT Calculations checkbox.Note: The system disables this checkbox for
 factors greater than 1.0.

1. If you selected the
 A-Amount calculation method and you want this
 earnings code included in determining salaried earnings, select the Include in
 Salary Distribution Calculations checkbox.Note: If you select this checkbox and use
 this code to post hours by job, equipment, or account, the salaried
 employee’s pay rate and amount default to zero. When you process the PR
 Salary Distribution form, the system calculates the correct rate and amount.
 For more information, see [PR Salary Distribution](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/about-the-pr-salary-distribution-form).

1. If you want foremen or
 employees to be able to use this earnings code when entering timesheets in PR My
 Timesheet, check the Include in Remote Timesheet
 Entry box. See [Entering Timesheets](/en/vista/vista/hr-and-payroll/payroll/time-entry/timesheets/entering-timesheets) for more information.


1. In the Earnings
 Type field, enter the earnings type that determines the GL
 account that the system expenses when updating earnings to GL. Press F4for a list of available earnings types. See [HQ Earn Types](/en/vista/vista/administration/headquarters/payroll-related-setup/about-the-hq-earn-types-form) for more information.

1. In the JC Cost
 Type field, enter the cost type the system uses for interfacing
 earnings to JC. Press F4 for a list of available
 cost types.

1. In the Limit
 Period and the Limit Amount fields, enter
 values if they apply. Refer to field help for more information.

1. If you want to include
 these earnings on their own detail line when you run the PR Certified Payroll
 Transcript or PR Certified Payroll Transcript With Class Info reports, select
 the Include Detail on Certified Reports checkbox.Note: If you do not select this checkbox, the
 system summarizes this earnings code under the “Other Taxable” or “Other
 Non-Taxable” fields on these reports.

1. In the Fringe Benefit
 Type field, select the fringe benefit classification to use with
 the LCPtracker or eMars reports. Based on the type selected, the system places
 the appropriate rates/amounts in the corresponding report fields.

1. On the Dedn / Liabs tab, associate deductions and liabilities with this earnings code. See [Associating Deductions and Liabilities with Earnings Codes](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/associate-deductions-and-liabilities-with-earnings-codes) for more information.

1. If you selected
 L-Allowance from the Method field, use the Subject
 Earnings tab to enter the earnings codes that are subject to this
 allowance.

1. Save the record.

Related information

- [PR Earnings Codes Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-earnings-codes-form)

- [PR Employees Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employees-form)

- [About Syncing Payroll with the General Ledger](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/about-syncing-payroll-with-the-general-ledger)

- [Job Cost Interface](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/about-syncing-payroll-to-job-cost/job-cost-interface)

- [About Payroll Allowances](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-payroll-allowances)
