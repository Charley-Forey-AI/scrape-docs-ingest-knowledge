---
title: "Inventory Sales | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/tickets/ticket-entry/inventory-sales"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/tickets/ticket-entry/inventory-sales"
---

# Inventory Sales

This type of sale is used to record materials and hauling posted to another inventory location, either within your own company or to a sister-company.
Do not use this program if you are only transferring a material from one location to another. Although they may seem similar in some respects, sales to inventory and material transfers are not the same. Material transfers are performed in IN Transfer Entry, and are used only for transferring materials from one location to another within the same company. The transfer creates a General Ledger entry that updates the Inventory accounts for each location.
When posting sales to Inventory, the specified material must be stocked at the destination location. The selling location has the option to either sell the material from its own stock, or to direct purchase the required material from a vendor, even if it does not normally stock the material.
Pricing and haul rates follow the standard
 hierarchy.
Non-stocked materials are priced in the same manner with the exception that the Pricing Option does not apply. If the material does not exist on a quote or price template, the unit price is pulled from HQ Materials, and no markup/discount rates are used. If you normally discount or markup unit prices in this type of situation, you can use the system calculator to figure your markup or discount amount and then enter the resulting unit price manually.

## General Ledger Implications

When posting inventory sales, the
 General Ledger entries are determined by whether you are posting inventory sales in
 the same company, or whether you are posting sales to a sister-company, and if so,
 whether intercompany invoices are used. If selling to inventory locations in the
 same company, or cross-company and not using intercompany invoices, all of the
 necessary accounting is made to relieve Inventory and record sales revenue. If you
 are selling the materials to a sister-company, additional journal entries are made
 to the intercompany AR and AP accounts. If using intercompany invoices,
 cross-company sales are treated as a customer sale. An invoice is created, and the
 journal entries will be the same as those made for a customer sale. Sales to
 inventory will not be recorded until the intercompany invoice is updated in AP. See
 Intercompany Invoicing in Related Topics below for information about creating
 invoices for sales to sister companies.
If posting taxes or freight charges to
 inventory sales, the “Burdened Unit Cost - Include AP Misc Amt and Tax” option in IN
 Company Parameters determines how tax is updated to GL for the destination location.
 If burdened, tax and freight charges are included in the material total and updated
 to the Inventory account for the destination location. If not, tax and freight
 charges are updated to GL using the Misc GL Account (freight) and Tax GL Account
 (taxes) specified in IN Company Parameters for the destination location. Tax and
 freight charges are always updated to separate GL accounts for the “selling”
 company, regardless of how burden is posted. The system uses the GL Account
 specified in HQ Tax Codes for the tax amount and haul amounts (freight charges) are
 updated to the haul accounts specified for the “selling” location.
Override accounts can be defined for the
 Cost of Goods, Inventory, and Inventory Sales accounts (by company, category, and/or
 company/category); therefore, the system will use a hierarchical search to determine
 which account to use. If no overrides exist, the accounts specified in the IN
 Locations are used. For more information, refer to the online help for Inventory.
The following diagrams illustrate the
 General Ledger updates that occur when sales to Inventory transactions are posted.

## GL Implications for Value Added Tax Transactions

If you are posting Goods and Services
 Tax (GST) and/or Provincial Sales Tax (PST), the update to GL will credit the
 appropriate GST and/or PST tax payable accounts (i.e, the Credit GL Account defined
 in HQ Tax Codes). If you are tracking Income Tax Credits (ITC), the GST amount is
 deducted from the job expense and debited to the Debit GL Account specified for the
 GST tax code in HQ Tax Codes. If not tracking ITC, the GST amount is included in the
 job expense and no update to the Debit GL Account occurs.
If Burdened Unit Cost is Y
If Burdened Unit Cost is N
