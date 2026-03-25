---
title: "About Setting Up a Change Order | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-setting-up-a-change-order"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-setting-up-a-change-order"
---

# About Setting Up a Change Order

You can set up change orders for existing jobs (in JC Change Orders) to identify additions, deletions, or modifications to the original scope of work on the job.
Change order amounts posted here may affect current contract amounts and/or current phase estimates; they do not affect the Original contract amount or Original phase estimate amounts.
There are three levels to a Job Cost change
 order:

- Header – Use this level to tie the
 change order to a job and its contract, specify the number of days by which the
 change order changes the completion date, and indicate whether the change order
 is internal (affecting the contractor’s internal budget) or external (affecting
 the owner’s schedule of values).

- Change Order Items – This level is
 used to set up change order items, indicating the contract items to which they
 are related, the number of days by which the item changes the completion date,
 and the changes to units and billable dollars.

- Phase/Cost Type Detail – This level
 is used to set up changes to your estimated costs related to this change order.
 Estimated changes to units, hours, and dollars will update your current
 estimate.

When adding change order items, you must
 specify the contract item to which the change order item is related. The contract item
 can be either a part of the original contract, or one you add for billing the change
 order. If you specify a contract item that does not already exist for the contract, you
 are immediately taken to the JC Contract Items form so that you can add the contract
 item.
Note: When adding a contract item on the fly, the units, unit
 price, and amount inputs are disabled. You will need to access the form via JC Contracts
 in order to modify the values for those fields.
The Phase Detail tab allows you enter change
 order detail; that is, the phases to which the change order applies. This includes the
 phase, cost type, month, UM, estimated hours and units, unit cost, and estimated cost.
 As with contract items, you can use existing phases or create new ones. Since you are
 adding estimated costs rather than actual costs, this program works somewhat like the
 Original Job Estimates program, in that it overrides the normal rules for locked jobs
 and allows you to create new phases even if the job's phases are locked. The new phases
 will be cross-referenced to the contract item for the change order item.
Note: As you enter items and phase detail, the
 informational section above the tab pages displays the Revenue, Cost, Profit, and Markup
 information for the change order item.
While you have extreme flexibility in how
 you use phases and contract items, as a practical matter, you should follow guidelines
 similar to these:

- If the owner is not requiring you to
 bill the change order separately, simply set up the change order with existing
 items and phases.

- If the owner wants to be billed
 separately, set up a new contract item for the change order. Then decide whether
 it is practical to collect your costs separately. If so, create new phases (such
 as by using the non-validated portion of your phase code--usually the
 sub-sub-phase). If separate costing is not practical, then use existing phases
 and try to break out the change order amount at billing time.

- For very large change orders, you
 may find it useful to create a new sub-job that is linked to the same contract.
 In this scenario, you need to set up all new contract items and phases for the
 change order.

Note: You can delete change orders (headers and items) if necessary; however, they can
 only be deleted if the change order does not exist on a billing in Job
 Billing.
