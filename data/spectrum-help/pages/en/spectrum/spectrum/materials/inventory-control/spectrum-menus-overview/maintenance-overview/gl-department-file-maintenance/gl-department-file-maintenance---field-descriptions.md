---
title: "G/L Department File Maintenance - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/materials/inventory-control/spectrum-menus-overview/maintenance-overview/gl-department-file-maintenance/gl-department-file-maintenance---field-descriptions"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/materials/inventory-control/spectrum-menus-overview/maintenance-overview/gl-department-file-maintenance/gl-department-file-maintenance---field-descriptions"
---

# G/L Department File Maintenance - Field Descriptions

Use the table below for reference when completing the fields on this screen.
Field/Button
Description

Department code
Enter an inventory General Ledger department code. If you are editing or viewing a department code, changes cannot be made to this field.
Default Hierarchy for Department Codes
The system first looks to the Category File Maintenance
 for the G/L department code. If the field is blank there, the software will
 then look to the Warehouse File Maintenance. If this is
 also blank, the user will be prompted to enter a valid code.

Description
Enter the description for this code, or press Enter to accept the corresponding department code description.

G/L accounts

Sales
Enter the General Ledger account code to be used to post sales transactions. G/L accounts with a status of 'Not Used' are not allowed. The corresponding description displays to the right of this field.

Job sales
If the Post requisition to General Ledger as internal job sale? option is selected in Inventory Control Installation, the Job sales G/L account will be used in place of Job markup.

Cost of sales
Enter the General Ledger account code to be used to post the cost of sales. G/L accounts with a status of 'Not Used' are not allowed. The corresponding description displays to the right of this field.

Inventory value (non-stock)
Enter the General Ledger account code to be used to post inventory or non-stock inventory values. G/L accounts with a status of 'Not Used' are not allowed. The corresponding description displays to the right of this field.
When users are performing stock transactions, they are debiting inventory when receiving it, and crediting inventory when it is sold or used on a job. However, if it is a non-stock transaction, the G/L code entered here is still debited when the non-stock item is received, and credited when sold or used on a job. This field is simply an offset account for non-stock mixes. When using this field for non-stock items, the software will debit whatever G/L account code is entered here, just like for stock items. If the user has both non-stock and inventory items, he or she should set up several G/L departments for the inventory types and one for the "non-stock" G/L department.

Adjustments
Enter the General Ledger account code to be used to post adjustments to inventory. G/L accounts with a status of 'Not Used' are not allowed. The corresponding description displays to the right of this field.

Cost adjustments
Enter the General Ledger account code to be used to post adjustments to standard cost. The corresponding description displays to the right of this field.

Receipts
Enter the General Ledger account code to be used to post receipts. G/L accounts with a status of 'Not Used' are not allowed. The corresponding description displays to the right of this field.

Job markup
Enter the General Ledger account code to be used to post job cost markups. G/L accounts with a status of 'Not Used' are not allowed. The corresponding description displays to the right of this field.

Job cost
Enter the General Ledger account code to be used to post job cost direct costs. G/L accounts with a status of 'Not Used' are not allowed. The corresponding description displays to the right of this field.

Mix usage
Enter the General Ledger account code to be used to post mix usage costs. G/L accounts with a status of 'Not Used' are not allowed. The corresponding description displays to the right of this field.

Equipment cost
Enter the General Ledger account code to be used to post equipment costs. G/L accounts with a status of 'Not Used' are not allowed. The corresponding description displays to the right of this field.

Transfers
Enter the General Ledger account code to be used to post transfers. G/L accounts with a status of 'Not Used' are not allowed. The corresponding description displays to the right of this field.

Scale transfer freight variance
Enter the General Ledger account code to be used to post scale transfer freight variance items. G/L accounts with a status of 'Not Used' are not allowed. The corresponding description displays to the right of this field.
You can enter freight and miscellaneous charges in the Inventory Control module. These costs will be allocated to each item in the transaction based on quantity. Use this field to transfer new costs to the General Ledger module.

Scale receipt freight variance
Enter the General Ledger account code to be used to post scale receipt freight variance items. G/L accounts with a status of 'Not Used' are not allowed. The corresponding description displays to the right of this field.
You can enter freight and miscellaneous charges in the Inventory Control module. These costs will be allocated to each item in the transaction based on quantity. Use this field to transfer new costs to the General Ledger module.
