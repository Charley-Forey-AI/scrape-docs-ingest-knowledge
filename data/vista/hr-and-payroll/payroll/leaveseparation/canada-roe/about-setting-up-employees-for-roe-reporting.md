---
title: "About Setting Up Employees for ROE Reporting | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/leaveseparation/canada-roe/about-setting-up-employees-for-roe-reporting"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/leaveseparation/canada-roe/about-setting-up-employees-for-roe-reporting"
---

# About Setting Up Employees for ROE Reporting

(Canada only) Important information regarding ROE reporting.
In order for ROE records to be generated for employees, you must enter dates in the Most Recent Rehire Date and Separation Date fields in the PR Employees form.
This is due to how the system determines what data must be included in an employee's ROE records.

- The system uses the time period between the last rehire date and the separation date for the employee to determine the time period from which to pull payroll data when generating employee ROE records.

- The system only reports on data for the last 12 months the employee worked plus one pay period (to meet Service Canada specifications). If the employee has worked less than 12 months (plus one pay period) between the most recent rehire date and the separation date, the system will use the entire time period between those dates.

- When calculating Total Insurable Earnings for Block 15B of the ROE report, the system includes data for the last 6 months the employee worked plus one pay period.

- The Most Recent Rehire Date field value comes from the Hire Date field for new employee records. However, you must enter a date in this field for any existing records.

- The Separation Date field

- is used specifically for ROE reporting and works independently from the Term Date field.

- Indicates the end date for the employee's period of employment for reporting purposes and may not represent a termination date (in the case of maternity leave, for example). For more information, see the field help for the [Termination Date](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employees-form/field-definitions-pr-employees-form#ID-0003821e--en) field.

- If an employee returns to work after an interruption of earnings, you should clear the Separation Date field and update the Most Recent Rehire Date field.

- If you change an employee's payroll group (PR Group field, PR Employees form), the system will only report information on the ROE report based on the current pay period.

Related information

- [About the PR Record of Employment Form](/en/vista/vista/hr-and-payroll/payroll/leaveseparation/canada-roe/about-the-pr-record-of-employment-form)
