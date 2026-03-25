---
title: "About PAYG Reporting Periods (Australia) | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/about-payg-reporting-periods-australia"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/about-payg-reporting-periods-australia"
---

# About PAYG Reporting Periods (Australia)

You can use the PAYG Reporting Periods tab in PR Employees to track the employment cycles for each employee.
You can only access the PAYG Reporting Periods tab if the Default Country field in the HQ Company Setup form is set to AU for the active company.
For long term employees, this generally means they will have one reporting period per year, running 7/1/YY through 6/30/YY. Other employees, however, may have multiple employment cycles due to seasonal work or other separation reasons. In this case, there will be a separate reporting period record for each employment cycle.
The system automatically creates and updates reporting periods based on hiring and termination dates. However, reporting periods are also affected by income type changes and the generation of year-end or on-demand PAYG summaries.
If the income type for an employee changes (for instance, if a working holiday maker becomes a permanent employee), do not change the Income Type of the current reporting period, as it will cause a discrepancy in PAYG reporting. Instead, follow the steps for [changing an employee's PAYG income type](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/set-up-payg-withholding-for-employees/change-an-employees-payg-income-type-australia) to enable the system to create a new reporting period for the employee that reflects the new income type. This ensures that the summaries generated for each reporting period have the correct income type.
 When you generate a year-end or on-demand summary, if the employee has not been terminated, the system will update the Period End Date of the current reporting period record and create a new reporting period record for one day after the Period End Date of the prior record.
The following illustrates how the system creates and maintains reporting periods under the simplest conditions. For our examples, we will assume the same employee.
New Employee is set up in the PR Employees form

- Employee: John Smith

- Hire Date: 01/01/20

- Most Recent Hire Date: 01/01/20 (The first time you enter a Hire Date, the system sets the Most Recent Hire Date equal to the Hire Date. The system then uses the Most Recent Hire Date to populate the Period Start Date.)

The system creates a single period of reporting record:
Period Start Date
Period End Date
Final Pay Period Date
Income Type
Tax Year
Summary #

01/01/20

S - Salary or wages

Employee is terminated due to shortage of work

- Termination Date: 03/18/20 (The system uses the Termination Date to populate the Period End Date.)

The system updates the existing reporting period record as follows:
Period Start Date
Period End Date
Final Pay Period Date
Income Type
Tax Year
Summary #

01/01/20
03/18/20

S - Salary or wages

Employee is rehired

- Most Recent Rehire Date: 04/25/20 (Once you enter a rehire date, the system
 automatically clears the Termination Date.

The system creates a second reporting period record:
Period Start Date
Period End Date
Final Pay Period Date
Income Type
Tax Year
Summary #

01/01/20
03/18/20

S - Salary or wages

04/25/20

S - Salary or wages

Employee requests an On Demand summary

- Period End Date: 05/15/20 (This date should be a period end date closest to
 the date the employee requested the summary.)

- In PR PAYG Process:

- Tax Year: 2020

- In PR PAYG Employee Generate Amts:

- Process Through Date: 05/15/20 (The Process Through
 Date should be equal to the Period End Date you entered for the current
 reporting period.)

Once you enter the Period End Date for the current reporting period and save the record, the system automatically creates a new reporting period since the employee was not terminated. It sets the Period Start Date for the new record to one day after the Period End Date of the previous reporting period. When you generate the summaries (in PR PAYG Employee Generate Amts), the system updates the Tax Year for each applicable reporting period using the Tax Year you selected in PR PAYG Summary Process. In addition, it updates the Summary # for each reporting period as assigned to the related summary record in PR Employee PAYG Summaries.
Period Start DatePeriod End DateFinal Pay Period DateIncome TypeTax YearSummary #
01/01/20
03/18/20

S - Salary or wages
2020
1

04/25/20
05/15/20

S - Salary or wages
2020
2

05/16/20

S - Salary or wages

Year-end Summaries are generated

- Period End Date: blank (In this case, leave the Period End Date blank to allow the system to automatically set the Period End Date for all employees at one time.)

- In PR PAYG Process:

- Tax Year: 2020

- PR PAYG Employee Generate Amts:

- Employee: Leave blank (to run for all employees)

- Process Through Date: 6/30/20 (When running summaries for all employees, the Process Through Date field is disabled; however, the system automatically applies the date to 6/30 of selected tax year.)

Once you generate the summaries, the system sets the Period End Date for the current reporting year equal to the Process Through Date (6/30/YY). It also updates the Tax Year and Summary # as appropriate. It then creates a new period of reporting record with a Period Start Date of 7/1/YY (one day after previous record's Period End Date).
Period Start Date
Period End Date
Final Pay Period Date
Income Type
Tax Year
Summary #

01/01/20
03/18/20

S - Salary or wages
2020
1

04/25/20
05/15/20

S - Salary or wages
2020
2

05/16/20
06/30/20

S - Salary or wages
2020
3

07/01/20

S - Salary or wages

Related information

- [PR Employees Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employees-form)
