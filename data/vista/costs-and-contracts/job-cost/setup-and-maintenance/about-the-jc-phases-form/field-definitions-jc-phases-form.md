---
title: "Field Definitions: JC Phases Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-phases-form/field-definitions-jc-phases-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-phases-form/field-definitions-jc-phases-form"
---

# Field Definitions: JC Phases Form

The following is a list of field descriptions for the JC
 Phases form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Phase

 Enter a unique
 code for a division of work on a job. The exact length (number of characters) and format
 (such as dashes between characters) of the phase code is defined to your specifications at
 installation time by Viewpoint.

[](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-phases-form)JC Phases

##  Description

 Enter a description for this phase code, up to
 60 characters. If a description needs to change on different jobs, set up a standard
 description here and then change the phase description for specific jobs in JC Job Phases
 or Project Management.

[](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-phases-form)JC Phases

##  Minimum Projection %

 Enter the minimum percent complete needed to
 calculate a cost projection in JC Cost Projections. If the percent complete is below this
 minimum, then the projected costs will be calculated as the higher of the estimated or
 actual costs.
Projection minimum percentage is set up in several places

- [PM Company Parameters ](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form) / [JC Company Parameters ](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/jc-company-parameters-form) - This value is only used if a projection minimum percentage has not been set up on the project/job or phases.

- [PM Projects](/en/vista/vista/project-management/projects-and-contracts/projects/pm-projects-form) / [JC Jobs](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form) - This value is only used if a projection
 minimum percentage has not been set up on the phases.

- [PM Project Phases ](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-phases-form) / [JC Job Phases](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-job-phases-form) - This field defaults based on the
 projection minimum percentage set up using the JC Phases form.

- [JC Phases
 ](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-phases-form) - This is the default value of the projection minimum percentage when new
 phases are added to a project/job.

[](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-phases-form)JC Phases

##  Cost Type

 Enter each of the valid standard cost types
 that apply to this phase. The system will only allow posting to these standard cost types
 for this phase.
Note: Standard cost types can be added to or changed for a specific job phase in JC Job Phases.  
[](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-phases-form)JC Phases

##  U/M

 Enter the standard unit of measure in which
 this cost type for this phase will be tracked. Must be a valid unit of measure set up in HQ
 Units of Measure.
 For labor, the unit of measure should not be HRS (hours) in most circumstances. Units are separate from hours, and actual units will not be updated with hours from Payroll. The UM should be the quantity to be completed. If no quantity (units) is being tracked, it may be set up as LS (lump sum).
Note: The standard unit of measure may be changed for a specific job phase in JC Job Phases. 
[](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-phases-form)JC Phases

## Bill Flag

Specify whether units and/or costs for this
 cost type on this phase are to be used in calculating progress complete. Used only for Job
 Billing.
Y = Both units and dollars posted to this cost type will be used to calculate progress complete.
C = Only dollars will be used in calculating percent complete for this phase/cost type.
N = Neither units or dollars posted to this cost type will be used when calculating progress complete. Cost types with this flag will also not be included in T & M billings.
Note: The standard bill flag may be changed for a specific phase in JC Job Phases.  
[](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-phases-form)JC Phases

##  Item Unit Flag

 Check this box if this cost type on this phase
 will be used to accumulate units complete for the related contract item. When summarizing
 job costs, the costs are all totaled, but only the units posted to the specified phase/cost
 type are counted. This option is typically checked for only one cost type on one phase
 linked to a contract item, and the phase selected would be the one most closely related to
 the contract item.
 Leave this box unchecked if this cost type will not be used to accumulate units complete for the related contract item.
Note: This flag is used only for reporting.  
[](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-phases-form)JC Phases

##  Phase Unit Flag

 Check this box if this cost type will be used
 to accumulate units complete for this phase. Typically, this box is checked for the main
 cost type, and only units posted to that cost type for that phase would be accumulated.
 Leave this box unchecked if this cost type will not be used to accumulate units complete for this phase.
Note: This flag is used only for reporting.  
[](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-phases-form)JC Phases

## Notes

Use this tab to enter any miscellaneous information about this item.
The space allowance is virtually unlimited.
Spelling Check
 Click the Spelling icon on the toolbar or select
 Tools > Spelling
  to spell check the text in this field.
Add a Standard Note
Standard notes allow you to insert frequently used text into some fields in the application. This text is created and maintained using the [HQ Standard Note](/en/vista/vista/administration/headquarters/standard-notes/about-the-hq-standard-note-form) form.
To insert a standard note into the field, right
 click the mouse while focus is in the field and select Standard
 Notes from the shortcut menu, which opens the Standard Note Copy window.
 Then enter the standard note to copy (or select from F4 lookup) and click OK. The
 system inserts the selected note into the field.
