---
title: "G/L Department File Maintenance - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/service/work-order/spectrum-menus-overview/maintenance-overview/gl-department-file-maintenance/gl-department-file-maintenance---field-descriptions"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/service/work-order/spectrum-menus-overview/maintenance-overview/gl-department-file-maintenance/gl-department-file-maintenance---field-descriptions"
---

# G/L Department File Maintenance - Field Descriptions

Use the table below for reference when completing the fields on this screen.
Field/Button
Description

G/L department
Enter a departmental code for this
 department.
Description
Enter a description for this
 department.
Direct job cost?
Select this checkbox if this
 department will be used for work orders charged to jobs.
Labor G/L accounts

Payroll department
Enter a valid payroll department, as
 defined in Payroll Department Expense Maintenance. If labor hours are updated
 to Pre-Time Card Entry, entry in this field determines where those hours will
 post. It is recommended that you use a Direct work order cost
 department, because non-direct cost departments (such as Admin)
 update to Payroll without including the work order number, equipment,
 component, and contract information. The direct cost
 designation above must match the direct cost designation in Payroll
 Department Expense Maintenance for this department.

Labor sales
Enter a valid G/L code indicating where
 labor charged to the customer will be credited as revenue. The No direct cost
 option must be selected in G/L Master File Maintenance screen for this account.
  If the labor sales G/L account code is set to
 Not used, it
 cannot be selected in this field.

Cost of sales debit
Enter a G/L account code. The labor
 cost of sales will post to the General Ledger if labor hours are entered during
 Labor Hours Entry and charged to the customer. If the actual payroll cost of
 those labor hours has already been posted as an expense through payroll
 processing, this entry provides a method of reflecting labor hours that have
 been allocated to Work Order Entry. This account code defines where in the
 General Ledger this is reflected. The General Ledger account code entered here
 must have the same direct cost designation as the "direct cost" box above on
 this screen.  If the Work Order Installation Post labor cost checkbox
 is clear, entry in this field is irrelevant. If the user is posting to the
 General Ledger, then the payroll department is irrelevant. Ordinarily one
 would not want to post labor cost of sales to the General Ledger both from
 Work Order and through Payroll processing.
 If the
 cost of sales G/L account code is set to Not used, it cannot be
 selected in this field.
If the 'Direct job cost'
 flag is selected, this field will be unavailable for entry.

Cost of sales credit
Enter a G/L account code. The labor
 cost of sales will post to the General Ledger if labor hours are entered during
 Labor Hours Entry and charged to the customer. If the actual payroll cost of
 those labor hours has already been posted as an expense through payroll
 processing, this entry provides a method of reflecting labor hours that have
 been allocated to Work Order Entry. This account code defines where in the
 General Ledger this is reflected. The General Ledger account code entered here
 may not be for a direct cost account.  If the Work Order
 Installation Post labor
 cost checkbox is clear, entry in this field is irrelevant.
 If the user is posting to the General Ledger, then the payroll department is
 irrelevant. Ordinarily one would not want to post labor cost of sales to the
 General Ledger both from Work Order and through Payroll processing.
 If the cost of sales G/L account code is set to
 Not used, it
 cannot be selected in this field.
If the 'Direct
 job cost' flag is selected, this field will be unavailable for
 entry.

Co. equipment G/L accounts

Co. equipment sales
Enter a valid G/L code where equipment
 used for work orders will be credited as revenue to the General Ledger. The 'No
 direct cost' option must be selected in G/L Master File Maintenance screen for
 this account code. This field is required and cannot be left blank.Note: Material, Labor, and Equipment Sales may
 credit the same G/L account, if desired. If the Co. equipment sales G/L
 account code is set to 'Not used', it cannot be selected in this field.


Cost of sales debit
Enter a G/L account code for equipment
 used for work orders to debit as revenue to the General Ledger. Direct Work
 Order and Non-direct G/L accounts are allowed, but Direct job cost G/L accounts
 are not allowed. If the 'Direct job cost' flag is selected, this field will be
 unavailable for entry.The General Ledger account code
 entered here must have the same direct cost designation as the "direct cost"
 box above on this screen.

Cost of sales credit
Enter a G/L account code for equipment
 used for work orders to credit as revenue to the General Ledger. Direct Work
 Order and Non-direct G/L accounts are allowed, but Direct job cost G/L accounts
 are not allowed. If the 'Direct job cost' flag is selected, this field will be
 unavailable for entry.The General Ledger account code
 entered here must have the same direct cost designation as the "direct cost"
 box above on this screen.

Material G/L accounts

Material sales
Enter a valid G/L code where material
 used for work orders will be credited as revenue to the General Ledger. The
 General Ledger account code entered here may not be for a direct cost account.
  If the material sales G/L account code is set to
 Not used, it
 cannot be selected in this field.

(Inventory) Cost of sales debit
This field is applicable
 only if the Inventory Control module is installed. Enter the G/L account code
 to represent the cost of sales debit and credit for stock material items. This
 code should be a direct work order (or job cost) expense account. If the cost of sales G/L account code is set to
 Not used, it
 cannot be selected in this field.

(Inventory) Cost of sales credit

(Non-inventory) Cost of sales debit
Enter a G/L account code
 designating where materials (non-stock items) should post. This will typically
 be a cost-of-goods sold or expense account. This code should be a direct work
 order (or job cost) expense account. If the cost of sales
 G/L account code is set to Not
 used, it cannot be selected in this field.

(Non-inventory) Cost of sales credit

Other charge G/L accounts

Other charge sales
Enter a G/L account code
 for Other charge sales, Cost of sales debit, and Cost of sales credit. These
 fields will only be applicable for site work orders, and is required entry when
 the department is a non-direct cost. If the 'Direct job
 cost' flag is selected, this field will be unavailable for
 entry.

Cost of sales debit

Cost of sales credit

Overrides
If items other than labor and materials
 are to be charged, the G/L revenue accounts for those items can be entered in
 the Other Charge
 Overrides window. Examples of items that might appear here would
 be equipment or travel. These other costs must have been previously defined in
 Other Cost Maintenance.
