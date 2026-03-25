---
title: "Field Definitions: HR Initialize PR Employees Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/human-resources/applicantsresources/resource-setupmaintenance/about-the-hr-initialize-pr-employees-form/field-definitions-hr-initialize-pr-employees-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/human-resources/applicantsresources/resource-setupmaintenance/about-the-hr-initialize-pr-employees-form/field-definitions-hr-initialize-pr-employees-form"
---

# Field Definitions: HR Initialize PR Employees Form

The following is a list of field descriptions for the HR
 Initialize PR Employees form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Update Direction

Specify whether to update to HR or from HR.

- Update PR to HR - Select this option if you wish to
 initialize employees set up in PR Employees into HR Resources. Update will only occur
 for those employees that do not already exist in HR and meet the criteria (i.e. do
 not have the same first/last name combination and/or same SSN).

- Update HR to PR - Select this option if you wish to
 initialize employees set up in HR Resources into PR Employees. Update will only occur
 for those employees that do not already exist in PR and meet the criteria (i.e. do
 not have the same first/last name combination and/or same SSN, and are assigned a PR
 group, department, earn code, race, SSN, craft, class, insurance code/state, local
 code, and unemployment state.)

## PR Co#

Specify a valid PR company. If initializing
 resources from HR Resources to PR Employees, this will be the PR company to which employees
 will be initialized. If initializing employees to HR Resources from PR Employees, this will
 be the PR company from which employees will be initialized.

## Initialize All

Check this box to initialize all eligible employees
 (Update PR to HR) or resources (Update HR to PR). When initializing from PR to HR, an
 employee is eligible if no resource exists in HR with the same SSN and/or first/last name.
 When initializing from HR to PR, an resource is eligible if no employee exists in PR with
 the same PR Employee #, SSN, and/or first/last name, and the Exists in PR flag (HR
 Resources) is not checked.
Uncheck this box to initialize a specified range of employees/resources (designated below).
Once you have entered desired criteria, click
 Update
 Grid to load the grid with all eligible employees/resources. If any of the
 Readyflags are unchecked, you can clear them from the grid using the Clear
 button. A message displays asking you if you want to clear only those entries that are not
 ready to be initialized. Click Yes to clear only the entries flagged as
 N, or click No to clear all entries from the grid. After you have reviewed all of the
 entries, click on the Initialize button to implement the update process. All eligible
 employees/resources will be update to the appropriate module.

- If an employee’s Ready box
 is checked, but you do not want them included in the update, you can change this flag
 to N in the grid. However, once changed, you cannot change the flag back to Yes. You
 will need to clear the grid and then repopulate it to reset the flag.

- You should only use this program to initialize new
 resources/employees; updates to static, salary, or benefits information for an
 employee/resource should be handled in HR Resources (static info) or HR Update
 Benefit/Salary to PR (salary/benefits info).

## Exclude Inactive Employees

Check this box to exclude all employees flagged as
 “inactive” when initializing for update to HR or PR. If updating to HR from PR, this will
 be all employees whose Active flag in PR Employees is N
 (unchecked). When updating to PR from HR, this will be all employees whose Active PR
 Employee flag in HR Resources is N (unchecked).
Uncheck this box to include all employees when initializing for update to HR or PR, regardless of whether they are active or inactive.
Once you have entered desired criteria, click
 Update
 Grid to load the grid with all eligible employees/resources. If any of the
 Readyflags are unchecked, you can clear them from the grid using the Clear
 button. A message displays asking you if you want to clear only those entries that are not
 ready to be initialized. Click Yes to clear only the entries flagged as
 N, or click No to clear all entries from the grid. After you have reviewed all of the
 entries, click on the Initialize button to implement the update process. All eligible
 employees/resources will be update to the appropriate module.

- If an employee’s Ready box
 is checked, but you do not want them included in the update, you can change this flag
 to N in the grid. However, once changed, you cannot change the flag back to Yes. You
 will need to clear the grid and then repopulate it to reset the flag.

- You should only use this program to initialize new
 resources/employees; updates to static, salary, or benefits information for an
 employee/resource should be handled in HR Resources (static info) or HR Update
 Benefit/Salary to PR (salary/benefits info).

## Beginning/Ending Employee #

This field is enabled only if the Initialize
 All box is unchecked.
Specify the beginning and ending in a range of employees that you want to initialize from PR to HR, or resources that you want to initialize from HR to PR.
Once you have entered desired criteria, click
 Update
 Grid to load the grid with all eligible employees/resources. If any of the
 Readyflags are unchecked, you can clear them from the grid using the Clear
 button. A message displays asking you if you want to clear only those entries that are not
 ready to be initialized. Click Yes to clear only the entries flagged as
 N, or click No to clear all entries from the grid. After you have reviewed all of the
 entries, click on the Initialize button to implement the update process. All eligible
 employees/resources will be update to the appropriate module.

- If an employee’s Ready box
 is checked, but you do not want them included in the update, you can change this flag
 to N in the grid. However, once changed, you cannot change the flag back to Yes. You
 will need to clear the grid and then repopulate it to reset the flag.

- You should only use this program to initialize new
 resources/employees; updates to static, salary, or benefits information for an
 employee/resource should be handled in HR Resources (static info) or HR Update
 Benefit/Salary to PR (salary/benefits info).

## Ready

Indicates whether an employee is ready to be initialized to PR.
Checked – Employee is ready to be updated to PR.
Unchecked – Employee is not ready to be updated to PR and will be skipped during initialization.
Note: You can clear employees from the grid that are not ready to be updated to PR by clicking the Clear button and answering Yes to the ‘clear only entries that are not ready’ message. It is important to note that answering No to this message will clear all employees from the grid.
If this flag is set to Yes (checked) for an employee, but you do not want to update the employee to PR, you can set this flag to No (unchecked); however, once you uncheck this option, you cannot change it back to Yes. You will need to clear the entry from the grid and repopulate the grid to reset the flag.
