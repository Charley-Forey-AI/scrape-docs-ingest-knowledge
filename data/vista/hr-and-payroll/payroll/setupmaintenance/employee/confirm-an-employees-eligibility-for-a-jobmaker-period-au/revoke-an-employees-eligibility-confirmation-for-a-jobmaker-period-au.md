---
title: "Revoke an Employee's Eligibility Confirmation for a JobMaker Period (AU) | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/confirm-an-employees-eligibility-for-a-jobmaker-period-au/revoke-an-employees-eligibility-confirmation-for-a-jobmaker-period-au"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/confirm-an-employees-eligibility-for-a-jobmaker-period-au/revoke-an-employees-eligibility-confirmation-for-a-jobmaker-period-au"
---

# Revoke an Employee's Eligibility Confirmation for a JobMaker Period (AU)

If you erroneously confirmed an employee's eligibility for a
 JobMaker reporting period and you reported the confirmation in a prior submission to the
 ATO, you must revoke the confirmation and report it to the ATO.
As with confirmations, revocations are reported as "pseudo-allowance" items using the Other Allowance Type code and a special JobMaker revocation description, and are reported within the employee's allowance collection in STP.Note: You should revoke a prior erroneous confirmation for an employee at your earliest opportunity after you have discovered the error, using either a regular, recurring STP Pay Event submission, or a special, out-of-cycle STP Update Event ("Fix YTD") submission.
The following steps outline how to revoke an employee's eligibility confirmation for a JobMaker period and report it to ATO via the STP process.

1. In PR Employees, enter the employee in the Employee field.

1. Click on the Add'l Info tab.

1. In the Confirmation of Eligibility by Period section, select the JobMaker period for which you are revoking eligibility confirmation.

1. From the drop-down, select M0#X - Revoke prior declaration (where # represents the period number). For example, from the Period 1 drop-down, you would select M01X - Revoke prior declaration.

1. Save the record.

1. To submit the revocation declaration to the ATO, you must run the STP process (via PR STP Process).When generating submission data, the system creates a pseudo-allowance entry on the Allowances tab (in PR STP Employee), with a Type of Other, a description of the revocation declaration (for example, "M01X - JobMaker Period 1 Revocation (JMHC-P01X)), and a YTD Amount of 0.00.For detailed information about running the STP process (generating data, verifying data, and creating the e-file), see [Create an STP Pay Event Report](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/single-touch-payroll-stp/create-an-stp-pay-event-report).

Related information

- [Confirm an Employee's Eligibility for a JobMaker Period (AU)](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/confirm-an-employees-eligibility-for-a-jobmaker-period-au)

- [Nominate / Renominate Employees for JobMaker Hiring Credit (AU)](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/nominate--renominate-employees-for-jobmaker-hiring-credit-au)

- [PR Employees Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employees-form)

- [PR STP Process Form](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/single-touch-payroll-stp/pr-stp-process-form)
