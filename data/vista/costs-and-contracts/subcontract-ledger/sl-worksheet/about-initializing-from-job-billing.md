---
title: "About Initializing From Job Billing | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-worksheet/about-initializing-from-job-billing"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-worksheet/about-initializing-from-job-billing"
---

# About Initializing From Job Billing

When using the Job Billing (JB) module to enter the
 quantities or dollars expected to be paid on an application with the owner, and the
 subcontractors should be paid based on these quantities or percent complete (typical of
 highway contractors), select the Use Job Billing to Initialize Amounts checkbox.
The initialization process will then
 pre-load the subcontracts with these amounts, which can then be edited as needed.
The billing contract and subcontract items
 are linked by selecting the same phase for both. This link works well in cases where the
 contract item and the phase are a one-to-one link. It may not work well when there are
 multiple phases pointing to a single contract item or multiple subcontracts are worked
 on for a single phase. For example, you might have several subcontractors all with items
 for mobilization. The owner is billed for 30% complete on mobilization. Although the 30%
 of work completed may show one subcontractor as 100% complete, another 50%, and another
 0%, the form assumes 30% on each subcontract with phases linked to contract item
 Mobilization.
If initializing subcontracts for these items
 is more confusing than helpful, uncheck the Initialize Subcontracts checkbox in JC
 Contract Items, and the update will not occur. When initializing from JB on these items,
 it is important to review and edit each subcontract as needed.
It may not be practical to initialize
 invoice amounts from JB if your organization processes subcontractor invoices before
 processing billing to the owner (typical of general contractors). Instead, with the Use
 Job Billing box unchecked, each subcontract item is loaded into the work file with zero
 billing for the current period, which can be edited as needed.
