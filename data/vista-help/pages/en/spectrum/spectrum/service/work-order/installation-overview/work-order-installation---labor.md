---
title: "Work Order Installation - Labor | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/service/work-order/installation-overview/work-order-installation---labor"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/service/work-order/installation-overview/work-order-installation---labor"
---

# Work Order Installation - Labor

Use this tab to select the labor settings for the Work
 Order module. These settings can be changed as needed at any time.
Important: Selecting both the Update labor
 entries to pre-time card entry? and Update cost of goods sold for
 labor entries? checkboxes is not recommended. If they are both selected,
 then the entry is updated twice. If the transaction has been transferred to A/R, the status
 will be set to 'Updated' even if the transfer to Payroll and/or Payroll Update has not yet
 occurred. Once the status is 'Updated', it does not revert to another status during Payroll
 Processing.
Field
Description

Work order labor entry

Automatically build task detail for labor?
Select this checkbox to automatically
 transfer labor detail lines from task to task; otherwise, leave this checkbox
 clear.  If this checkbox is selected, labor tasks set up
 in the Task File Maintenance window will
 automatically transfer to new work orders set up in Work Order
 Entry if they have a cost detail associated with them.
 Additionally, all labor tasks will be listed individually in
 Labor Entry, Material
 Entry, and Other Cost Entry.
When labor transactions are generated for tasks, the G/L
 department will be set from the new G/L department field in the work order
 header.

Update labor entries to pre-time card entry?
The system is prompting you to decide
 whether work order entries will interface with Payroll Pre-Time Card Entry. If
 this checkbox is selected and the payroll transfer is authorized using Update
 Labor Hours, the applicable employee labor costs will automatically be recorded
 in the Pre-Time Card Entry files. It will then be necessary for the operator to
 perform the Pre-Time Card Update and administer the remainder of the payroll
 cycle. If this checkbox is not selected, payroll files will be unaffected by
 work order activities. Entry in this field is irrelevant
 if the Payroll module is not installed in this company.

Work order labor cost history

Post actual payroll burden to work order
Select this checkbox to specify
 whether to post actual burden for payroll costs to the work order cost history
 file.

- If this checkbox is selected the Pre-time card burden
 percent field and percentage will be displayed below. When
 this checkbox is selected, Spectrum ignores the burden defined in both
 the Technician Maintenance file and Labor Category Maintenance file.

- If not selected, the Payroll burden percent
 field and percentage will be displayed below.

Unposted time card burden percent
If the Post actual payroll burden to work
 order checkbox above is selected, the Unposted time card burden
 percent field and percentage will be displayed in this field. If not selected,
 the Payroll burden
 percent field and percentage will be displayed instead.
Payroll overhead
Select this option to specify whether
 or not to accrue overhead based on labor cost charges to work orders during the
 Payroll update, and if so, whether to calculate based on a percentage or as a
 rate per hour.
Overhead %
Enter an overhead percentage or rate
 per hour, based on the Payroll overhead method selected above.
Work order labor billing

Default labor entries to taxable?
Select this checkbox if labor is
 usually taxable. Leave the box blank if labor on work orders is usually not
 taxable. When new sites are entered, the option selected
 here will be the default, but either option may be selected at that time.


Update cost of goods sold for labor entries?
The system is prompting you to decide
 whether labor "cost of goods sold" should be transferred via the instant
 transfer in Work Order Entry or the Transfer
 to AR & Complete WO update through to General Ledger. If
 this checkbox is left at the default of selected, then the labor costs will be
 posted to the A/R invoice files, and subsequently will update to the General
 Ledger as a "cost of goods sold" entry. If the Payroll module is not present in
 this company, and you want to post labor costs to General Ledger, select this
 checkbox. If Payroll module is present in this company, and you want to record
 the timing difference between the date of work performed and payday, select
 this checkbox and utilize a "payroll variance account". Otherwise, leave this
 checkbox blank if no General Ledger entry is to be made for labor "cost of
 goods sold" through Work Order Entry. Regardless of
 entry in this field, cost and profit figures will be recorded for the work
 order. Entry in this field will be used by the software only when companies are
 engaging in non-job work orders.
Show labor entries in summary on A/R invoice?
The system is prompting whether to
 include Summary or
 Detail labor
 billing information on the A/R invoice when work order transactions are
 transferred to Accounts Receivable > Invoice Entry. If this field is set to Summary, all labor on the
 work order will be titled "LABOR USED" and will be summarized for each
 different billing rate. For example, Regular and Overtime labor will show
 separately. If this field is set to Detail, then the A/R
 invoice will include specific labor itemization, based on the selection made in
 the Detail labor
 billing field on this screen.
A/R invoice labor detail
The system is prompting for you to
 select what method should be used to detail labor amounts on the A/R invoice
 when a completed work order is transferred to Accounts Receivable > Invoice Entry. If this field is set to Phase detail, labor billing
 entries will be recorded on the A/R invoice by phase. If this field is set to
 Category detail,
 labor billing amounts will be recorded on the A/R invoice by work order
 category. If this field is set to Employee detail, then the A/R invoice will detail each employee
 who participated on the work order.
