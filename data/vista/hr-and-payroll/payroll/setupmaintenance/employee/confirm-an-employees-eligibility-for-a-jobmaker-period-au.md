---
title: "Confirm an Employee's Eligibility for a JobMaker Period (AU) | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/confirm-an-employees-eligibility-for-a-jobmaker-period-au"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/confirm-an-employees-eligibility-for-a-jobmaker-period-au"
---

# Confirm an Employee's Eligibility for a JobMaker Period (AU)

Once you nominate employees for the JobMaker Hiring Credit
 (JMHC) program, you must then confirm each employee's eligibility for applicable JobMaker
 periods. Confirmation is required before you can make a claim for an
 employee/period.
For an employee to be eligible for a JobMaker period, they must satisfy the minimum hours requirement for that period; that is, they must have completed a minimum of 20 hours of work per week on average for the specified period (either the hours for which the employee is being paid or the hours the employee worked). Australian Taxation Office rules provide for consideration of paid overtime, paid leave, and paid absences on public holidays, but exclude any unpaid leave in the evaluation of hours. For the complete set of criteria, please see the ATO website. If you determine an employee satisfies the requirements, you must confirm the eligibility for the selected period, and then declare the confirmation via the STP (Single Touch Payroll) process. Confirmations are reported as "pseudo-allowance" items using the Other Allowance Type code and a special JobMaker declaration description, and are reported within the employee's allowance collection (in PR STP Employee, Allowances tab).
Note: You can confirm eligibility for an employee at any time after you have made a determination that the employee met the minimum hours test for the period. However, you must confirm the employee's eligibility for this period no later than the STP reporting due date (three days before the end of the relevant claim period) in order to make a claim for the employee for this period. For more information about reporting due dates, see the ATO website.

1. In PR Employees, enter the eligible employee in the Employee field.

1. Click on the Add'l Info tab.

1. In the Confirmation of Eligibility by Period section, select the JobMaker period (1-8) you are confirming for the employee.

1. From the drop-down, select M0# - Declare employee met minimum hours test (where # represents the period number). For example, from the Period 1 drop-down, you would select M01 - Declare employee met minimum hours test.

1. Save the record.

1. To submit the declaration to the ATO, you must run the STP process (via PR STP Process).When generating submission data, the system creates a pseudo-allowance entry on the Allowances tab (in PR STP Employee), with a Type of Other, a description of the declaration (for example, "M01 - JobMaker Period 1 Declaration (JMHC-P01)), and a YTD Amount of 0.00.For detailed information about running the STP process (generating data, verifying data, and creating the e-file), see [Create an STP Pay Event Report](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/single-touch-payroll-stp/create-an-stp-pay-event-report).

Related information

- [Nominate / Renominate Employees for JobMaker Hiring Credit (AU)](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/nominate--renominate-employees-for-jobmaker-hiring-credit-au)

- [Revoke an Employee's Eligibility Confirmation for a JobMaker Period (AU)](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/confirm-an-employees-eligibility-for-a-jobmaker-period-au/revoke-an-employees-eligibility-confirmation-for-a-jobmaker-period-au)

- [PR Employees Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employees-form)

- [PR STP Process Form](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/single-touch-payroll-stp/pr-stp-process-form)

- [Revoke an Employee's JobMaker Nomination / Renomination (AU)](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/nominate--renominate-employees-for-jobmaker-hiring-credit-au/revoke-an-employees-jobmaker-nomination--renomination-au)
