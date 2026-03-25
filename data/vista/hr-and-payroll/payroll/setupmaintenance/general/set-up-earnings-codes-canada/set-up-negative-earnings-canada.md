---
title: "Set Up Negative Earnings: Canada | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-earnings-codes-canada/set-up-negative-earnings-canada"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-earnings-codes-canada/set-up-negative-earnings-canada"
---

# Set Up Negative Earnings: Canada

You can use the PR Earnings Codes form to set up negative earnings. Negative earnings serve as earnings reductions (for example, Registered Retirement Savings Plans).
This topic discusses how to set up negative earnings codes. For more information on setting up true earnings codes, see [Setting Up Earnings Codes: Canada](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-earnings-codes-canada).
Note: While you can set up salary reductions as negative earnings, it is recommended that you set up salary reductions as pre-tax deductions. For more information, see [Setting Up Pre-Tax Deductions](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-up-pre-tax-deductions).
To determine the taxability of salary reduction plans, consult your plan administrator, appropriate tax laws, or insurance and craft requirements.

To set up negative earnings:

1. In the PR Earnings Codes form, in the Earnings
 Code field, enter a number that uniquely identifies the earnings
 code.Note: The numbers you assign to
 earnings codes determine the sequence in which the system processes
 earnings. See [Determining Earnings Code Sequences](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-earnings-code-sequences) for
 more information.

1.  In the Description field, enter a description of
 the earnings code.

1. From the Method drop-down, select the method the system users to
 calculate earnings. See [Determining Earnings Code Calculation Methods](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/earnings-code-calculation-methods) for more information.

1. In the Factor field, enter the number that the system multiplies the
 rate by for calculating this earnings code.Typically, you will enter a factor
 of 1.0.

1. Select the Include in
 Liability Distributions checkbox to have the system include the
 earnings code in liability distributions to the job.If you do not select this check this
 box, the system does not distribute the earnings to the job, but the payroll
 department associated with the employee (PR Employees form) receives the benefit. Do
 this if you want to reduce the job expenses.

1. In the Earnings
 Type field, enter the earnings type that determines the GL
 account that the system expenses when updating earnings to GL. Press F4 to select from a list of available earnings types. See [About the HQ Earn Types Form](/en/vista/vista/administration/headquarters/payroll-related-setup/about-the-hq-earn-types-form) for more information.

1. In the JC Cost
 Type field, enter the cost type the system uses for interfacing
 earnings to JC. Press F4 to select from a list of available
 cost types.

1. Use the Limit
 Type drop-down to select a limit type for the earnings code.The system enables the Limit for Auto Earnings field.
Note: The limit type determines how
 often the system resets the limit for this earnings code.

1. In the Limit for Auto
 Earnings field, enter the limit amount for automatic earnings.
 Enter a negative number to calculate the salary reduction
 appropriately.

1. [Set up automatic updates to AP](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-earnings-codes-canada/set-up-automatic-ap-updates-canada), as necessary.

1. Determine whether the earnings code needs to be reported on the Record of Employment report. For more information, see [Determining ROE Settings for Earnings Codes](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-earnings-codes-form/field-definitions-pr-earnings-codes-form#ID-00037064--en).

1. [Associate deductions and liabilities with this earnings code](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/associate-deductions-and-liabilities-with-earnings-codes).

1. Save the record.

To process negative earnings/salary reductions for a current payroll, run the PR Post Auto Earnings form.
