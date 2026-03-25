---
title: "About the PR Ledger Update Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/about-the-pr-ledger-update-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/about-the-pr-ledger-update-form"
---

# About the PR Ledger Update Form

Use this form to send payroll information to Job Cost,
 Equipment Management, Service Management, General Ledger, and Cash Management.

It also updates each employee’s monthly accumulations of earnings, deductions, and liabilities.
All of the updates must be run after the pay period is closed, but each may also be run while the pay period is still open. Running an update before closing the pay period allows you to produce reports in the updated module that include the most current payroll information (e.g., daily Job Cost reports often need to be run before the week is complete).
Each of the updates is able to post entries to more than a single month. When running the JC, EM, and SM updates, the timecard date is compared to the pay period’s Cutoff Date to determine which month to record costs and revenue. The GL, CM, and Accumulations updates use the employee’s payment month to determine which month updates. The GL update posts expenses based on timecard date, as well as cash based on the payment date. If expenses fall in one month and payment in another, the necessary accruals are made in the first month and reversed in the next.
Note: If you run the General Ledger/Cash Management/Accumulations update, the Job Cost/Equipment Usage/SM Labor Costs update must also be run. GL distributions related to EM revenue breakdown require processing of EM revenue performed with the JC/EM/SM update.
A validation procedure must be run before the update to check for valid codes and load the appropriate interface tables. These tables are used to print distribution reports before the update occurs. If any invalid codes are found, an error list can be printed to help you find and correct the problem.
Note: If you have checked the Attach GL ledger update reports to pay
 period box in PR Groups, the system will attach copies of the
 distribution reports to the pay period control record for the specified group. In order
 for reports to be attached, the corresponding box must be checked in the Distribution
 Reports section of the form.
Batch IDs are required on detail added to JC, EM, GL, CM, and SM; therefore, batches are added automatically during the update—one batch is created for each month updated.
For more information on using this form, see [Running Ledger Updates](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/run-a-ledger-update).

Related information

- [Run a Ledger Update](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/run-a-ledger-update)

- [Job Cost Update](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/run-a-ledger-update/job-cost-update)

- [Equipment Management Updates](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/run-a-ledger-update/equipment-management-updates)

- [General Ledger Update](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/run-a-ledger-update/general-ledger-update)

- [Cash Management Update](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/run-a-ledger-update/cash-management-update)

- [Employee Accumulations](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/run-a-ledger-update/employee-accumulations)
