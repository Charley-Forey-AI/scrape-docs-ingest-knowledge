---
title: "About the JC Projection Calculation Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-projection-calculation-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-projection-calculation-form"
---

# About the JC Projection Calculation Form

Use this form to initialize cost projections.
You can open this form by selecting File > Calculate Projections at the top of the [JC Cost Projections ](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-projections-form) form.

## Write Over Plugged Values

Use these options to select how previously plugged values entered in batches in the current month or prior months will be handled. The selection in this field does not take into account plugged values entered in the current batch.
The options that display are based on the projection method set up using the [JC Projection Options ](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-projection-options-form) form - for example the Only When Actual Costs Exceed Plugged Costs option will only display when you are using the Actual Costs projection method.

- Never — Never write over existing plugged values.

- Always — Always write over plugged values.

- Only When Actual Costs Exceed Plugged Costs - Plugged values are only overwritten when the actual costs exceed the plugged costs.

- Only When Actual + Committed Costs Exceed Plugged Costs - Initialization will only write over plugged values when the actual plus remaining committed costs exceed the plugged costs. This option will only display when the projection method set up

- Only When Actual Costs Exceed Plugged Costs, Keep as Plugged - Initialization will only write over plugged values when the actual costs exceed the plugged costs; however, values will remain flagged as ‘plugged’.

- Only When Actual + Committed Costs Exceed Plugged Costs, Keep as Plugged - Plugged values are only overwritten when the actual plus remaining committed costs exceed the plugged costs; however, values will remain flagged as ‘plugged’. This is the option used by most customers. Note: This option is affected by the ‘Previous Projected Column Through Prior Month’ option (JC Projection Options). If checked, plugged values will only be overwritten if the ‘actual plus remaining committed’ costs exceed the previous month's projection. If not checked, plugged values will be overwritten when ‘actual plus remaining committed’ costs exceed all projections through the current month. Here is another way to think about it...
 Basically this option allows you to define the value of your opinion (the plugged values). For example if you select Never, you are saying that your opinion has a very high value and should never be overwritten. If you select Only when actual costs exceed plugged costs, you are saying that you are usually right, so only overwrite your value if the system can prove that you are wrong (actual exceeds plugged).

## Initialized By

This section is used to specify how you will initialize projections. You can initialize projections for all jobs, a specific range of jobs, or by project manager. If initializing by project manager, projections will be initialized for all jobs to which the project manager you specify is assigned.

Click the links below for more information about using this form.
[About Initialize Worksheet Detail Option](/en/vista/vista/costs-and-contracts/job-cost/costs/enter-cost-projections/cost-projection-detail/about-initialize-worksheet-detail-option#concept-5275--en__concept-5275)
[Calculation Formula and Example](/en/vista/vista/costs-and-contracts/job-cost/costs/enter-cost-projections/calculation-formula-and-example#concept-4063--en__concept-4063)

Related information

- [About the JC Projection Options Form](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-projection-options-form)

- [About Reviewing & Updating Projections](/en/vista/vista/costs-and-contracts/job-cost/costs/enter-cost-projections/about-reviewing--updating-projections)

- [About the JC Projection Future CO Form](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-projection-future-co-form)

- [JC Job Phase Cost Detail Form](/en/vista/vista/costs-and-contracts/job-cost/costs/jc-job-phase-cost-detail-form)
