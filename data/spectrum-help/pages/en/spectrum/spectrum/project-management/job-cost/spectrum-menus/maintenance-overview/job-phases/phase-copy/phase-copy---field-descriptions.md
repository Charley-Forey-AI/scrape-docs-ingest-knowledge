---
title: "Phase Copy - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/maintenance-overview/job-phases/phase-copy/phase-copy---field-descriptions"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/maintenance-overview/job-phases/phase-copy/phase-copy---field-descriptions"
---

# Phase Copy - Field Descriptions

Use the table below for reference when completing fields on this screen.
FieldsDescriptions
Old jobThe job you enter here must already be set up in Jobs.
Enter the number of the job from which phase information is to be copied. Press F4 or double-click on this field to select from a list of available job numbers.

CompanyThis field defaults to the current company. To change the company, use the Up Arrow button on your keyboard from the New job field and select a different company code. You will only be able to enter a new company code if you have access to the Job Cost module in that company.
New jobEnter the number of the job to which phases are to be copied. Press F4 or double-click on this field to select from a list of available job numbers. To change the company, use the Up Arrow button on your keyboard from the New job field and select a different company code.
When you enter a new job number, the application validates that the job is
 valid in the destination company, has a status that is not complete, and has
 a phase mask that is the same length as the current job's phase mask.
In
 addition, the application confirms you have the appropriate security access
 in the Job Phases screen of the destination company
 and for the new job when job-based security is used in that company.

Include estimates?Leave the checkbox clear to exclude estimates, or select the checkbox if Estimate figures from the "old" job's phases should be copied into the "new" job's phases.
Copy unionsIf you are using wage codes and wage/unions are to be defined for a job, you can use the Phase Copy feature to copy wage codes, rather than to individually define wage codes in the window of the Job.
If you are not using wage codes, the Union code is irrelevant, even for when the New job is for a different company.

Union codeEnter the same job number in "old" and "new" job fields; then at the "union code" prompts, enter the code for each union that will have workers on this job, up to five. Repeat as needed.
Once you select OK, and as phases are being copied into Job Phases, the specified unions will be set up in the Jobs with their corresponding wage codes. To determine which wage codes should be set up, the system looks at the Wage code File Maintenance and the Union File Maintenance screens.
If this union code is recorded in the Job Cost > Job Phases > Properties > Wage Codes for Phases window, the wage/union code will be copied to the new
 job.
Note: Press F4 or
 double-click this field to display the Unions
 window and view the codes, Union names, and respective crafts. For more
 information, see [Union code example](/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/maintenance-overview/job-phases/phase-copy/union-code-example).

Include active wages codes onlySelect this checkbox if you want the system to not copy any inactive wage codes for any of the union codes you've specified.
ContinueSelect Continue to continue or Cancel to exit the screen without saving your changes.
If you are copying information to a new company, once the update is initiated,
 the phases will be copied to the destination company. If the worker's
 compensation code specified in the Job Phases > Phase Defaults window old job is not valid in the destination company, it
 will be left blank in the new phase.
If the work state,
 work county,
 work local, or
 worker's
 compensation codes specified in the Job Phases > Properties window of the of the old job are not valid in the destination
 company, the corresponding fields will be left blank in the new phase.
If the job includes a cost type that is not set up in the destination company,
 the cost type will be copied to the Cost Type File
 Maintenance screen in the destination company. The system
 will assure that the G/L account (if any) for the cost type is valid in the
 destination company before copying; if it is invalid or Not used, the G/L account
 code field will be left blank in Cost Type File
 Maintenance in the destination company.
