---
title: "Purchase Order Features | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2021-releases/whats-new-in-vista-2021-r1/costs-and-contracts/purchase-order-features"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2021-releases/whats-new-in-vista-2021-r1/costs-and-contracts/purchase-order-features"
---

# Purchase Order Features

Vista 2021 R1 delivers on user-requested Purchase Order enhancements, fixes, and other improvements.

## Associate Purchase Orders with Job Cost Field Tickets

You can now assign Job Cost field tickets to purchase orders, enabling you to link related costs to specific work activity on a job, and facilitate owner billing.
The following changes were made to enable this functionality

- PO Purchase Order Entry - Added a Ticket field to the PO Items section. This field displays only for purchase order items with a Type of 1-Job. When you enter a job PO item, you can associate the item to a field ticket for the specified job/contract; however, the field ticket must be Open. You cannot post to field tickets with a Closed, Approved, Rejected, or Billed status.

- The PO Receipts Entry - When you receive a purchase order in this form that is associated with a field ticket, the system now shows the field ticket number in the Type field of the informational display.
If you selected the Update GL/Sub-Ledgers on Receipt checkbox in PO Company Parameters, posting a receipts batch automatically creates an entry on the Cost Detail tab of JC Field Ticket, with a Source of PO Receipts. If you did not select the Update GL/Sub-Ledgers on Receipt checkbox, the Cost Detail tab will be updated once you post an invoice for the PO in AP Transaction Entry.Note: When you manually add or initialize a purchase order in AP Transaction Entry or AP Unapproved Invoice Entry, the system includes the field ticket assigned to the PO item. You cannot edit the field ticket number on the invoice, so if you need to change it, you must do so in PO Purchase Order Entry.

For more information about the Field Tickets feature, see [JC Field Ticket Form](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-field-ticket-form).

## Check Issue Status

To see a list of defects fixed in this version, go to the [Track Cases/Issues page](https://support.viewpoint.com/s/browse-cases-and-issues) of the Viewpoint Customer Portal. Use the filter options to select your product and module. In the Fixed in Version field, select this version, then select Apply Filters.
