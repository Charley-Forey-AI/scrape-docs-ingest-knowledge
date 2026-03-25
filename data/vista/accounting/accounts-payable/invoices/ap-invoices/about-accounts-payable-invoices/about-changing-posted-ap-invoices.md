---
title: "About Changing Posted AP Invoices | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/about-accounts-payable-invoices/about-changing-posted-ap-invoices"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/about-accounts-payable-invoices/about-changing-posted-ap-invoices"
---

# About Changing Posted AP Invoices

You can change invoice details using AP Transaction Entry, but the changes you can make depend on whether the invoice has been paid or not.
Note: (Australian and Canadian users) For more information on deleting on-cost invoices, see [About Deleting On-Cost Invoices](/en/vista/vista/accounting/accounts-payable/invoices/on-cost-invoices/about-deleting-on-cost-invoices).

## Unpaid Invoices

If you have not yet paid an invoice, you can make changes to the invoice, including deleting the invoice or lines on the invoice. You must first add the invoice/transaction into an AP Transaction Entry batch (via File > Add Transaction). In order to proceed, the invoice/transaction must have been posted in the same month as the current batch.
Note: If you are updating the Vendor or APRef for an invoice, you must add all invoice lines into the batch.

After you have added the invoice into the batch, you can make changes to both header and line detail. Although you can change most of the information on a posted invoice, you cannot make changes to the invoice if it has been split for partial payments in the AP Payment Control Detail form.
Once you have completed the necessary changes, you can post the batch as normal.

## Paid Invoices

You can make limited corrections to paid invoices without having to void checks and reopen the invoices. You must first add the invoice/transaction into a AP Transaction Entry batch (File > Add Transaction). The invoice must have been posted in the same month as the current batch. Paid invoices are identified by a red “PAID” notice that displays in both the header and lines sections of form.
Once you have pulled the invoice into the batch, you can make changes to header and line detail. However, changes are limited as follows:

- Header - The following options are available for modification in the header.

- AP Reference

- Description

- Invoice Date

You cannot make changes to any of the payment information on the Payment Info tab (for example, hold code, pay method, CM account, check #, EFT Fed Tax Payment info, Child Support Payment info, and so on), nor can you make changes to any information on the Address Override & 1099 Info tab.

- Lines - Allowed line changes are based on line type:Job
Inventory
Expense
Equipment
EM Work Order
SM Work Order*

JC Co
IN Co
Material
EM Co
EM Co
SM Co

Job
Location
Description
Equipment
Work Order
SM Work Order

Phase
Material
GL Co
Comp Type
WO Item
Scope

CT
Description
GL Account
Component
Cost Type
SM Cost Type

Material
GL Account

Cost Code
Material
JC Cost Type

Description

Cost Type
Description
Material

Material

Description

You can only change the Material for a line if the UM field value does not change. In other words, the unit of measure specified for the old material must be a valid unit of measure for the new material.
You cannot change any information for PO or SL lines.Other information that cannot be changed (for any line) includes the UM, Units, Unit Cost, ECM, Supplier, Pay Type, Gross, Freight/Misc, Inc, Tax Type, Tax Code, Tax Basis, Tax Amt, Ret%, Retainage, Disc%, or Discount.
*Changes to the information for an SM Work Order line (as indicated above) update the associated work completed miscellaneous line in SM Work Order. If you change the SM Co and/or work order, the system generates a new work completed miscellaneous line for the specified SM Co and/or work order and removes the work completed line from the previous SM Co/work order. Note: If the previously posted invoice has a Job line, the system posts change to the closed revenue account defined for the contract item's department (Closed Revenue Acct field, JC Departments form)

You can add new lines to a paid invoice if needed; however, you must adjust the Invoice Total to reflect the addition of the new line. Adding a new line changes the status of the invoice to "Open" and allows the new line to be pulled into a payment batch.
Once you have changed the necessary information or added new lines, post the batch as normal.
Existing payment history information within AP retains the original values for AP Reference, Description, and Invoice Date. Changes to information for a paid transaction is not updated in payment history information.
