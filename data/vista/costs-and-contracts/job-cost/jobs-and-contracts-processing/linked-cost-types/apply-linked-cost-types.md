---
title: "Apply Linked Cost Types | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/linked-cost-types/apply-linked-cost-types"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/linked-cost-types/apply-linked-cost-types"
---

# Apply Linked Cost Types

When posting progress on a job (JC Progress Entry) or entering cost projections (JC Cost Projections or PM Cost Projections), you can have the system automatically update the related cost types.

1. Identify the cost type that you will use to post progress, for example labor. This is the primary cost type.

1. Select the primary cost type
 in the Link
 Progress Cost Type field (JC Cost Types> Info tab) on each cost
 type that should be linked to it. For example, if you want to post progress to labor
 and want burden and equipment update with the same units or percent complete, you
 need to select the labor cost type in the Link Progress Cost Type field on
 both the burden and equipment cost types.

1. When posting progress using the [JC Progress Entry ](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-progress-entry-form) form, posting units or percent complete to the primary cost type will automatically update the linked the cost types. For example if you post 100 units to labor, 100 units will also be posted to burden and equipment.

- If you are posting progress units for a primary cost type
 and the linked cost type has estimated units of 0.00, units will only be posted to
 the linked cost type if the UM is the same as the primary cost type UM.

- You can post progress to the linked cost types even if
 progress has not been posted to the primary cost type. This provides for those
 situations where the primary cost type is not used on a job, but the linked cost
 types are. In this case, the primary cost type will not be updated.

1. Optional:
 You can override a linked cost type when posting progress using the JC Progress Entry
 form. Select File > Maintain
 Progress Link Cost Types to override the linked cost types. The changes made using this option
 will only impact the current batch. [More](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/jc-progress-link-ct-detail-form)

1. When you enter projections (in JC Cost Projections or PM Cost Projections), the system will automatically
 update any linked cost types when you enter a plugged value on a primary cost type.
[](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-cost-types-form)JC Cost Types
[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-progress-entry-form)JC Progress
 Entry
[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/jc-progress-link-ct-detail-form)JC Progress Link CT
 Detail
