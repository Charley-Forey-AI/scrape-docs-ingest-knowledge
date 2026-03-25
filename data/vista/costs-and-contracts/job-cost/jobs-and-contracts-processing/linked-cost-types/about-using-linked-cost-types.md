---
title: "About Using Linked Cost Types | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/linked-cost-types/about-using-linked-cost-types"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/linked-cost-types/about-using-linked-cost-types"
---

# About Using Linked Cost Types

Linking cost types allows you to update related cost types automatically when posting progress on a job (in JC Progress Entry) or when entering cost projections (in JC Cost Projections or PM Cost Projections).
For example, you can set up labor as a primary cost type and burden as a secondary cost type. When entering cost projections for the job, any plugged value entered on the primary cost type automatically updates the secondary cost types. This means if you increase the Units Remaining on labor by 10%, the system automatically increases the burden Units Remaining by 10%.

## Why would you link cost types?

You might use linked cost types if:

- You post units complete and you typically use the same unit of measure and estimated units for some or all cost types or,

- You post percent complete and do not use the same unit of measure on all cost types, but typically assume that the percent complete is the same across all cost types.

Do not use linked cost types if you want to enter the units or percent complete on each cost type on a phase.

## Job Cost vs. Project Management

Cost projection handling for linked cost types differs between Job Cost and Project Management.
 In Job Cost, linked cost types automatically update when the primary cost type is updated. For example, if "Burden" is linked to "Labor," updating labor units in JC Cost Projections automatically updates the associated burden units.
 In Project Management, cost projections are managed by projection code. Linked cost types assigned to a projection code do not automatically update when the primary cost type changes. To enable automatic updates for linked cost types, you must select the Proj Code Units checkbox in PM Projection Codes for each relevant projection code/linked cost type combination. If this checkbox is not selected, changes to the primary cost type's projected units will not update the linked cost types.
