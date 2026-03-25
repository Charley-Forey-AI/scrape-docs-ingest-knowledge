---
title: "Create Earnings & Deduction Codes for Annual Leave: Normal Termination | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/payg-payment-summaries/process-etps-australia/types-of-automatic-payments-for-terminated-employees/about-unused-annual-leave-payments/create-earnings--deduction-codes-for-annual-leave-normal-termination"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/payg-payment-summaries/process-etps-australia/types-of-automatic-payments-for-terminated-employees/about-unused-annual-leave-payments/create-earnings--deduction-codes-for-annual-leave-normal-termination"
---

# Create Earnings & Deduction Codes for Annual Leave: Normal Termination

(Australia only) You must create earnings codes for annual leave payments that
 you will make to employees for normal termination, along with corresponding leave loading
 earnings codes and deduction codes for taxation purposes.
 To set up the earnings
 codes and deductions for annual leave, normal termination:

1. In the PR Earnings Codes form, create
 an earnings code. When doing so, select ETPA - Employment Termination, Annual
 Leave from the ATO Category drop-down on the Addl
 Info tab. For more detailed instructions, see [Set Up Earnings Codes: Australia](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-earnings-codes-australia).

1. Create an additional earnings code for leave loading. Select



 ETPA - Employment Termination, Annual Leave from the



 ATO Category drop-down on the Addl Info tab. To create an earnings code for leave loading, you will need to create a payroll routine using a rate of gross. For more information, see [Earnings Based Routines: Australia](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-payroll-routines/earnings-based-routines-australia).

1. In the PR Deductions / Liabilities form, create a deduction code for taxation purposes. When creating the code, use the following settings:

- From the Method field, select R-Routine and enter ETPMargina in the Routine field.

- From the
 ATO Category
 field on the Addl Info tab, select Tax Withheld.

- On the Basis Codes tab, enter the corresponding earnings code(s), including any earnings codes used for leave loading.

Important: In order for the ETP deduction to be calculated during payroll processing, you must also enter this deduction code in the DLCode column of the PR Federal Info form (Add'l Federal Based Dedns/Liabs tab).

1. For the earnings code you set up in step 1, and for the earnings code used for leave loading you set up in step 2, visit the PR Auto Termination Pay Setup form and enter an ETP type record. For more information, see [Setting Up Automatic Long Service Leave ETPs](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/payg-payment-summaries/process-etps-australia/types-of-automatic-payments-for-terminated-employees/about-unused-long-service-leave-payments/set-up-automatic-long-service-leave-etps).

Note: During
 processing, the system calculates the tax based on marginal rates for all accrual
 dates that occur after 17 August 1993. The system will not calculate tax for leave
 accrued prior to 18 August 1993.If the payment amount is
 under the amount specified in the Leave Flat Rate Limit field (PR
 Limits and Rates form) the system does not use the marginal rates calculation but instead withholds the lesser of:

- the standard calculated
 amount or

- the rate specified in the Leave Flat Rate field (PR Limits
 and Rates form).
