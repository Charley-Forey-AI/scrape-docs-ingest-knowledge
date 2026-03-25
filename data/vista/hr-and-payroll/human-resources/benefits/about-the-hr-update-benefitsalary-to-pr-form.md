---
title: "About the HR Update Benefit/Salary to PR Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/human-resources/benefits/about-the-hr-update-benefitsalary-to-pr-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/human-resources/benefits/about-the-hr-update-benefitsalary-to-pr-form"
---

#  About the HR Update Benefit/Salary to PR Form

Use the HR Update Benefit/Salary to PR form to prepare HR benefits and/or salary information for update to PR.
This program is the only program within HR that is processed by batch. The criteria on this form is used to determine what information will be initialized into the batch (i.e. salary and/or benefits) and for whom. Once initialized, the batch can be validated, reviewed, and posted.

## Selection Criteria

When selecting
 the information to initialize to a batch, you must
 first specify whether to initialize all employees or
 a specified employee. If restricting by employee,
 you have the option to initialize using the HR
 resource number or the PR employee number.
Next you must
 specify whether to update salary information (Post
 Salary to PR) and/or benefits information (Post
 Benefits to PR). Although you do not have to select
 both options, you must select at least one in order
 to update the batch table.
If you are
 updating benefits information (Post Benefits to PR
 is checked), you have the option to restrict
 selection by benefit code. If using this method of
 selection, only those employees who have benefit
 information for the specified benefit code will be
 loaded into the batch table. Additionally, the
 benefit’s Update PR option must be checked in HR
 Resource Benefits in order for the benefit to be
 updated into the batch table.
The Effective
 Date is used to restrict what gets updated into the
 batch table. Salary and benefit changes must be
 effective on or before the specified Effective Date
 in order to be included in the update.
Note: In order for benefits to
 be included in the batch table for a resource, they
 must meet the following criteria:

- The benefit code must be
 flagged as Active (in HR Resource Benefits) and an
 Effective Date specified.

- The Ready
 Y/N box must be checked for one or
 more of the deduction, liability, and earnings
 codes defined for the benefit code (in HR Resource
 Benefits).

## Update and Post the Batch

Once you have entered the criteria, click the Update button
 to load the batch table. The grid at the bottom of
 this form will display all of the eligible entries
 in the batch, showing the employee and resource
 numbers, employee's name, whether it is a benefit or
 salary update, the benefit code and description, and
 whether you are adding or changing information. You
 can repeat the criteria selection process as
 necessary.
 If you are
 satisfied with all entries in the grid, click the
 Post button (at the bottom of the form). This will
 bring up the HR Batch Process form, and you can
 process the batch as normal.
Note: Resources that do not
 have a valid PR Employee # will be excluded from the
 grid, regardless of whether changes have been made
 to salary and/or benefits information. Employee must
 exist in PR and have a valid PR employee number.


## Removing Entries

If after populating the grid, you determine there are
 employees that you do not want included in the
 update, you can remove those employees before
 Posting the batch. Just enter the employee's
 resource number in the 'HR Resource #' field and
 click the Remove button. This will remove the
 specified employee from the grid. You can repeat
 this process as many times as necessary until you
 are satisfied with the remaining entries. Then post
 the batch as normal.Note: To remove all entries in the
 batch at one time, click the Cancel button. A
 message displays asking for confirmation that you
 want to clear the batch. Click Yes to clear the
 batch, No to cancel and leave the batch intact.
