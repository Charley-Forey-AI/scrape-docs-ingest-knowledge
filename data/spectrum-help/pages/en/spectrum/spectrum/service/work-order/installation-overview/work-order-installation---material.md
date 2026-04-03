---
title: "Work Order Installation - Material | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/service/work-order/installation-overview/work-order-installation---material"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/service/work-order/installation-overview/work-order-installation---material"
---

# Work Order Installation - Material

Use this tab to select the material settings for the Work Order module. These settings can be changed as needed at any time.
Field
Description

Automatically build task detail for material?
Select this checkbox to automatically
 transfer material detail lines from task to task; otherwise, leave this check
 box clear. If this checkbox is selected, material tasks
 set up in the Task File Maintenance window will
 automatically transfer to new work orders set up in Work Order
 Entry if they have a cost detail associated with them.
 Additionally, all material tasks will be listed individually in
 Labor Entry, Material
 Entry, and Other Cost Entry.
 When material transactions are generated for tasks, the
 G/L department will be set from the new G/L department field in the work
 order header.

Automatically build task detail for other charges?
Select this checkbox to automatically
 transfer other cost detail lines from task to task; otherwise, leave this check
 box clear.  If this checkbox is selected, other cost
 tasks set up in the Task File Maintenance window will
 automatically transfer to new work orders set up in Work Order
 Entry if they have a cost detail associated with them.
 Additionally, all other cost tasks will be listed individually in
 Labor Entry, Material
 Entry, and Other Cost Entry.
When other cost transactions are generated for tasks, the
 G/L department will be set from the new G/L department field in the work
 order header.

Default material entries to taxable?
Select this checkbox if materials are
 usually taxable. Leave the box blank if materials on work orders are usually
 not taxable.  When new sites are entered, the option
 selected here will be the default, but either option may be selected at that
 time.

Update cost of goods sold for non-stock material entries?
The system is prompting you to decide
 whether materials "cost of goods sold" should be transferred to Accounts
 Receivable. If this checkbox is selected, the material costs will be posted to
 the A/R invoice files, and subsequently will update to the General Ledger as a
 "cost of goods sold" entry. If Inventory Control module is present in this
 company, material costs will transfer to A/R and G/L only for non-stock items.
 If the Inventory Control module is not present, all
 material costs will be transferred. If this checkbox is not selected, then
 no General Ledger entry will be made for material "cost of goods sold".
 Regardless of entry in this field, cost and profit figures will be recorded
 for the work order.
Cost of goods sold for
 inventory (stock) entries will be unaffected by this checkbox.
Note: If the Inventory Control module is NOT installed, this
 checkbox will affect all material transactions.

Default material entries to show on A/R invoice in detail?
Select this checkbox if you want
 material items to remain separate on the Accounts Receivable invoice. Do not
 select this checkbox if you want to combine material items into a single line
 on the Accounts Receivable invoice labeled 'MATERIAL USED'. The stock and
 non-stock items will be combined unless one of the following conditions exists:


- Lines are assigned to different Work Order G/L Departments.
—OR—

- Lines are assigned to the same department, but the Cost of Goods Sold
 G/L accounts in the Work Order G/L Department file are different for
 material and inventory.

Material markup
This field will default from
 Service Contract Maintenance if a contract # has been
 specified. If the markup field is blank in Service Contract
 Maintenance, then the field will default from Site
 File Maintenance. If the markup field is blank in
 Site File Maintenance, then the field will default
 next from Customer File Maintenance. If the markup field
 is blank in Customer File Maintenance, then the field
 will default from Work Order Installation as a last
 resort. The code entered here will be used conditionally when a new work order
 is added. The markup code entered here will be used when
 the software tries to compute the unit price from the cost of a material
 item when added into Material Entry or the detail
 windows of Purchase Order Entry or Accounts Payable > Invoice/Credit Memo Entry. This optional entry field will only be enabled for 'Site'
 work orders. When calculating the price, the software marks up the cost,
 including any sales and use tax.
