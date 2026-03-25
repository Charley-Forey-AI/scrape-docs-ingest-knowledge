---
title: "Setting Up Liability Codes for Superannuation | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/superannuation/set-up-superannuation/setting-up-liability-codes-for-superannuation"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/superannuation/set-up-superannuation/setting-up-liability-codes-for-superannuation"
---

# Setting Up Liability Codes for Superannuation

(Australia only) For each superannuation fund that you offer to employees, you must set up a corresponding liability code.
This page provides instructions specific to setting up a liability code for calculating superannuation fund amounts. If you want a more general description of creating liability codes, see [Create Deduction and Liability Codes](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/create-deduction-and-liability-codes).

The system uses this liability code to determine what amount you will need to pay on behalf of your employee. For more information, see [Superannuation: Australia](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/superannuation/set-up-superannuation).

1. In the PR
 Deductions/Liabilities form, enter a code number in the Dedn/Liab
 Code field and enter a description of the code/fund in the
 Description field.

1. In the Type section of the form, select the Liability radio button and enter the type in the Liability
 Type field. Press F4 to select from a list of liability types.

1. Set the Calculation
 Category drop-down to E-Employee.

1. Set the method of calculation:

- If you want the system to use a routine to calculate
 the liability, select R-Routine from the
 Method drop-down and
 specify the SuperMin routine in
 the Routine field. When
 you use a routine, you ensure that the system takes into account the
 monthly earnings threshold amount when determining your liability
 amount.

- If you want the system to calculate superannuation
 at the standard rate, without regard to the monthly earnings threshold,
 select G-Rate of Gross from
 the Method drop-down.

1. In the Rate/Amount #1 and Rate/Amount
 #2 fields, enter the standard
 superannuation rate.Note: If you are paying an employee a
 superannuation rate that is higher than the standard percentage rate, create a second liability code for the percentage amount over
 the standard rate. For example, if the standard percentage rate for
 superannuation is 9%, and you wish to give an employee 12%, you would first
 create a liability code for the 9% and a second one for 3%.

1. In the Limit section of the form, select the Subject
 Amount radio button.The system enables the Amount and the Applied fields.

1. In the Amount field, enter the maximum quarterly contribution base for
 the current tax year.

1. Set up automatic AP
 updates for the code, making sure to select the Separate AP
 transaction per Employee checkbox. For more information, see [Set Automatic Accounts Payable Updates for D/L Codes](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-automatic-accounts-payable-updates-for-dl-codes).

1. On the Addl Info tab,
 select Superannuation from the ATO Category drop-down. If
 you are creating a second liability code for additional superannuation payments
 (over the standard rate), select Superannuation-Extra from the
 ATO
 Category drop-down.The system enables the Fund field.

1. In the Fund field, enter the superannuation
 fund identification number or press
 F4 to select from a list of funds.

1. If you are using a
 weekly minimum for superannuation, enter the amount in the Superannuation
 Weekly Minimum field. For more information, see [Set Weekly Minimums for Superannuation](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/superannuation/set-up-superannuation/set-weekly-minimums-for-superannuation).


1. Determine the calculation basis for the liability code that is needed to determine the ordinary time earnings. For more information, see [About Determining the Calculation Basis for Deduction and Liability Codes](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/about-determining-the-calculation-basis-for-deduction-and-liability-codes).

1. If an employee wants to contribute additional superannuation amounts, you must set up deduction codes properly to ensure that the amounts are reported correctly on PAYG payment summaries and Super contribution files. Use the steps above, with these considerations:

- For pre-tax deductions for salary sacrifice, check
 the Pre-Tax Deduction box
 (Info tab) and select S-Superannuation from
 the ATO Category
 drop-down (Addl Info tab).

- For after-tax deductions, select SE-Superannuation-Extra from the ATO
 Category drop-down (Addl Info tab).

Related information

- [Set Up Superannuation](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/superannuation/set-up-superannuation)

- [PR Deductions/Liabilities Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-deductionsliabilities-form)

- [About the HQ Super Funds Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/superannuation/about-the-hq-super-funds-form)
