---
title: "Set Up Death Benefit ETPs | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/payg-payment-summaries/process-etps-australia/types-of-automatic-payments-for-terminated-employees/set-up-death-benefit-etps"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/payg-payment-summaries/process-etps-australia/types-of-automatic-payments-for-terminated-employees/set-up-death-benefit-etps"
---

# Set Up Death Benefit ETPs

Prior to processing death benefit ETPs, you must create an earnings code as well as a deduction code for taxation purposes.
Once you have set up these codes, you can then manually process a timecard record for this type of payment.
Important: The system calculates taxation based only on payments made to the employee's dependents.

To set up an earnings and deduction code for death benefit ETPs:

1. In the PR Earnings Codes form, create an earnings code for the death benefit ETP. On the Addl Info tab, from the
 ATO Category
 drop-down, select













 ETPD - Employment Termination, Death. For more information, see [Set Up Earnings Codes: Australia](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-earnings-codes-australia).

1. In the PR Deductions / Liabilities form, create a deduction code for taxation purposes. When creating the code, use the following settings:

1. On the Info tab, select









 R-Routine from the









 Method field and enter









 ETPMargina in the









 Routine field.

1. On the Addl Info tab, select









 Tax Withheld ETP Death from the









 ATO Category field.

1. Enter the corresponding earnings code(s) on the Basis Codes tab.Important: In order for the ETP deduction to be calculated during payroll processing, you must also enter this deduction code in the DLCode column of the PR Federal Info form (Add'l Federal Based Dedns/Liabs tab).

For more information, see [Create Deduction and Liability Codes](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/create-deduction-and-liability-codes).

You can now manually process timecard records for death benefit ETPs. When you do:

- The system removes any applicable non-taxable invalidity
 portion based on the employee's years of service and wages lost through retirement
 age.

- The system removes any applicable non-taxable portion for the employee's term of service prior to 1 July 1983.

- Any remaining amount is taxed based upon the preservation age and the ETP cap limit (ETP Cap
 field, PR Limits and Rates form).

- If there is an amount that exceeds the ETP cap limit, the system taxes this amount using the rate in the
 Excess of Cap Rate
 field (PR Limits and Rates form).

Related concepts

- [Types of Automatic Payments for Terminated Employees](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/payg-payment-summaries/process-etps-australia/types-of-automatic-payments-for-terminated-employees)
