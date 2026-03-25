---
title: "Field Definitions: HR Update BenefitSalary to PR Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/human-resources/benefits/about-the-hr-update-benefitsalary-to-pr-form/field-definitions-hr-update-benefitsalary-to-pr-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/human-resources/benefits/about-the-hr-update-benefitsalary-to-pr-form/field-definitions-hr-update-benefitsalary-to-pr-form"
---

# Field Definitions: HR Update BenefitSalary to PR Form

The following is a list of field descriptions for the HR
 Update BenefitSalary to PR form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Restrict by Employee

 Check this box to restrict
 initialization of salary and benefits information by Resource # or Employee #.
 Leave this box unchecked to initialize salary/benefits changes for all resources/employees.
Note: Employees with salary/benefits changes will only be
 pulled into the batch if the ‘Exists in PR’ flag in HR Resources is Y (checked) and they
 are assigned both a PR Co# and a PR Empl #.

##  Use Resource/Employee #

- Use HR Resource # - Select this option to restrict initialization of salary/benefits information by resource number (specified in the Employee # field below).

- Use PR Employee # - Select this option to restrict initialization of salary/benefits information by employee number (specified in the Employee # field below).

##  PR Co#

 Disabled if restricting by HR Resource #.
 Specify the PR company against which the Employee # specified below will be validated, and to which all salary and benefit information will be updated.

##  Employee #

 If initializing by HR Resource #, specify the
 resource (from HR Resources) for which to update salary and/or benefits information to PR.
 The resource number entered in the Employee # field below is validated against the
 currently active HR company.
 If initializing by PR Employee #, specify the employee (from PR Employees) for which to update salary and/or benefits information to PR. The employee number entered in the Employee # field below is validated against the PR company specified below.
Note: Employees with salary/benefit history will only be
 pulled into the batch if in HR Resources the "Exists in PR" flag is Y, and they are
 assigned a PR Co# and a PR Empl #.

##  Post Salary to PR

 Check this box to update all salary information for the specified resources/employees to PR.
 Leave this box unchecked if you do not want to update salary information for the specified resources/employees to PR.
Note: If you do not check this option, then you must check the Post Benefits to PR option in order to continue with the update process. At least one of these two options must be checked in order to post to PR.

##  Post Benefits to PR

 Check this box to update all benefit information for the specified resources/employees to PR.
 Leave this box unchecked if you do not want to update benefit information for the specified resources/employees to PR.
Note: If you do not check this option, then you must check the Post Salary to PR option in order to continue with the update process. At least one of these two options must be checked in order to post to PR.
 In addition, the 'Update to PR' option must be checked for each benefit defined for the employee (in HR Resource Benefits) that you want updated to PR. Those benefits not flagged for update will be skipped during the update process.

##  Restrict by Benefit Code

 Enabled only if Post Benefits to PR option is checked.
 Check this box to restrict initialization by benefit code.
 Leave this box unchecked to initialize all benefit codes.

##  Benefit Code

 Enabled only if restricting initialization by benefit code.
 Specify the benefit code (from HR Benefit Codes) that will be included in the update to PR.

## Effective Date

Specify the effective date for restricting the information being updated to PR. All salary and/or benefit changes that are effective on or before this date will be included in the update.

##  HR Resource #

 Enter the resource number to remove from the batch. Then click the Remove button (to the right) to remove the resource from the grid and the batch.
Note: This feature allows you to remove individual resources from the update batch. However, if you want to remove all resources from the batch, use the Cancel button.
