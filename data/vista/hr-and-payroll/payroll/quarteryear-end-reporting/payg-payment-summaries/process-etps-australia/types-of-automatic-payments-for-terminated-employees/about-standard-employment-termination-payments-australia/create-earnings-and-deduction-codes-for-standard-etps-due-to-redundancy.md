---
title: "Create Earnings and Deduction Codes for Standard ETPs Due to Redundancy | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/payg-payment-summaries/process-etps-australia/types-of-automatic-payments-for-terminated-employees/about-standard-employment-termination-payments-australia/create-earnings-and-deduction-codes-for-standard-etps-due-to-redundancy"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/payg-payment-summaries/process-etps-australia/types-of-automatic-payments-for-terminated-employees/about-standard-employment-termination-payments-australia/create-earnings-and-deduction-codes-for-standard-etps-due-to-redundancy"
---

# Create Earnings and Deduction Codes for Standard ETPs Due to Redundancy

The specific steps for making earnings and deductions codes work for standard redundancy ETPs.
You do not need to complete the steps in this section for unused RDO ETPs.

These steps are only those that are specific to standard ETPs. If you need additional help

- creating an earnings code, please see [Set Up Earnings Codes: Australia](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-earnings-codes-australia).

- creating deduction codes, please see [Create Deduction and Liability Codes](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/create-deduction-and-liability-codes).

1. In the PR Earnings Codes form, create an earnings code for each type of standard ETP due to redundancy/early retirement. When creating the code, use the following setting:

1. In the Addl Info tab, in the ATO Category drop-down, select ETPR - Employment Termination Redundancy/Early Retirement.

1. In the PR Deductions / Liabilities form, create a deduction code for taxation purposes. When creating the code, use the following settings:

1. In the Method field, select R-Routine.

1. In the Routine field, enter ETPRedunda.

1. In the Addl Info tab, in the ATO Category field, select Tax Withheld ETP.In

1.  the Basis Codes tab, enter the corresponding earning(s) code.

Important: In order for the ETP deduction to be calculated during payroll processing, you must also enter this deduction code in the DLCode column of the PR Federal Info form (Add'l Federal Based Dedns/Liabs tab).

1. For ETPs that can be auto-generated, enter an ETP type record in the PR Auto Termination Pay form for the earnings code from step 1. For more information, see [Set Up Automatic Standard ETPs](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/payg-payment-summaries/process-etps-australia/types-of-automatic-payments-for-terminated-employees/about-standard-employment-termination-payments-australia/set-up-automatic-standard-etps).

- The system removes the redundancy tax-free portion (as specified in the Redundancy Tax Free Basis field in the PR Limits and Rates form).

- The system removes any applicable tax-free portion (based on the Redundancy Tax Free Years of Service Basis field in the PR Limits and Rates form) times the employee's years of service.

- The system removes any applicable non-taxable portion for the employee's term of service prior to 1 July 1983.

- The remaining amount is taxed based upon the preservation age and the ETP cap limit (ETP Cap field, PR Limits and Rates form).

- If there is an amount that exceeds the ETP cap limit, the system taxes this amount using the rate in the Excess of Cap Rate field (PR Limits and Rates form).
