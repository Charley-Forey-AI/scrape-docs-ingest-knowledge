---
title: "Revoke an Employee's JobMaker Nomination / Renomination (AU) | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/nominate--renominate-employees-for-jobmaker-hiring-credit-au/revoke-an-employees-jobmaker-nomination--renomination-au"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/nominate--renominate-employees-for-jobmaker-hiring-credit-au/revoke-an-employees-jobmaker-nomination--renomination-au"
---

# Revoke an Employee's JobMaker Nomination / Renomination (AU)

If you erroneously nominated or renominated an employee for
 participation in the JobMaker program and you reported the nomination / renomination in a
 prior submission to the ATO, you must revoke the nomination / renomination and report it to
 the ATO.
As with nominations and renominations, revocations are reported as "pseudo-allowance" items using the Other Allowance Type code and a special JobMaker revocation description, and are reported within the employee's allowance collection in STP.Note: You should revoke a prior erroneous nomination for an employee at your earliest opportunity after you have discovered the error, using either a regular, recurring STP Pay Event submission, or a special, out-of-cycle STP Update Event ("Fix YTD") submission.
The following steps outline how to revoke a JobMaker nomination or renomination and report it to ATO via the STP process.

1. In PR Employees, enter the employee in the Employee field.

1. Click on the Add'l Info tab.

1. To revoke an employee's JobMaker nomination:

1. In the New Hire drop-down, select MNMX - Revoke prior nomination.

1. Save the record.

1. To submit the revocation to the ATO, you must run the STP process (via PR STP Process).During the generation process, the system creates a pseudo-allowance entry on the Allowances tab (in PR STP Employee), with a Type of Other, a description of "MHMX - JobMaker Nomination Revocation (JMHC-NOMX), and a YTD Amount of 0.00 (per ATO requirements).

1. To revoke an employee's JobMaker renomination:

1. In the Recent Rehire drop-down, select MRMX - Revoke prior renomination.

1. Save the record.

1. To submit the revocation to the ATO, you must run the STP process (via PR STP Process).During the generation process, the system creates a pseudo-allowance entry on the Allowances tab (in PR STP Employee), with a Type of Other, a description of "MRMX - JobMaker Renomination Revocation (JMHC-RENOMX), and a YTD Amount of 0.00 (per ATO requirements).For detailed information about running the STP process (generating data, verifying data, and creating the e-file), see [Create an STP Pay Event Report](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/single-touch-payroll-stp/create-an-stp-pay-event-report).

Related information

- [Nominate / Renominate Employees for JobMaker Hiring Credit (AU)](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/nominate--renominate-employees-for-jobmaker-hiring-credit-au)

- [Confirm an Employee's Eligibility for a JobMaker Period (AU)](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/confirm-an-employees-eligibility-for-a-jobmaker-period-au)

- [PR Employees Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employees-form)

- [PR STP Process Form](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/single-touch-payroll-stp/pr-stp-process-form)
