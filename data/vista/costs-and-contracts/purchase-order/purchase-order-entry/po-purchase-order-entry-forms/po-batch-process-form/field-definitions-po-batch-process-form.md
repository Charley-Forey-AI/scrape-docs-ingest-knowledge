---
title: "Field Definitions: PO Batch Process Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-batch-process-form/field-definitions-po-batch-process-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-batch-process-form/field-definitions-po-batch-process-form"
---

# Field Definitions: PO Batch Process Form

The following is a list of field descriptions for the PO
 Batch Process form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Audit Reports

Prints the distribution information from the batch sorted according to updates to other modules.

- Batch List - Prints the entries in the batch in sequence order.

- Job Cost Distribution - Prints the JC Distributions List for the current batch. Data shown will be based on the batch you are processing. For example, if processing a batch of purchase orders, the list will show the PO#, vendor, material, current units, committed units and unit cost, and phase/CT. If processing a batch of purchase order receipts, shows the changes to PO received and backordered units, JC received units and costs, and JC committed units and costs.

- Inventory Distribution - Prints the PO IN Distribution List (PO Entry) or PO IN Receipts Distribution List (PO Receipts Entry). Depending on the batch type, information may include vendor, purchase order, purchase order item, change units, std unit of measure, location, material, and units backorder, received not invoiced, and on order.

- Error List - Lists the sequence number and the error message for any entries where errors were found in the validation process. You must correct the errors before you can post the batch.

Note: It is recommended that you print the audit lists before you post a batch because once you post the batch, the audit lists are no longer available.
Note: Users who have access to batch processing forms do not automatically have access to the related audit reports. It is recommended that if they will be processing batches, you give them access to the related audit reports using VA Report Security. If users do not have access, they will receive an error message when trying to preview/print those reports to which they do not have access. In addition, if using the ‘Attach Batch Report to HQ Batch Control’ feature (assigned in PO Company Parameters), restricted access to one or more audit reports will prevent the user from posting the batch.
