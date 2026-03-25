---
title: "Create Earnings and Deduction Codes for Redundancy/Early Retirement ETPs | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/payg-payment-summaries/process-etps-australia/types-of-automatic-payments-for-terminated-employees/about-setting-up-redundancy-etps/create-earnings-and-deduction-codes-for-redundancyearly-retirement-etps"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/payg-payment-summaries/process-etps-australia/types-of-automatic-payments-for-terminated-employees/about-setting-up-redundancy-etps/create-earnings-and-deduction-codes-for-redundancyearly-retirement-etps"
---

# Create Earnings and Deduction Codes for Redundancy/Early Retirement ETPs

(Australia only) Prior to processing ETPs for redundancy, you must create an earnings code as well as a deduction code for taxation purposes.

1. In the PR Earnings Codes form, create an earnings code for the redundancy/early retirement ETP. Select ETPR - Employment Termination Redundancy/Early Retirement from the ATO Category drop-down on the Addl Info tab. For more information, see [Set Up Earnings Codes: Australia](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-earnings-codes-australia).

1. In the PR Deductions / Liabilities form, create a deduction code for taxation purposes. When creating the code, use the following settings:

1. On the Info tab, select R-Routine from the Method field and then enter ETPRedunda in the Routine field

1. On the Add'l Info tab, select Tax Withheld ETP Redundancy from the ATO Category field.

1. On the Basis Codes tab, enter the corresponding earnings codes.

Important: In order for the ETP deduction to be calculated during payroll processing, you must also enter this deduction code in the DLCode column of the PR Federal Info form (Add'l Federal Based Dedns/Liabs tab).

For more information, see [Create Deduction and Liability Codes](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/create-deduction-and-liability-codes).

1. In PR Employment Term Setup, enter an ETP type record in for the earnings code from step 1. For more information, see [Set Up Automatic Redundancy/Early Retirement ETPs](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/payg-payment-summaries/process-etps-australia/types-of-automatic-payments-for-terminated-employees/about-setting-up-redundancy-etps/set-up-automatic-redundancyearly-retirement-etps).

During processing, the system calculates the tax based on the following:

- The system removes the redundancy tax-free portion (as specified in the Redundancy Tax Free Basis field in PR Limits and Rates).

- The system removes any applicable tax-free portion based on the Redundancy Tax Free Years of Service Basis field (PR Limits and Rates) times the employee's years of service.

- The system removes any applicable non-taxable portion for the employee's term of service prior to 1 July 1983.

- The remaining amount is taxed based upon the preservation age and the ETP cap limit (ETP Cap field, PR Limits and Rates).

- If there is an amount that exceeds the ETP cap limit, the system taxes this amount using the rate in the Excess of Cap Rate field (PR Limits and Rates form).
