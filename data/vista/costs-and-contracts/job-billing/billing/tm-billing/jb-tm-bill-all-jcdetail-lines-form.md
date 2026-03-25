---
title: "JB T&M Bill All JCDetail Lines Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-bill-all-jcdetail-lines-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-bill-all-jcdetail-lines-form"
---

# JB T&M Bill All JCDetail Lines Form

Use the JB T&M Bill All JCDetail Lines form to review the
 job cost transaction detail for an entire billing.
Access this form from JB T&M
 Bill Edit by selecting File > Job Cost
 Detail. When opened, this form automatically defaults to the
 currently selected detail sequence line and the grid displays all of the JC
 transactions that comprise this sequence.

## Cost Transaction Detail

You can view cost
 transaction details by expanding the Cost Transaction Detail section
 above the grid (click  button). Clicking on each detail
 line displays the cost detail for that line. The cost detail shown
 differs depending on the line's transaction type. For example, a PR
 line will show the Employee, Craft, Class, Factor, and Shift info,
 while an EM line will show the EMCo, Equipment, and Revenue Code
 info.
If you are using billing
 categories (that is, you selected the Labor, Equipment, and/or
 Material Categories checkboxes on the T&M template), you can
 see the billing category assigned to a sequence (in JB T&M
 Template) by selecting the detail line and pressing Ctrl +
 A.Note: In order to see
 the billing category for a detail line, you must first
 expand the Cost Transaction Detail section.

## Adding Transaction Details to Sequences

This form does not allow transaction editing; you can only add, delete,
 or mark transactions as billable. When adding a JC transaction to
 the sequence, the detail must match the detail requirements defined
 for the template sequence (e.g., source, summary and sort options,
 cost type, etc.) prior to initialization. If the transaction’s
 detail does not match the requirements, a warning displays. If the
 transaction does match the requirements, the system adds the
 transaction amounts (Units, Amount) to the detail sequence
 totals.
You can add transaction detail to sequences using one of the following
 methods:

- Manually entering the JC Month and JC transaction in the
 grid

- Using the JB T&M JC Detail Fill Grid form, accessed
 by clicking the Refresh Cost
 Detail button. When using this method,
 the system adds all of the JC Detail for all lines
 and sequences. For more information, see [Add JC Cost Detail to a T&M Billing](/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/add-jc-cost-detail-to-a-tm-billing).

Regardless of which method you use, the system automatically
 sets the transaction to Billable. If the transaction is not
 billable, deselect the Billable checkbox. However, if you set the
 status to Non-Billable, the system does not add the amount to the
 detail sequence’s total amount. The transaction remains flagged as
 non-billable and will not display on subsequent billings. If the
 entire billing is deleted, and later re-initialized, the system
 includes this transaction, which defaults as billable.Note: A
 transaction’s Unit Price does not update the sequence’s Unit
 Price. Additionally, the transaction’s units only update the
 sequence’s units if the unit of measure is the
 same.

To delete transaction detail, select the appropriate detail line and
 click the Delete button.

Related concepts

- [JB T&M JC Detail Fill Grid](/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-jc-detail-fill-grid)

- [JB T&M Bill Edit Form](/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-bill-edit-form)

- [JB T&M Bill JCDetail By Seq Form](/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-bill-jcdetail-by-seq-form)
