---
title: "Use Tax | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/purchase-order/procedures-overview/in-depth-overview/use-tax"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/accounting/purchase-order/procedures-overview/in-depth-overview/use-tax"
---

# Use Tax

In some states, vendors do not charge tax on the invoice,
 but companies should still pay the vendor tax. Items may be considered taxable on a
 phase-by-phase basis.
The same items may be taxable on some phases, but not on others depending on how they are
 used and state tax laws.
The Accounts Payable Use Tax Report can be run for either sales or use tax, in detail or in summary.
Open commitments do not include tax amounts for either sales or use tax.

## Purchase Order

Sales tax codes default in Purchase Order Entry from the vendor file. Sales and use tax codes are changed by item code on the tax % field on the Purchase Order Detail window. Neither tax will increase the extension of the line items, but sales tax amounts appear at the bottom of the page, along with taxable and non-taxable purchase amounts. If the vendor has a use tax code in its master file, delete the sales tax code and rate fields in the P.O. header. If use tax codes need to be used on a P.O., the codes need to be entered line item by line item in either the Details page of P.O. entry, in P.O. invoice receiving, or in invoice entry after the invoice has been transferred to A/P.
When importing purchase orders, if no tax code is specified in the import file, then tax codes will be assigned based on the default hierarchy used in the [Purchase Order Entry](/en/spectrum/spectrum/accounting/purchase-order/spectrum-menus/data-entry-overview/purchase-order-entry) page.

## Job Cost

If use tax tracking is not needed, deselect the Utilize tax classification checkbox on the Job Cost Installation page. Job File Maintenance will then reflect the A/R sales tax codes.
If the Utilize tax classification checkbox on the Job Cost Installation page is selected, the Job File Maintenance asks for a tax class code. Set up the tax classification codes in Job File Maintenance. The tax class code has both the A/R sales tax code and the A/P tax codes, either sales or use. The A/P Tax Exemptions is used to set taxable status by cost type, with exceptions being noted by phases (for example, M=N not taxable, materials would not be taxable except for phases listed in the window). If no items are exempt, no exemptions need to be listed here.
Purchase orders entered against the job use this file to determine tax codes to be used. If there are multiple tax codes that apply to a particular job, the different rates must be manually entered in Purchase Order Entry.

## Purchase Order Hierarchy

If the purchase order is charged to a job and the Utilize tax classification checkbox is selected on the Job Cost Installation page with the By job defaults option selected, the software looks first to Job File Maintenance to see if there is a tax class code entered. If there is a tax class code, tax is calculated based on that information for items that are identified as taxable. If no tax class code is in Job File Maintenance, the software will then look to the main page of Purchase Order Entry to determine tax codes to be used, if any. If left blank, the default will come from the P.O. Installation page. For non-job purchase orders, the software will look to the main page of Purchase Order Entry for tax codes to be used, if any. If left blank, the default will come from the P.O. Installation page. The Purchase Order Installation page includes a field for use in specifying a default use/sales tax code for purchase orders. This tax code will default automatically onto new purchase orders when there is no specific tax code designated for the vendor or Job Cost tax classification designated for the job. The installation field may be left blank if a default tax code is not desired.
Job Purchase Orders - use tax shows as non-taxable, and the line item totals will not change, but the tax rate displays. The vendor's sales tax rate is overridden on the P.O. by the job tax rate.

## PO Table 1: "default = Job" in Job Cost Installation

Steps
Taxable (Y/N) is set
Tax code is set

1. On Purchase Order Entry, check the main page to see if there is a tax code set.
 X
X

2. Override the tax if the job has a tax class code, then read the tax class file for the A/P tax.
X
X

3. Override the tax flag if the cost type has an exemption in tax class file.
X

## PO Table 2: "default = Vendor" in Job Cost Installation

Steps
Taxable (Y/N) is set
Tax code is set

1. If the job has a tax class code, then read the tax class file for the A/P tax.
X
X

2. Override the tax flag if the cost type has an exemption in tax class file.
X

3. Override the tax flag if the phase has an exemption in tax class file.
X

4. Override the tax code if there is a tax code set in the Purchase Order Entry (main page), and set the taxable flag to Y if it is not yet set based on Job Classification.
X
X
