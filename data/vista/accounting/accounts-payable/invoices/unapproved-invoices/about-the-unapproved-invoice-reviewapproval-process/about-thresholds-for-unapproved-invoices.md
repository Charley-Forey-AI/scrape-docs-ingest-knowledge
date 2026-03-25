---
title: "About Thresholds for Unapproved Invoices | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/about-the-unapproved-invoice-reviewapproval-process/about-thresholds-for-unapproved-invoices"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/about-the-unapproved-invoice-reviewapproval-process/about-thresholds-for-unapproved-invoices"
---

# About Thresholds for Unapproved Invoices

Thresholds provide a way to limit the number of invoices assigned to reviewers by setting a minimum invoice amount.
 As long as the
 Gross
 amount is over the reviewer's threshold amount, the reviewer is added to all lines. If the
 Gross
 amount is less than the reviewer's threshold amount, the system does not add the reviewer to any invoice lines.
Note: The header has
 two amount figures. One is Gross, a display-only field in the header's
 top right, and the other is Invoice Total, an entry field located in the
 header's bottom right. They are not always the same amount. The amount in the Invoice Total field
 is the sum of the Gross amount and all other amounts also shown nearby in the top of the header
 display.
If you want the system to ignore the invoice

 Gross
 amount and instead assign threshold reviewers to individual lines based on
 the line amounts, you can select the Apply Reviewer threshold amount at line level check
 box in the HQ Reviewer Group form (Info tab). With this checkbox selected, the system adds the
 reviewer to the line only if the amount in the line’s
 Gross
 field is equal to or greater than the threshold amount; if the invoice
 line's gross amount is less than the threshold, the system does not add the reviewer.
You should be aware of the following as you work with thresholds:

- The system is designed to control invoice
 assignment based on minimums (thresholds) only, and not on limits.

- The system never adds reviewers with
 thresholds to the header Reviewers tab, regardless of any header or line amount or group
 setting.

- Threshold rules only apply to reviewers who
 are members of the group that is assigned to the invoice line or header.

- If the threshold amount for a reviewer is
 not satisfied, the system may assign the reviewer to the invoice anyway if you have
 assigned that reviewer to the vendor/job/equipment/etc.

- Increases to existing invoices' header or
 line amounts that push the amount across a threshold prompt the system to update the
 Reviewers tab accordingly and add reviewers who meet the threshold amounts.

- Reductions to existing invoices' header and
 line amounts prompt the system to remove reviewers if the new amount falls below the threshold amount
 assigned to the reviewer.

- A reviewer with a threshold who needs to
 review a credit invoice can be assigned manually to the invoice line(s). An alternative
 option is to create a separate reviewer group without thresholds which can be assigned to
 invoices of less than $0.00.
