---
title: "JC Progress Link CT Detail Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/jc-progress-link-ct-detail-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/jc-progress-link-ct-detail-form"
---

#  JC Progress Link CT Detail Form

Use this form to link cost types in this batch.
To open this form, select File > Maintain Progress Link Cost Typesin the [JC Progress Entry ](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-progress-entry-form) form.
 Linking cost types allows you to tie cost types together so that when you are posting progress on a job, the linked cost types are automatically updated with the same units or percent complete as the primary cost type. A common use for this might be linking burden and/or equipment to labor.
 You will normally maintain cost type links in JC Cost Types; however, this form allows you to define this relationship on a batch-by-batch basis. This allows for situations where you do not want automatic updates of units complete for linked cost types on one or more jobs. For example, you might have your equipment cost type linked to your labor cost type so that units complete posted for labor will automatically update the units complete for equipment. However, you now have one or more jobs where equipment was either not used or where units complete for equipment differs than units complete for labor. Using this form, you would temporarily remove the ‘link to’ cost type (labor) for the equipment cost type. The equipment cost type will now display in the grid (provided you designated the cost type for display in JC Progress Filter) so that units complete can be entered for equipment separately.
 The reverse applies as well. If you do not normally link equipment to labor, but need to for a specific job (or jobs), you would use this form to temporarily link the equipment cost type to the labor cost type so that units complete entered for labor will automatically update units complete for equipment.
Important:
 It is important to note that overrides defined in this form apply only to the current batch and will affect all jobs/phases in the batch. Once the batch is posted, the overrides are cleared.
[Linked Cost Types](/en/vista/vista/costs-and-contracts/job-cost/costs/enter-cost-projections/linked-cost-types#concept-4453--en__concept-4453)
[About the JC Cost Types Form](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-cost-types-form#ID-000185a2--en__ID-000185a2)
[About the JC Progress Entry Form](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-progress-entry-form#ID-00019a61--en__ID-00019a61)
[About the JC Progress Filter Form](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-progress-filter-form#ID-00019b7c--en__ID-00019b7c)
