---
title: "Process Subcontract Backcharges | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/process-subcontract-backcharges"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/process-subcontract-backcharges"
---

# Process Subcontract Backcharges

A backcharge is an accounting of costs for something that has
 to be provided because of the subcontractor.
For example if a subcontractor does not clean up after completing a job and you have to use your own resources to perform the cleanup. The costs incurred are backcharged to the subcontractors, reducing the amount that you pay them.
Follow the steps below to process backcharges.

1. JC Job Phases or JC Original Estimates—Assign a phase to the job that backcharges will be posted to. It may be useful to reserve sub-phase or
 sub-sub-phase codes for backcharges, but NOT set up the phase codes in JC
 Phases; it cannot always be predicted when backcharge phases are used or how
 many will be needed.
If setting aside certain phase codes to use for backcharges, you might use a system as shown in the examples below:
Original Phases
Backcharge Phase

15400 - - Plumbing
15400 - - 99

09700- - Drywall
-or-

09800- - Taping
99000-01

09900- - Painting

The example of 15400- -99 assumes you reserve the last few characters of your phase codes (beyond the Valid # Of Chars In Phase code specified in JC Company Parameters) for backcharge phases. The example of 99000-01 assumes you reserve phase codes higher than normal for backcharge phases. The basic difference between these two examples is the location on Job Cost reports in which backcharge phases will print; 15400- -99 will appear within the range of actual cost phases while 99000-01 will appear at the end of the report after all other phases.

1. SL Subcontract Entry—Add a new item to the subcontract for backcharges, identifying the backcharge phase and cost type set up in Job Cost. Backcharge costs are accumulated through posting the actual costs in Payroll, Accounts Payable, or other appropriate accounting modules. Backcharge items are set up in SL Subcontract Entry using the Backcharge transaction type. When entering a Backcharge, specify the Job, Phase, and Cost Type that will be used to track incurred costs, which then become the basis of your backcharges. Entering an amount is optional, but backcharges do not affect a subcontract’s Original or Current totals (or JC committed cost), even if an amount is entered here.

1. PR Timecard Entry, AP Transaction Entry, IN Adjustments, etc.—Post costs for the additional work performed. Post all costs to the phase set up for backcharges on this subcontract.

1. SL Backcharge Detail Report—Run the report to determine the total backcharge costs posted to the backcharge phase in other accounting modules. When printing the SL Backcharge Detail report, the system collects all of the costs associated with each backcharge item. To reduce the payable amount to subcontractor(s), use the report when posting in AP.

1. AP Transaction Entry—Post a negative amount payables transaction (subcontract transaction type) to the subcontractor for the amount of all backcharge costs (plus any markup needed). This reduces the total payables amount owed on the subcontract, but does not affect the current totals on the subcontract.

Example

Current
Invoiced

Subcontract w/change orders
=
$ 20,000
$ 20,000

Backcharges
=
N/A
–650

Net
=
N/A
$ 19,350
