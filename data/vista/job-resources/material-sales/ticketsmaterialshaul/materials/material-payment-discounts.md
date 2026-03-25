---
title: "Material Payment Discounts | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/materials/material-payment-discounts"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/materials/material-payment-discounts"
---

# Material Payment Discounts

Although discount dates and amounts fields are not included
 on the MS Material Payment Worksheet form, those values will calculate during the batch
 update based on the payment terms for the haul vendor.
Discount Taken amounts display for each
 applicable invoice on the MS Material Vendor Payment AP Audit list. GL distributions
 will be determined by the ‘Post Discounts Offered to GL and Net Amounts to Subledgers’
 option in AP Company Parameters.
The ‘Post Discounts Offered to GL and Net
 Amounts to Subledgers’ option also controls the update to MatlCost in MS Ticket Detail
 (MSTD).
If checked, includes discount:

- Material Taxed: MatlCost = Total
 Cost + Tax Amount – Discount

- Material Not Taxed: MatlCost = Total
 Cost – Discount

If unchecked, excludes discount:

- Material Taxed: MatlCost = Total
 Cost + Tax Amount

- Material Not Taxed: MatlCost = Total
 Cost

For more information about the Post
 Discounts Offered to GL and Net Amounts to Subledgers option, see [About Using Discounts ](/en/vista/vista/accounting/accounts-payable/invoices/taxes-and-discounts/about-discounts) .
Note: The system uses payment terms to calculate due dates
 and discount dates; however, if you specify a due date during initialization, it will
 override the standard due date calculation for all sequences. Because discount dates
 will not recalculate accordingly, it may result in some discount dates falling on or
 after the due date.

Related information

- [About the MS Material Payment Worksheet Form](/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/materials/about-the-ms-material-payment-worksheet-form)
