---
title: "About Changing Existing Subcontracts | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-changing-existing-subcontracts"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-changing-existing-subcontracts"
---

# About Changing Existing Subcontracts

Changes to a previously added subcontract’s original amounts,
 as well as any other changes, may be made within certain limitations. To change a
 subcontract, bring it into a batch by using SL Add Transaction to Batch (accessed by
 selecting File > Add
 Subcontract).
Once you add a subcontract to the batch,
 changes can be made to any information in the header, except for the subcontract number
 and the Job Cost company. Use SL Compliance to make changes to previously initialized
 compliance detail.
Items can be deleted or changed as long as
 they do not have posted change orders or invoices. If change orders or invoices exist,
 the job, phase, cost type, and unit of measure cannot be changed.
Original amounts can be changed on existing
 items under the following conditions:

- If all of an item’s Original and Current values are equal, then any
 Original amount can be changed.

- If an item’s Original and Current Unit Cost are equal, but its Original
 and Current Units or Total Cost are not, then Original Units and Total Cost can be
 changed, but Original Unit Cost cannot.

Changes to Original amounts will make an
 equal change to Current amounts, so that the Change Detail will represent the difference
 between Original and Current. Total and Remaining Committed Units and Costs will also be
 adjusted in JC.
The Vendor field (subcontractor) cannot be
 changed under the following conditions:

- The subcontract has been invoiced;

- The subcontract has associated change orders; or,

- The subcontract is in a worksheet.
