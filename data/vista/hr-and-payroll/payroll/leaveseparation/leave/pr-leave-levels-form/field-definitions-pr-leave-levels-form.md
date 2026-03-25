---
title: "Field Definitions: PR Leave Levels Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/leaveseparation/leave/pr-leave-levels-form/field-definitions-pr-leave-levels-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/leaveseparation/leave/pr-leave-levels-form/field-definitions-pr-leave-levels-form"
---

# Field Definitions: PR Leave Levels Form

The following is a list of field descriptions for the PR
 Leave Levels form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Leave Level

Leave Level field in the PR Leave Levels form.
If you want to be able to accrue employee leave at a rate specific to a
 job/contract, set up a code here and assign it to a leave code in the PR Leave Codes
 form (Leave Level Overrides tab). Then assign it to the job using either the JC Jobs or
 the PM Projects form. The system then considers this job/project-level Leave Level code
 as a potential override during processing.
When you process PR Auto Leave, the system compares the following two rates and uses the highest of the two in leave accrual calculations:

- the rate set for the employee in the PR Employee Leave form, or if there is not one there, the PR Leave Codes form

- the rate associated with the leave level code (as set in the PR Leave Codes form, Leave Level Overrides tab)

If the job leave rate happens to be the highest of the two, the amount of leave accrued by the employee is also based on how much they worked on the job. Note: Job-specific Leave Level overrides affect only *accruals* . These accruals cannot override limits, nor do they impact frequencies or usage.

## Description

Description field in the PR Leave Levels form
Enter a description for this Leave Level code that helps you identify it in reports and other forms.
