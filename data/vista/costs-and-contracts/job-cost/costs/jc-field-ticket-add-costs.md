---
title: "JC Field Ticket Add Costs | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/costs/jc-field-ticket-add-costs"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/costs/jc-field-ticket-add-costs"
---

# JC Field Ticket Add Costs

Use the JC Field Ticket Add Costs form to add cost detail to or remove cost detail from a field ticket.
 You can access this form via the Job Cost Programs menu or from the JC Field Ticket form by selecting File > Add/Remove Costs.
When you open this form, the grid initially displays as blank. Once you specify the contract and cost posting month, the grid populates with applicable cost transactions for the contract that were posted in the specified month, are not currently associated with a field ticket, and not yet been billed. Applicable cost transactions are those with one of the following sources:

- AP Entry

- AR Receipt

- EMRev

- IN MatlOrd

- JC CostAdj

- JC MatUse

- MS Tickets

- PO Receipt (only if the Include PO Receipts checkbox is selected on the contract's JB Template)

- PR Entry

- SM WorkOrd

 You can further filter the number of transactions shown by specifying a transaction Type. For example, if you specify AP, only AP-related cost transactions for the specified month display in the grid.Note: Some sources may be associated with multiple transaction types. For example, costs with a source of SM WorkOrd can include transaction types AP, EM, IN, JC, MI, and PR. If you want to see only costs associated with a specific source, leave the Type field blank and use the grid filter to show only costs for the specified source.

You must also specify the field ticket to which you are assigning the cost transactions. Then either individually select transactions to add or click Check All to include all transactions in the grid. Once you click Add, the system assigns all selected transactions to the specified field ticket and displays them on the Cost Detail tab in JC Field Tickets.
You can also use this form to remove costs from the field ticket using the Show only ticketed costs checkbox. When selected, the grid populates with only those costs already assigned to the field ticket. You can then select the cost detail to remove and click Remove. The costs are removed from the ticket; however, the transactions remain intact.
Click the link below for more information on using this form.
[Add / Remove Costs for a Field Ticket](/en/vista/vista/costs-and-contracts/job-cost/costs/add--remove-costs-for-a-field-ticket)
