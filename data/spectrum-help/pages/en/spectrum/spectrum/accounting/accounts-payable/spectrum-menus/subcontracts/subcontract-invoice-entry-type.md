---
title: "Subcontract Invoice Entry Type | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/subcontracts/subcontract-invoice-entry-type"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/subcontracts/subcontract-invoice-entry-type"
---

# Subcontract Invoice Entry Type

 If a subcontract # has been specified, the Subcontract Invoice Entry Type window
 displays. Slightly different offerings display in this window based on whether the subcontract
 is fixed price or unit price.
The Release retention option allows you to
 reclassify retention on subcontract invoices on zero-dollar invoices (for example, when
 recording an invoice with no additional expense incurred). If this option is selected, an
 additional the Amount to release field displays where you can enter
 a (positive) value, less than the outstanding retention balance. When you click Continue, the invoice is generated and
 the retention amount will show up as a negative value, resulting in a zero-dollar entry in
 the Retention amount field.
Rules for Retention Release Invoices

- The 'Total amount' of a retention release invoice is always zero.

- You are allowed to change the Retention amount field.
 Here, the number must be entered as negative to create the reclass invoice. The field
 is validated to not allow entry of a negative value greater than the retention
 already withheld.

- The label Retention release displays next to the Subcontract field as a visual clue
 about the invoice.

- A zero dollar transaction line will display in the distribution section of the
 invoice. By rule, retention release invoices may only have one distribution record.
 If you attempt to add another line, you will receive an error message stating "ERROR
 – Retention release invoice, only one detail line required."

- Credit memos using the retention release feature are not allowed.

- Pay-when-paid and instant check/credit card options are not available on a retention release invoice.

- Retention release invoices cannot be reversed. This is similar in how a zero dollar invoice is treated.
