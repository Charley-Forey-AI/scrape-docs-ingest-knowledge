---
title: "Field Definitions: JC Projections Calculation Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-projection-calculation-form/field-definitions-jc-projections-calculation-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-projection-calculation-form/field-definitions-jc-projections-calculation-form"
---

# Field Definitions: JC Projections Calculation Form

The following is a list of field descriptions for the JC
 Projections Calculation form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Write Over Plugged Values

Use these options to select how previously plugged values entered in batches in the current month or prior months will be handled. The selection in this field does not take into account plugged values entered in the current batch.
The options that display are based on the
 projection method set up using the [JC Projection Options ](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-projection-options-form) form - for example the Only When Actual Costs
 Exceed Plugged Costs option will only display when you are using the Actual
 Costs projection method.

- Never — Never write over existing plugged values.

- Always — Always write over plugged values.

- Only When Actual Costs Exceed Plugged
 Costs - Plugged values are only overwritten when the actual costs
 exceed the plugged costs.

- Only
 When Actual + Committed Costs Exceed Plugged Costs - Initialization
 will only write over plugged values when the actual plus remaining committed costs
 exceed the plugged costs. This option will only display when the projection method
 set up

- Only When Actual Costs Exceed Plugged Costs, Keep as Plugged - Initialization will only write over plugged values when the actual costs exceed the plugged costs; however, values will remain flagged as ‘plugged’.

- Only When Actual + Committed Costs Exceed Plugged Costs, Keep as Plugged - Plugged values are only overwritten when the actual plus remaining committed costs exceed the plugged costs; however, values will remain flagged as ‘plugged’. This is the option used by most customers.
Note: This option is affected by the ‘Previous Projected Column Through Prior Month’ option (JC Projection Options). If checked, plugged values will only be overwritten if the ‘actual plus remaining committed’ costs exceed the previous month's projection. If not checked, plugged values will be overwritten when ‘actual plus remaining committed’ costs exceed all projections through the current month. Here is another way to think about it...
 Basically this option allows you to define the
 value of your opinion (the plugged values). For example if you select Never,
 you are saying that your opinion has a very high value and should never be
 overwritten. If you select Only when actual costs exceed plugged
 costs, you are saying that you are usually right, so only overwrite
 your value if the system can prove that you are wrong (actual exceeds plugged).

[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-projection-calculation-form)JC Projection Calculation

## Initialize Worksheet Detail Option

The system only enables this field when you
 you have check the Activate Projection Detail Feature box in JC Company Parameters,
 Projections tab.
Specify how to handle projection detail when calculating projections.

- None – Select this option if you do not want to initialize projection detail.

- Initialize Detail Projections with Values – Select this option to initialize projection detail with the existing values (units, hrs/unit, hours, cost/hour, unit cost, and amount).

- Initialize Detail Projections without Values – Select this option to initialize projection detail and set all values to 0.00 (units, hrs/unit, hours, cost/hour, unit cost, and amount).

[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-projection-calculation-form)JC Projection Calculation

## Initialize By

- All Jobs – Select this option to
 initialize projections for all jobs.

- Job Range – Select this option to
 initialize projections for a selected range of jobs.

- Project Manager – Select this option to initialize projections for all jobs assigned to the project manager specified below.

[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-projection-calculation-form)JC Projection Calculation

## Beginning Job

Enabled only when initializing by Job Range.
Enter the beginning job in a range of jobs to initialize.
Note: If you enter a soft- or hard-closed job and you do not allow posting to closed jobs (flags in JC Company Parameters), a message displays indicating the job’s status and entry is not allowed.  
[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-projection-calculation-form)JC Projection Calculation

## Ending Job

Enabled only when initializing by Job Range.
Enter the ending job in a range of jobs to initialize.
Note: If you enter a soft- or hard-closed job and you do not allow posting to closed jobs (flags in JC Company Parameters), a message displays indicating the job’s status and entry is not allowed.  
[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-projection-calculation-form)JC Projection Calculation

## Project Manager

Enabled only when initializing by Project Manager.
Enter the project manager (as defined in JC Project Managers) whose jobs you want initialized. Projections will be calculated for all jobs to which this project manager is assigned.

[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-projection-calculation-form)JC Projection Calculation
