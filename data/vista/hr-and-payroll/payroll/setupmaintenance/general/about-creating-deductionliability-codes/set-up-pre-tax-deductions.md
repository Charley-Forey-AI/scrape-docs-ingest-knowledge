---
title: "Set Up Pre-Tax Deductions | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-up-pre-tax-deductions"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-up-pre-tax-deductions"
---

# Set Up Pre-Tax Deductions

You can use the PR Deductions/Liabilities form to set up deduction codes for any pre-tax salary reduction plans. Some examples of pre-tax salary reduction plans are health insurance premiums, 401(k) and cafeteria plans for U.S. users, and pre-tax union dues for Canadian users.
Prior to creating a pre-tax deduction, you must set up a pre-tax deduction group. The system uses the group to apply limits across multiple deductions. For more information, see [Set up a Pre-Tax Deduction Group](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-a-pre-tax-deduction-group).
Setting up pre-tax deduction codes is very similar to creating a standard deduction code, but there are a few differences in how you implement them in the system.
For detailed information about setting up pre-tax deductions for 401(k) and Roth, see [Set Up a Standard 401(k) Deduction](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-up-pre-tax-deductions/set-up-a-standard-401k-deduction) and [Set Up a Roth 401(k) Deduction](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-up-pre-tax-deductions/set-up-a-roth-401k-deduction).
To set up other pre-tax deductions:

1. [Create a deduction code](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/create-deduction-and-liability-codes) in PR Deductions/Liabilities for the pre-tax deduction. In particular, keep these steps in mind:

1. Keep pre-tax deductions separate from other deductions.

1. Set the Calculation Category to E-Employee.

1. Set the Method field to A-Amount or G-Rate of gross.

1. Do not enter an amount in the Amount field in the Limit section. The limit for this deduction code is determined by the pre- tax deduction group.

1. Select the Pre-Tax Deduction checkbox.

1. In the Pre-Tax Group field, enter the appropriate pre-tax deduction group number. When multiple deductions require a combined annual limit, use the same pre-tax deduction group for all.

1. [Assign the pre-tax deduction code to the calculation basis](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/about-determining-the-calculation-basis-for-deduction-and-liability-codes) for all applicable deduction codes. By assigning pre-tax deductions to the Basis Codes tab in PR Deductions/Liabilities, you ensure that the pre-tax deduction is not included in calculating the basis of the standard deduction code.

1. [Associate the pre-tax deduction code with all applicable earnings codes](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/associate-deductions-and-liabilities-with-earnings-codes) in PR Earnings Codes. Note: You must associate pre-tax deductions with earnings codes to ensure the system processes payroll correctly.

Related information

- [PR Pre-Tax Deduction Groups Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-pre-tax-deduction-groups-form)

- [PR Deductions/Liabilities Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-deductionsliabilities-form)

- [PR Earnings Codes Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-earnings-codes-form)
