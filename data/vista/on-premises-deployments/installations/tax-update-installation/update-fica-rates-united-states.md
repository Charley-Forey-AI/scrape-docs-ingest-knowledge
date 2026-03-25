---
title: "Update FICA Rates: United States | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/on-premises-deployments/installations/tax-update-installation/update-fica-rates-united-states"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/on-premises-deployments/installations/tax-update-installation/update-fica-rates-united-states"
---

# Update FICA Rates: United States

Vista tax updates include changes to various tax routines, including Federal income tax, as well as State/Provincial income taxes). However, each year you must update any rate changes to non-routine deductions and/or liabilities.
An example of this is the FICA SS deduction/liability. Prior to the first payroll run of each calendar year, you must update both your FICA-SS deduction and FICA-SS liability codes to reflect any changes. See IRS Publication 15 for the current year's rates and wage base.
If at any time you process one or more payrolls in a year with the wrong rate(s) or wage base in place, you can correct the amount for the year on the next pay period by selecting the Use YTD accumulations to correct rounding errors checkbox for the deduction code in the PR Deductions/Liabilities form.

When the Use YTD accumulations to correct rounding errors checkbox is selected, during payroll processing the system compares year-to-date accumulations for the deduction or liability against already calculated values and makes corrections as needed. Typical use is with both the FICA deduction and liability, as well as any other EDL code whose calculation period should be the entire calendar year. For more details, see [Use YTD Accumulations to Correct Rounding Errors](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-deductionsliabilities-form/field-definitions-pr-deductions-liabilities-form#ID-00036a89--en).
Important: This checkbox should never be selected for an EDL code that has or could possibly have more than one single effective rate during the year (like SUTA).
