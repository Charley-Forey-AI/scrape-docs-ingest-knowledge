---
title: "About Sort Options and Restrictions for Printing Direct Deposit Stubs | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/payments/print-direct-deposit-stubs/about-sort-options-and-restrictions-for-printing-direct-deposit-stubs"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/payments/print-direct-deposit-stubs/about-sort-options-and-restrictions-for-printing-direct-deposit-stubs"
---

# About Sort Options and Restrictions for Printing Direct Deposit Stubs

The PR Deposit Print form provides several sort options and restrictions to control the order in which direct deposit stubs print, as well as determine which checks print.
Depending upon the sort option you specify,
 different restriction options are displayed to allow specifying the range of employee
 sort names, employee numbers, job codes, check print order numbers, or crew codes.
Note: You can also restrict checks by payment sequence number
 and/or by CM reference number, as well as specify to include employees notified by
 email. For more information about these options, see the F1 help.

The following table shows the available sort
 options, along with their related restriction options.
Sort Option
DescriptionAvailable
 Restriction Fields

N - Employee Sort
 Name
Print checks in order by the employee sort name.
Restrict by Employee
 Sort Name

- Beginning
 Sort Name

- Ending Sort
 Name

E - Employee #
Print checks in order by employee number.
Restrict by Employee
 #

- Beginning
 Employee #

- Ending
 Employee #

J - Job, Check Print
 Order and Employee
Print checks in order by job, then by check print order, and then
 by employee number.
Restrict by Job and
 Employee #

- Beginning JC
 Co#

- Job

- Employee #


- Ending JC
 Co#

- Job

- Employee #


C - Check Print
 Order and Employee #
Print checks by check print order and then by employee
 number.
You can set the check print order using the Check
 Print Order fields in either PR Employees or PR
 Employee Pay Seq Control.
Restrict by Check
 Print Order and Employee #

- Beginning
 Check Print Order

- Employee #


- Ending Check
 Print Order

- Employee #


W - Crew, Check
 Print Order and Employee #
Print checks by crew, then by check print order, and then by
 employee number.
Restrict by Crew and
 Employee #

- Beginning
 Crew

- Employee #


- Ending Crew


- Employee #


For example, if you select to sort by job,
 check print order, and employee number, checks are first sorted using the job assigned
 to the employee (in PR Employees), then by the check print order assigned to each
 employee (in PR Employees), then by employee number. Employees not assigned a job or
 check print order are printed first. If you prefer to print by job, make sure the Check
 Print Order is blank for all employees.
The same applies if sorting by crew, check
 print order, and employee number. Employees not assigned a crew or check print order are
 printed first. If you leave the Check Print Order blank all employees, checks print in
 order by job and employee.
