---
title: "PO Purchase Order Entry Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-purchase-order-entry-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-purchase-order-entry-form"
---

# PO Purchase Order Entry Form

Use this form to set up and/or modify purchase orders.

Header information is entered in the upper section, which includes additional tabs for entering the shipping address or address overrides. The lower section is used to enter PO items, as well as view the cost data for each item.
You can add purchase orders to a batch manually or by initialization. You an also add previously posted POs to a batch using the (accessed by selecting File > Add Purchase Order).

## Auto-Add Material Notes

Notes entered for materials (in HQ Materials) can be automatically added to items on a PO. When entering a purchase order item, if notes exist for the specified material, the Copy Notes button (to the right of the tax fields) is enabled. Selecting this button automatically adds all notes entered for the material to the notes for the PO item, appending them to any already existing notes.

## Posting Freight

You can enter freight as a single line on any purchase order. This is advisable if freight will be billed from the vendor as a separate item. In this case, treat this as a miscellaneous item on the PO and enter it by skipping the material code, entering Freight as the description, LS as the unit of measure, and entering all other fields in the transaction line as required for that type of PO. You can then either access the original dollar amount field later to enter the freight-billed amount or just enter the amount with the invoice.

## Address Overrides

The Address Overrides tab allows you to override the vendor's standard purchasing and/or payment addresses. In order to use this feature, you must set up at least one additional address for the vendor in AP Additional Addresses. If overriding the purchasing address, the address sequence must have an address type of 'Purchase Order' or 'Both'. The purchase address prints on the purchase order.
 For payment addresses, the address type must be 'Payment' or 'Both'. The payment address is updated to the invoice header (in AP Transaction Entry, AP Recurring Invoices, or AP Unapproved Invoice Entry) when entering PO lines where the purchase order is referenced. However, this address sequence is only used if there is no override address or address sequence already specified in the invoice header and if it is the first PO line on the invoice.

## Field Tickets

Field tickets enable you to link labor, material, and equipment costs related to specific work activity on a job, and facilitate owner billing. When you add job-related items to a purchase order, you can assign each item to a field ticket associated with the contract for the specified job. You can assign multiple purchase order items to a single field ticket, as long as the ticket is open (that is, it has a status of Open). Once the status for a field ticket is set to Closed, Approved, Rejected, or Billed, you can no longer post costs to that ticket.Note: Costs associated with approved field tickets only impact T&M billings; therefore, assigning field tickets to purchase order items for a job is only useful if the job's contract/contract item has a bill type of T&M or Both. For more information about field tickets, see JC Field Ticket.

For more information about field tickets, see [JC Field Ticket Form](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-field-ticket-form).

## SM Work Orders

This type of purchase order is associated with a service work order (work orders created in SM Work Orders). You can create them here in PO Purchase Order Entry (using a line type of 6-SM Work Order) or directly from the work order using SM Purchase Order Entry.
 When you post a PO batch (in either form), the system automatically generates a work completed purchase line in SM Work Orders for each purchase order item that references an SM work order. You can then receive and invoice them as you would any other purchase order.
For information about entering SM purchase orders, see [Entering an SM Purchase Order](/en/vista/vista/service-management/purchase-orders/about-entering-an-sm-purchase-order).

Related information

- [About Calculating Material Costs](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/about-calculating-material-costs)

- [About Tracking Compliance](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/about-tracking-compliance)

- [Pay Type/Pay Category](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/pay-typepay-category)

- [About Committed Costs](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/about-committed-costs)

- [PO Shipping Locations Form](/en/vista/vista/costs-and-contracts/purchase-order/setup-and-maintenance/po-setupmaintenance-forms/po-shipping-locations-form)
