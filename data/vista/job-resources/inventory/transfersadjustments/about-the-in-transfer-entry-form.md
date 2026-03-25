---
title: "About the IN Transfer Entry Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/inventory/transfersadjustments/about-the-in-transfer-entry-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/inventory/transfersadjustments/about-the-in-transfer-entry-form"
---

#  About the IN Transfer Entry Form

Use this form to post inventory transfers and to track
 movement of inventory between locations.
This form can only be used if multiple locations are set up on the system.
Transfers will update the On Hand field (IN Location
 Materials) for both the source and destination locations. Last and Average unit costs
 will be updated at the destination location if the transfer date is equal to or later
 than the material’s last purchase date (i.e. Last Cost Update) at that location.
The values of location transfers posted in this form
 are based on the Cost Method specified in IN Locations or IN
 Location Category Override.
General Ledger entries are made by debiting the
 destination location’s Inventory account and crediting the
 source location’s Inventory account (as specified in IN
 Locations or IN Location Category Overrides). Refer to the
 following diagram for an example of a GL entry for a transfer.

 Transfer From:
 Location #1

 Transfer To:
 Location #2

 Units:
 5

 Unit Cost:
 $100.00

Debit
Credit

 $100
 $100

 Destination Location Inventory Account
 Transferring Location Inventory Account

Note: When using this form, transactions can only be edited in an open batch. Once the batch is posted, transactions cannot be edited; adjusting entries will have to be made.
