---
title: "About Moving Employee Records to Confidential Payroll | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/confidential-payroll/miscellaneous-procedures/about-moving-employee-records-to-confidential-payroll"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/confidential-payroll/miscellaneous-procedures/about-moving-employee-records-to-confidential-payroll"
---

# About Moving Employee Records to Confidential Payroll

There are situations when you want to "promote" an employee record into the confidential company.
Use the Copy Employees to Another Company utility, found in the Payroll module, to perform this task.
This utility is broken down into two main processes: copying information and purging information. When moving or promoting an employee to the confidential company, their information is first copied over to the confidential company. Then the existing information in the main company is purged leaving one set of employee data.
The following are key points about this utility:

- This feature can only be used when the pay cycle is clear. In other words, perform this step immediately after a pay cycle has been completed.

- As part of the copy process, once employees have been copied to another company, the software offers the ability to remove (purge) them from the original company.

- When copying an employee, you have the option to copy the Employee Maintenance information only, or to also include the History information.Important: If you choose to omit the historical information, you must run an employee file rebuild after you perform the copy. Go to Payroll  > Utilities > Rebuild Employee File. Make sure the Through Check Date is a date that includes all payroll checks for the current year. Accept the default dates for the Month-to-date, Quarter-to-date and Year-to-date fields.

- This feature includes protection to prevent employees from being copied if any validated codes, such as union or worker's compensation codes or formula codes assigned to deductions and user-defined fields, are not yet set up in the destination company.

- If any error(s) are encountered during the copy, a report displays the specific setup that is non-compliant in the destination company. Additional protection is provided when purging employees after the copy is complete if Human Resources module is present.

- You must have full security access to the Payroll module in both companies.

- Copying and purging of data are captured on the Spectrum Audit Log.

## Cost Center Enabled Companies Only

You must have security to access the employee's assigned cost center to proceed. Cost center overrides are not applicable here. You do not have to have access to the cost center in the new company. In other words, cost center validation is performed during the selections process only.
 The employee's existing cost center must exist in the new company, although a blank cost center is allowed.

Related information

- [Copy Employee Records to Another Company](/en/spectrum/spectrum/accounting/confidential-payroll/miscellaneous-procedures/copy-employee-records-to-another-company)
