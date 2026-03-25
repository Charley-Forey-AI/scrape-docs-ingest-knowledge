---
title: "About Processing Insurance/Worker's Comp | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/payments/about-processing-insuranceworkers-comp"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/payments/about-processing-insuranceworkers-comp"
---

# About Processing Insurance/Worker's Comp

When processing your payroll, the system determines the
 insurance or worker's comp liability based on values stored in the Insurance Accums table
 (PRIA).
They are as follows:

- Earnings – Gross (earnings subject to the insurance liability)

- Subject Amt – Earnings or hours, depending on the calculation method
 specified for the liability.

- Eligible Amt – Subject amount up to a limit, if specified.

- Basis Earnings – Earnings associated with the eligible amount.

- Calc Basis – Amount used to calculate the actual value of the
 liability.

The 'Earnings' are updated with the gross
 earnings, including any earnings that are flagged as 'subject only' (e.g. cafeteria
 plan). This will allow you to tie insurance reports to the FICA taxable wages on the PR
 941 report. The Subj Amount field on the insurance report represents the PRIA
 earnings
The 'Calc Basis' will be the same as the subject
 amount. If using straight time equivalent, the earnings will be the full gross
 (including premium pay), and the subject amount will be the straight time equivalent
 (excluding premium pay).
For example:
EarningsAmountsDescriptions
Employee
 Earnings$1,000.0040 hours @
 $25/hour
$37.501 hour OT
401(k)
 Contribution-$100.00Not subject to
 Ins/WC
Cafeteria Plan-$50.00Subject to Ins/WC, with
 Subject Only box
 checked in PR Deductions/Liabs
Gross$887.50

In the PRIA table, values would be stored as
 follows:
Liability MethodEarningsSubject AmtEligible AmtBasis EarningsCalc Basis
Rate of Gross$987.50$987.50$1,037.50$1,037.50$1,037.50
STE$987.50$975.00$1,025.00$1,037.50$1,025.00
Rate/Hour$987.50$41.00$41.00$1,037.50$41.00

All of the PR insurance reports include this
 information (PR Insurance Report, PR Insurance Report by Insurance Code, and PR
 Insurance Report by Job. Using the example above, for instance, the PR Insurance Report
 would display the following information for the STE liability method:
Report FieldDisplayed AmountPRIA Field that
 Determines Amount
Gross Amount$1,037.50Basis Earnings
Subj Amount$987.50Subject Amt
Basis$1,025.00Calc Basis
Eligible$1,025.00Eligible Amt

Additionally, the Subj Amount
 field on the report ties to the PR 940/941 Information report of FICA wages.
Note: When processing payroll (PR Payroll Process), the system
 stores hours in the PRIA table. This enables reporting hours along with worker’s
 compensation information to state authorities, if necessary. Run the PR Hours by State
 & Insurance Code report for reporting hours by insurance code.
