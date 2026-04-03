---
title: "Inventory Transaction Report / Update | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/materials/inventory-control/spectrum-menus-overview/data-entry-overview/inventory-transaction-report--update"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/materials/inventory-control/spectrum-menus-overview/data-entry-overview/inventory-transaction-report--update"
---

# Inventory Transaction Report / Update

This screen provides information on transactions that have
 not yet been updated: job requisitions, receipts, credit returns, transfers, adjustments,
 sales, usage, and/or items on order.
 The reports should be reviewed for
 accuracy, and if correct, saved as permanent records of the company. Additional
 transactions should not be entered while these reports are printing and updating.
Quantities posted into the Job Cost balance file will also be posted into the Job Cost quantity history file. This file is then used for the Job Productivity Report and Job Unit Cost Report to calculate the week-to-date quantity figures. The corresponding inquiry screens also include these quantities.
When the quantity detail is updated in the Inventory Item Warehouse Detail File during the Transaction Update, the software combines the quantity for the transaction being updated with the existing quantity bucket if the 'last-in' cost exactly matches. Likewise, if a transaction includes a negative entry (such as a return from job), the quantity buckets will be combined if the 'last-in' cost is the same as the return. Otherwise, in both cases, a new negative quantity-on-hand bucket is recorded at the applicable cost basis. The Inventory Transaction reflects estimated costs of the Inventory Warehouse while generating G/L transactions and posting to Job Cost and Equipment Control.

- If the Post to job cost history
 in detail checkbox is selected in the J/C Cost Type File
 Maintenance screen, the job cost history records will be updated with
 one history record per requisition transaction line. For example, if a requisition
 contained multiple lines for the same item on the same job, phase, and cost type,
 each requisition transaction line will be separated out in history rather than being
 summarized into one history record. If the cost type being posted is not set for
 detail posting, then one history record will be created per item on the requisition
 per job, phase and cost type. Additionally, the software checks the source and
 destination company's inter-company accounts to see that the G/L account code
 Direct cost option is
 set to No direct cost in
 G/L Master File Maintenance.

- If the Post requisition to
 General Ledger as internal job sale? checkbox is selected in
 Inventory Control Installation, do not make the Job Markup
 a credit entry. Instead, read the columns in G/L Inventory Department table for the
 assigned G/L account codes. The Cost of Goods Sold will be a debit entry, and Job
 Sales will be a credit entry.

- If the G/L account is set to 'Direct equipment cost', the Equipment code and
 Cost category code will be updated from the invoice distribution line.
Important: These reports should be retained as a permanent audit
 record of the company. After the report has printed, the update will adjust
 quantities on-hand and on-order, and will create records in the inventory history
 file. This update will also prepare entries for the General Ledger; the debit and
 credit entries will be included on the next Inventory G/L Summary Report that is
 printed. The Job Cost and Time + Material files will also be updated. When
 multi-company job requisitions are updated to Job Cost history, both the item
 description and company code is stored in the Job Cost history file. This provides
 additional detail information for multi-company operations when using Job Cost
 reports and inquiry screens.
Note: Regarding Sub Jobs — If this is a sub-job billed
 from a master job, the software will read for job-specific setup rates for the master
 job, and if none are found use standard settings. If this is a sub-job billed at the
 sub-job level, the software will read for job-specific setup rates for the sub-job
 first, and if billing rates are not found then the master job, and if none are found
 there use standard settings.
Note: Regarding Standard Cost costing method — During
 this update, if the item is configured to use the 'Standard Cost' costing method and
 there is no quantity on hand in the warehouse and the warehouse-specific standard
 cost is blank, then the unit cost will be written to the Warehouse standard cost
 column of the Item Warehouse Table.

- For receipt transactions, store the quantity and current 'Standard cost' of
 the receipt for the item in the Warehouse Quantity Table. If there is no quantity on
 hand, assign the warehouse-specific 'Standard cost' and otherwise, store the standard
 cost from the Item Master Table.

- For transfer transactions, instead of storing the same cost that came out of
 the 'From warehouse,' assign the standard cost of the 'To warehouse.'

- For mix transactions, the quantity of the mix item (finished product) will be
 added to the warehouse at the warehouse-specific 'Standard cost' of that item (not
 the sum of the components).

- For cost adjustment transactions, after figuring the new unit cost of the cost
 adjustment, set the warehouse-specific 'Standard cost' to the same unit cost stored
 in the Warehouse Quantity Table.

- For adjustment transactions, when the quantity on-hand goes negative Spectrum
 will look for the warehouse-specific 'Standard cost' instead of from Item Main
 Properties during the update. If blank at the warehouse level, spectrum will read for
 the standard cost in Item Main Properties.
Note: Regarding Inventory Transfers and G/L Codes —
 Inventory transfers do not update the General Ledger because the inventory item is
 not changing value, it is simply moving from one warehouse to another. In the
 Materials Management module you can have scale tickets that are transfers, and this
 G/L account is used on the freight cost update as the location for freight charges
 related to the transfer.

Related information

- [Inventory G/L Report/Update](/en/spectrum/spectrum/materials/inventory-control/spectrum-menus-overview/data-entry-overview/inventory-gl-reportupdate)

- [Inventory Transaction Report](/en/spectrum/spectrum/materials/inventory-control/spectrum-menus-overview/data-entry-overview/inventory-transaction-report--update/sample-reports---inventory-transaction-report/inventory-transaction-report)

- [Job Requisition Transaction Report](/en/spectrum/spectrum/materials/inventory-control/spectrum-menus-overview/data-entry-overview/inventory-transaction-report--update/sample-reports---inventory-transaction-report/job-requisition-transaction-report)
