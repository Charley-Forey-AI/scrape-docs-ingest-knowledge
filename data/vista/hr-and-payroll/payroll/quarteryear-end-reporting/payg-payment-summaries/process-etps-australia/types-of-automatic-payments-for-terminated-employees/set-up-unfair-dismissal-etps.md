---
title: "Set Up Unfair Dismissal ETPs | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/payg-payment-summaries/process-etps-australia/types-of-automatic-payments-for-terminated-employees/set-up-unfair-dismissal-etps"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/payg-payment-summaries/process-etps-australia/types-of-automatic-payments-for-terminated-employees/set-up-unfair-dismissal-etps"
---

# Set Up Unfair Dismissal ETPs

Prior to processing early termination payments (ETPs) for unfair dismissal, harassment, personal injury, or
 discrimination, you must create an earnings code as well as a deduction code for taxation
 purposes.
Once you have set up these codes, you can manually
 process a timecard record for this type of payment.To set up an earnings and deduction code
 for unfair dismissal ETPs:

1. In the PR Earnings Codes form, create an earnings code for the unfair dismissal ETP. On the Addl Info tab, from the
 ATO Category
 drop-down, select
 ETPU - Employment Termination, Unfair Dismissal/Harassment/Discrimination. For more detailed information, see [Set Up Earnings Codes: Australia](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-earnings-codes-australia).

1. In the PR Deductions / Liabilities form, create a deduction code for taxation purposes. When creating the code, use the following settings:

1. On the Info tab, from the
 Method
 field, select
 R-Routine
 and enter
 ETPUnfair
 in the
 Routine
 field.

1. On the Addl Info tab, from the
 ATO Category
 field, select
 Tax Withheld ETP Unfair Dismissal.

1. On the Info tab, from the
 Method
 field, select
 R-Routine
 and enter
 ETPUnfair
 in the
 Routine
 field.

1. Enter the corresponding earnings
 code(s) on the Basis Codes tab.

For more information, see [Create Deduction and Liability Codes](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/create-deduction-and-liability-codes).

You can now manually process timecard records for unfair dismissal ETPs. When you do:

- The system removes any applicable non-taxable portion for the employee's term of service prior to 1 July 1983.

- Any remaining amount is taxed based upon the preservation age and the ETP cap limit (ETP Cap
 field, PR Limits and Rates form).

- If there is an amount that exceeds the ETP cap limit, the system taxes this amount using the rate in the
 Excess of Cap Rate
 field (PR Limits and Rates form).

Related concepts

- [Types of Automatic Payments for Terminated Employees](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/payg-payment-summaries/process-etps-australia/types-of-automatic-payments-for-terminated-employees)
