---
title: "Union Copy Between Companies | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/utilities-overview/union-copy-between-companies"
fetched_at: "2026-04-03T20:47:07.463050+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/utilities-overview/union-copy-between-companies"
---

# Union Copy Between Companies

This screen is used to copy union information to another
 company.
Any date-sensitive union deduction, fringe, benefit tier and rate information will be
 automatically included in the copy.
During this update, the software will verify the General Ledger fringes payable accounts are valid in the destination company. If an account is not found, a window is available for you to designate a valid G/L account. The software further validates the Time + Material billing codes and deduction codes in the destination company. If a code is not set up in the "to" company field, it is not copied. If a union deduction override G/L account exists in the 'from' company but it does not exist or has a status of 'Not used' in the 'to' company, the override G/L account will be blank.
Caution should be exercised when performing this copy. This update may only be performed if the operator possesses security access to the Payroll module of the destination company.
Note: Clicking the Preview button runs the update and will only display
 a report if there are exceptions.
Companies Using Multi-company Processing
If you are using multi-company processing and you need to make union codes, wage codes and certified reports interact between multiple companies, this copy utility can be helpful when you need to pay for work on a job that resides in a different company. If the job has the union code attached to it, then you will only need a "home" union code in the payroll issuing company attached to the employee along with the default wage code for this employee.

- Use the Payroll > Utilities > Union Copy Between Companies utility to copy the union from the job company to the payroll company.
 Make sure the union/wage codes are attached to the job in the job company.

- The job will then drive what union code is used for each time card line based on the wage code. The union code will exist in both companies and the wage codes will only reside in the job company. You need to manually override the wage code if the employee changes his skill class for this particular time card line.

- Optional : If this is a certified job then you must make sure the employees
 that reside in the Payroll company have the Include on certified
 report checkbox selected on the [Employee Personal Information](/en/spectrum/spectrum/accounting/payroll/employees/employee-properties/employee-personal-information).
