---
title: "Accounts Payable Features | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2023-releases/whats-new-in-vista-2023-r2/accounting/accounts-payable-features"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2023-releases/whats-new-in-vista-2023-r2/accounting/accounts-payable-features"
---

# Accounts Payable Features

Vista 2023 R2 delivers on user-requested Accounts Payable enhancements, fixes, and other improvements.

## Units Required on Unapproved Invoices

When entering unapproved invoices in AP Unapproved Invoice Entry, you must now enter a value in the Units field when the unit of measure is other than LS (Lump Sum).
 For LS items, the Units field auto-defaults to 0.00 and is disabled. But when the unit of measure is other than LS, you must enter an amount that is less than, equal to, or greater than 0.00 (previously, you could leave the Units field blank, which caused errors when adding the unapproved invoice to an AP Transaction Entry batch).

## Require SM Cost Type on SM Work Order Invoice Lines with Tax

If you enter enter an invoice line in AP Transaction Entry or AP Unapproved Invoice Entry for an SM work order (Line Type 8), and the invoice line includes tax (Tax Amt is not 0.00), you are now required to enter a cost type in the SM Cost Type field.
In AP Transaction Entry, if you apply taxes to the SM Work Order line but do not enter an SM Cost Type, an error displays indicating the SM Cost Type is missing and you must enter the cost type in order to save the line.
For unapproved invoices, the SM Cost Type field is not initially required; however, if you apply taxes to the invoice line and do not enter an SM Cost Type, an error displays indicating that the SM Cost Type is missing. The system saves the line, but you must specify an SM Cost Type before you can post the invoice via AP Transaction Entry or AP Unapproved Invoice Posting.

## Check Issue Status

To see a list of defects fixed in this version, go to the [Track Cases/Issues page](https://support.viewpoint.com/s/browse-cases-and-issues) of the Viewpoint Customer Portal. Use the filter options to select your product and module. In the Fixed in Version field, select this version, then select Apply Filters.
