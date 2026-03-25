---
title: "Purchases from Material Vendors to Inventory | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/tickets/ticket-entry/purchases-from-material-vendors-to-inventory"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/tickets/ticket-entry/purchases-from-material-vendors-to-inventory"
---

# Purchases from Material Vendors to Inventory

This type of transaction is used when a material is purchased
 from an outside vendor to stock your own inventory or the inventory of a sister company.

Since you must specify the location from which a
 material is sold, you will first need to set up a dummy location in IN Locations to
 represent the vendor location. Make sure to set up the dummy location with Inventory
 Sales, Haul Revenue, and Haul Expense accounts. The Inventory Sales account should be a
 payables account such as Material Vendors Payable.
When posting the ticket, enter the dummy location as the From Location, specify the Mat’l Vendor, and set the Sale Type to Inventory. Then enter the appropriate destination Inventory company and location.
When posting this type of transaction, the General Ledger entries are handled just like a standard Inventory sale. However, in place of the standard Inventory Sales account set up by location, you may want to substitute a Material Vendors Payable account (as discussed above). This account is debited when invoices are received for the materials and processed in AP.
The diagram below illustrates the General Ledger updates that occur when this type of purchase transaction is posted.
