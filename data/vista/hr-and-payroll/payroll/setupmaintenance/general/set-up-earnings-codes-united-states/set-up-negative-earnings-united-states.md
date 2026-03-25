---
title: "Set Up Negative Earnings: United States | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-earnings-codes-united-states/set-up-negative-earnings-united-states"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-earnings-codes-united-states/set-up-negative-earnings-united-states"
---

# Set Up Negative Earnings: United States

You can use the PR Earnings Code form to set up negative earnings.
Note: While you can set up salary reductions as
 negative earnings, it is recommended that you set up salary reductions as pre-tax
 deductions. For more information, see [Setting Up Pre-Tax Deductions](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-up-pre-tax-deductions).
 Negative earnings can represent
 earnings reductions (e.g., 401(k) and cafeteria plans). For example, many salary
 reductions lower federal taxable wages and federal income tax, as well as state
 taxable wages and state income tax. Other salary reductions lower federal and state
 in this same manner, but also reduce FICA Social Security and FICA Medicare wages
 and taxes for both the employee deductions and employer liabilities (Section 125
 plan).
Because these plans are typically either
 a percentage of earnings per pay period or a flat amount, it is often convenient to
 set them up as Automatic Earnings in PR Automatic Earnings instead of making an
 entry in PR Timecard Entry each time. You can also specify the limit of the salary
 reduction using PR Automatic Earnings. Always remember to use negativerates or
 amounts and limits. To determine the taxability of salary reduction plans, consult
 your plan administrator, appropriate tax laws, or insurance and craft
 requirements.
To process negative earnings/salary
 reductions for a current payroll, run the [PR Post Auto Earnings](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/about-the-pr-post-auto-earnings-form) form.
This topic discusses how to set up
 negative earnings codes. See [Setting Up Earnings Codes: United States](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-earnings-codes-united-states) for more information on setting
 up true earnings codes.
Note: These instructions are provided for
 informational and sample setup purposes only. Consult your plan administrator or
 appropriate tax laws to determine whether these types of salary reductions plans
 reduce specific deductions and liabilities.

1. In the Earnings
 Code field, enter a number that uniquely identifies the earnings
 code. Note: The numbers you assign to earnings codes
 determine the sequence in which the system processes earnings. See [Determining Earnings Code Sequences](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-earnings-code-sequences) for
 more information.
Important: The code number should be a higher
 number than any earnings that the negative earnings would be based
 on.

1. Enter a description of
 the earnings code in the Description field.

1. From the Method drop-down, select the method the system users to
 calculate earnings. See [Determining Earnings Code Calculation Methods](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/earnings-code-calculation-methods) for more information.


1. In the Factor field, enter the number that the system multiplies the
 rate by for calculating this earnings code. Typically, you will enter a factor
 of 1.0.

1. Check the Include in
 Liability Distributions box to have the system include the
 earnings code in liability distributions to the job. If you do not check this
 box, the system does not distribute the earnings to the job, but the payroll
 department associated with the employee (PR Employees) receives the benefit. Do
 this if you want to reduce job expenses.

1. In the Earnings
 Type field, enter the earnings type that determines the GL
 account that the system expenses when updating earnings to GL. Press F4 for a
 list of available earnings types. See [HQ Earn Types](/en/vista/vista/administration/headquarters/payroll-related-setup/about-the-hq-earn-types-form) for more information.

1. In the JC Cost
 Type field, enter the cost type the system uses for interfacing
 earnings to JC. Press F4 for a list of available
 cost types.

1. Use the Limit
 Period field to select a limit for the earnings code. This limit
 determines how often the system resets the limit for this earnings code. 

1. In the Limit
 Amount field, enter the limit amount for automatic earnings.
 Make sure to enter a negative number to calculate the salary reduction
 appropriately.

1. Check the Include Detail
 on Certified Reports box if you want to include these earnings
 on their own detail line when you run the PR Certified Payroll Transcript or PR
 Certified Payroll Transcript With Class Info reports. Note: If you do not check this box, the system
 summarizes this earnings code in the “Other Taxable” or “Other Non-Taxable”
 fields on these reports.

1. In the Fringe Benefit
 Type field, select the fringe benefit classification to use with the LCPtracker or eMars reports. Based on the type selected, the system places the appropriate rates/amounts in the corresponding report fields.

1. Set up automatic updates to AP, as necessary. See [Setting Up Automatic AP Updates](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-earnings-codes-united-states/set-up-automatic-ap-updates-united-states) for more information.

1. Set up deductions and liabilities for this earnings code. See [Associating Deductions and Liabilities with Earnings Codes ](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/associate-deductions-and-liabilities-with-earnings-codes)for more information.

1. Save the record.

1. In [PR Automatic Earnings](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-automatic-earnings-form), set up the negative earnings code. Enter the rate/amount and limit as negative numbers. Because these earnings are generally not posted to a job or phase, or apply to insurance, leave those fields blank.
