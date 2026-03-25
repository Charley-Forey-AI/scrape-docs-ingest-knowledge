---
title: "Sales of Non-Stocked Materials | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/tickets/ticket-entry/sales-of-non-stocked-materials"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/tickets/ticket-entry/sales-of-non-stocked-materials"
---

# Sales of Non-Stocked Materials

This type of transaction is used when non-stocked materials are sold to a job, customer, or inventory location other than your own.
These materials may exist in your own inventory, but for purposes specific to this type of transaction, the materials will be supplied by a material vendor.
When entering a ticket, you specify a material vendor and the material being sold. The material must be set up in HQ Materials; however, regardless of whether the material is stocked or not, if a material vendor is specified, the system will always assume the material is not coming from stock.
Pricing and haul rates follow the standard hierarchy discussed earlier, except that with non-stocked materials, the Pricing Option does not apply. If the material does not exist on a quote or price template, the unit price is pulled from HQ Materials, and no markup/discount rates are used. Refer to Material Pricing in Related Topics below for more information.

## General Ledger Implications

When posting this type of transaction,
 because the material is assumed non-stocked, Inventory is not reduced and no
 associated GL distributions are made. Revenue is recognized with ticket batch or
 invoice posting, but no costs are recorded.
The diagram below illustrates the
 General Ledger updates that occur when this type of purchase transaction is posted.
