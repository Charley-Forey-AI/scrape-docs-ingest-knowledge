---
title: "Add Transaction Details to Bill Line Sequences | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/add-transaction-details-to-bill-line-sequences"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/add-transaction-details-to-bill-line-sequences"
---

# Add Transaction Details to Bill Line Sequences

The JB T&M Bill All JCDetail Lines form does not allow transaction editing; you can only
 add, delete, or mark transactions as billable.
When adding a JC transaction to a bill line sequence, the detail must match the detail requirements defined for the template
 sequence (e.g., source, summary and sort options, cost type, etc.) prior to
 initialization. If the transaction’s detail does not match the requirements, a
 warning displays. If the transaction does match the requirements, the system adds
 the transaction amounts (Units, Amount) to the detail sequence totals.
Note: A transaction’s Unit Price does not update the
 sequence’s Unit Price. Additionally, the transaction’s units only update the
 sequence’s units if the unit of measure is the same.
Note: To delete transaction detail, select the appropriate detail
 line and click the Delete button.

1. Enter the JC
 transaction’s month in the JC Month field.

1. Enter the transaction in
 the JC Trans field.

1. Select
 Billable or Nonbillable from
 the Bill Status drop-down. The drop-down automatically
 defaults to Billable. Note: If the status is set to Nonbillable, the
 system does not add the amount to the detail sequence’s total amount. The
 transaction remains flagged as non-billable and will not display on
 subsequent billings. If the entire billing is deleted, and later
 re-initialized, the system includes this transaction, which defaults as
 billable.

To delete transaction detail, select the appropriate detail line and click the
 Delete button.
