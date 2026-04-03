---
title: "Update Labor Hours to Payroll | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/service/work-order/spectrum-menus-overview/data-entry-overview/update-labor-hours-to-payroll"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/service/work-order/spectrum-menus-overview/data-entry-overview/update-labor-hours-to-payroll"
---

# Update Labor Hours to Payroll

For job and site work orders, this update will transfer the
 work order labor hours (including pay types ER, EO, ED, and EU) that have been entered in
 Labor Entry.
If updating to payroll, a regular check (meaning check sequence # 1)
 will be created for each employee, or appended if time card information already exists. The
 pay rate in Payroll will be determined by the work date entered in Work Order > Labor Entry.
This update will mark the Work Order labor record as 'transferred to
 Payroll'. In addition, the software will assign a unique control code to both the source
 record in Work Order > Labor Hours Entry and the new record in Payroll > Pre-Time Card Entry during the update.
During the transfer, if the pay type of the labor transaction is ER, EO,
 ED, or EU, and if there are any active attachments for the specified equipment, the
 software will automatically generate the additional EU transaction records. The equipment
 rate type will default as detailed on the Work Order Labor
 screen.

- For job work orders, the update will also transfer labor hours in
 work order history.

- For site work orders, the software will record the Work Order # and
 current settings for Equipment, Component, Contract, Employee billing rate and Equipment
 billing rate.

- For prevailing wage jobs with non-stated fringe, the standard pay
 rate will include the non-stated fringe and the employee rate will be adjusted
 automatically. Important: This screen is only
 available if the 'Update labor entries to pre-time card entry' checkbox is selected
 in Work Order Installation.

This screen allows job work orders to validate the Payroll department
 associated with each transaction when the Validate job division with G/L department check
 box in the Job Cost Installation screen is selected, which assures
 the G/L code associated with the department matches the division assigned to the job.
 Update Labor Hours also automatically resets the Payroll department when the Auto default
 G/L department checkbox in the Job Cost Installation screen is
 selected. It is recommended that you assign a Direct work order cost Payroll department in the [G/L Department File Maintenance](/en/spectrum/spectrum/service/work-order/spectrum-menus-overview/maintenance-overview/gl-department-file-maintenance)
 screen because non-direct cost departments (such as Admin) update to Payroll without
 including the work order number, equipment, component, and contract information.
For job and site work orders, the software will evaluate whether the labor transaction has already been assigned a billing control code during the transfer to Pre-Time Card Entry. If so, that control code will be assigned to the WO/TC control code column of the new time card record in order to associate all costs posted against this transaction under one control code. After updating these labor entries to Pre-Time Card Entry, you will encounter certain editing limitations in both Labor Hours Entry and Payroll processing to assure billing and cost distribution integrity.
The system will also validate that related codes are not already entered as State, County
 or Local tax codes. Related codes cannot be entered directly on the time card record. When
 labor hours are updated from the work order, automatically attach all related tax
 codes.
