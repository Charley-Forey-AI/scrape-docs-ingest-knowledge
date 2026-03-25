---
title: "Sort Options and Restrictions for Printing Payroll Checks | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/payments/sort-options-and-restrictions-for-printing-payroll-checks"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/payments/sort-options-and-restrictions-for-printing-payroll-checks"
---

# Sort Options and Restrictions for Printing Payroll Checks

On the PR Check Print form, sort options and restrictions control the order in which checks are printed, as well as determine which checks print.
The Sort Checks by drop-down field controls the five sort options, which include:

- N - Employee Sort Name - Select this option to print checks in order by the employee sort name.

- E - Employee # - Select this option to print checks in order by employee number.

- J - Job, Check Print Order and Employee # - Select this option to print checks in order by job, then by check print order, and then by employee number.

- C- Check Print Order and Employee # - Select this option to print checks by check print order and then by employee number. You can set the check print order using the Check Print Order field in PR Employees or the Check Print Order field in PR Employee Pay Seq Control. These fields allow you to determine the order in which checks print.

- W- Crew, Check Print Order and Employee # - Select this option to print checks by crew, check print order, and then by employee number.For example, if sorting by job, check print order and employee number, checks are first sorted using the job assigned to the employee (in PR Employees), then by the check print order assigned to each employee (in PR Employees), then by employee number. Employees with no job and/or check print order assigned print first. If you prefer to print by job make sure the Check Print Order is blank for all employees.
 The same applies if sorting by crew, check print order, and employee number. Employees with no crew and/or check print order assigned print first. If check print order is left blank for all employees, checks print in order by job and employee.

Depending upon the sort option you specify, different restriction options are displayed to allow specifying the range of employee sort names, employee numbers, job codes, check print order numbers, or crew codes. You can also restrict checks to print only one payment sequence number or only a selected range of employees based on the employee number. The following table displays the different restriction fields that display when you select a specific sort option. The first field is the restriction checkbox, while the bulleted items are the fields that define restriction criteria.
Sort Option
Available Restriction Fields

N - Employee Sort Name
Restrict by Employee Sort Name

- Beginning Sort Name

- Ending Sort Name

E - Employee #
Restrict by Employee #

- Beginning Employee #

- Ending Employee #

J - Job, Check Print Order and Employee
Restrict by Job and Employee #

- Beginning JC Co#

- Job

- Employee #

- Ending JC Co#

- Job

- Employee #

C - Check Print Order and Employee #
Restrict by Check Print Order and Employee #

- Beginning Check Print Order

- Employee #

- Ending Check Print Order

- Employee #

W - Crew, Check Print Order and Employee #
Restrict by Crew and Employee #

- Beginning Crew

- Employee #

- Ending Crew

- Employee #
