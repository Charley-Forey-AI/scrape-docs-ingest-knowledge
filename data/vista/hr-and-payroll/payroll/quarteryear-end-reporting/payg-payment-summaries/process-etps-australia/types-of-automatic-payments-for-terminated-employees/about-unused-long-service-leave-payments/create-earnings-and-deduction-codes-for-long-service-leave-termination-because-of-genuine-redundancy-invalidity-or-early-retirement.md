---
title: "Create Earnings and Deduction Codes for Long Service Leave: Termination because of Genuine Redundancy, Invalidity, or Early Retirement | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/payg-payment-summaries/process-etps-australia/types-of-automatic-payments-for-terminated-employees/about-unused-long-service-leave-payments/create-earnings-and-deduction-codes-for-long-service-leave-termination-because-of-genuine-redundancy-invalidity-or-early-retirement"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/payg-payment-summaries/process-etps-australia/types-of-automatic-payments-for-terminated-employees/about-unused-long-service-leave-payments/create-earnings-and-deduction-codes-for-long-service-leave-termination-because-of-genuine-redundancy-invalidity-or-early-retirement"
---

# Create Earnings and Deduction Codes for Long Service Leave: Termination because of Genuine Redundancy, Invalidity, or Early Retirement

(Australia only) Steps to create earnings and deduction codes for Long Service Leave.
If you need to make payments to an employee for unused leave, you must create an earnings code for the type of annual leave, and a deduction code for taxation purposes.

1. In the PR Earnings Codes form, create an earnings code. When doing so, select
 LSAR - Leave, Lump Sum A Type R
 from the
 ATO Category
 drop-down on the Addl Info tab. For more detailed instructions, see [Setting Up Earnings Codes: Australia](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-earnings-codes-australia).

1. In the PR Deductions / Liabilities form, create a deduction code for taxation purposes. When creating the code, use the following settings:

- from the
 Method
 field, select
 G-Rate of gross
 and enter the current withholding rate in the
 Rate / Amount #1
 field. Obtain the current rate from the ATO website.

- From the
 ATO Category
 field on the Addl Info tab, select
 Tax Withheld.

- On the Basis Codes tab, enter the corresponding earnings code(s).Note: For more information, see [Creating Deduction and Liability Codes](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/create-deduction-and-liability-codes).

1. For the earnings code you set up in step 1, visit the PR Auto Termination Pay Setup form and enter an ETP type record. For more information, see [Setting Up Automatic Long Service Leave ETPs](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/payg-payment-summaries/process-etps-australia/types-of-automatic-payments-for-terminated-employees/about-unused-long-service-leave-payments/set-up-automatic-long-service-leave-etps).

Note: During processing, the system calculates the tax based on
 all accrual dates that occur after 16 August 1978 using the rate specified for the
 deduction code. If the payment amount is under the amount specified in the

 Leave
 Flat Rate Limit
 field (PR Limits and Rates form), the system doesn't use
 the marginal rates but instead withholds the lesser
 of:

- the standard calculated amount or

- the rate specified in the Leave
 Flat Rate
 field (PR Limits and Rates form).
