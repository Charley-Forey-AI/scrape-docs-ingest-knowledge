---
title: "Update Work Orders to Invoice Entry - Update Details | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/service/work-order/spectrum-menus-overview/data-entry-overview/update-work-orders-to-invoice-entry/update-work-orders-to-invoice-entry---update-details"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/service/work-order/spectrum-menus-overview/data-entry-overview/update-work-orders-to-invoice-entry/update-work-orders-to-invoice-entry---update-details"
---

# Update Work Orders to Invoice Entry - Update Details

When you transfer a work order to Accounts Receivable,
 Spectrum will recalculate the sales tax based on the effective rate associated with the sales
 tax code. This allows you to set up sales tax rate changes in advance, assuring you that your
 work orders will have the correct sales tax for billing and reporting.
If there is a salesperson code assigned to the work order, this code will be recorded on the A/R invoice during the transfer. If a bill-to code has been assigned to the selected work order site in Work Order Site Address Maintenance, this code will be transferred to the invoice in Accounts Receivable during the update.
Additional protection has been incorporated into the Work Order invoice transfer for users that assign the work order number to be the invoice number. The Work Order to Accounts Receivable transfer update will automatically provide a special window if the invoice number matching the work order number already exists. Within the window, you can then assign a new, unique, invoice number for that work order.
For Work Order users who also track quantities in Inventory Control,
 this screen will update the quantity history figures in the inventory warehouse detail
 file. This results in a quantity-used-by-month table on the Inventory Reorder Report.
An invoice for manufacturer warranties will be created, even if the
 Service Contract module is not present. The software will check to see if the warranty is
 valid, but a contract does not need to be specified in the work order header or detail
 level.
The software will set the work order status to 'Complete' if the selected detail line is set to Yes. If the detail line is set to No or left blank, the status will remain unchanged during this update.
Work orders that contain incomplete task-related transactions can be selected for billing, but the incomplete transaction lines will remain open. If such records are present in the work order, the update will not set the status of the work order to 'Complete'.
Note: Only work orders that have already been printed can be updated;
 unprinted work orders will not transfer to Accounts Receivable. If the selected work order
 has any inventory entries assigned to a warehouse conducting a physical inventory, the
 software will provide the following error message "ERROR: Physical inventory in progress at
 all warehouses - Transfer not allowed".
During each successive update, Other Charge history records will be added to the work order to store the calculation basis, bill # and actual billing amount. This modification is only available for other charge items with a calculation method of 'Hourly', 'Percent of cost' or 'Percent of bill'. Other charge items with a 'Fixed amount' calculation and items originating in General Ledger are billed only once, even if multiple billings are generated for the work order.
This update will set the 'alternate address' and Bill-to address code' columns in the new A/R invoice equal to the corresponding columns in the Work Order Header Table instead of the associated site.
If 'Work completed notes' are present for the particular work order, these notes will be copied into the 'Notes for Customer' box in the More Invoice Information window.
The assigned labor billing code will be transferred from the labor billing transaction to the cost history record.
