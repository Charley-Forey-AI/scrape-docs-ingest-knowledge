---
title: "New Job | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/jobs/job-properties/new-job"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/jobs/job-properties/new-job"
---

# New Job

Use this window to add the initial elements of a new job
 and contract.
 After completing this window, the [Job Main Properties](/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/jobs/job-properties/job-main-properties) screen opens.
Fields
Descriptions

Job defaults

Standard new job Use quick setup Use master job
Select a job default for the new job:

- If you select the Use quick setup option, specify a job setup group code.

- If you select the Use master job option, specify an existing job code to base the new job on.

Existing work site (optional)
Enter a work site ID. The Site code automatically displays if the designated Group code is set to copy the work order site or the source job has a specified work order site.

New job

Job code Description
Enter the job code and description.

- If you selected a group code in the section above, a job group code from the [Quick Job Setup Maintenance](/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/maintenance-overview/quick-job-setup-maintenance) screen displays.

- If you selected a master job code in the section above, the system will display the last sub-job number to the right of this field and default the next sub-job number. If no sub-job code is found, the system will alert you that no sub jobs are available for the selected job code.

Division
Specify a G/L department code for the new job.

Edit Key Personnel
Press this button to specify key personnel for the new job. When setting up a sub-job, the personnel fields will default automatically from the master job.

Properties

Customer code
Enter an active customer code in this optional section.

- The customer code defaults if you set up a quick-job group code that is set to copy the customer code.

- If a site code has been specified in the Quick Job setup section, the Customer Code defaults from the Work Order module.

Address
The address displays automatically if you entered a job code in the New job section.

Job located at customer address?
This checkbox displays if you entered a Customer code or did not select the Job located at Work Order site checkbox.

Original contract
Enter the original contract amount in this optional field. Do not include
 change orders. If a customer code has been specified above, the
 Accounts Receivable Contracts screen will store
 this contract amount.

Tax classification/Sales tax code
Use this optional field to track the sales tax or reporting location. The sales tax code is for Accounts Receivable reporting purposes while the tax classification code is a combination of Accounts Receivable sales tax and Accounts Payable sales or use tax.

- Select the Utilize tax classification checkbox in [Job Cost Installation - Properties](/en/spectrum/spectrum/project-management/job-cost/installation-overview/job-cost-installation---properties) to display the Tax class code field. Leave the checkbox clear to display the Sales tax field.

- Tax classification and sales tax codes should have previously been set up in [Tax Classification File Maintenance](/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/maintenance-overview/tax-classification-file-maintenance).

Tax Classification: Add or edit the tax class code for this job. You can enter up to 15 alpha-numeric characters.
If you filled out the Quick Job setup section, and set the code to copy the
 tax classification code, the tax code defaults from the Group code
 field.
Sales tax: Based on the job's location, enter the default sales tax code. A code should be entered even if this is not a taxable job. Click the drop-down arrow or double-click on this field to view valid sales tax codes.
If you selected the Group code and a Customer above, then the sales tax code associated with that customer is the default.

Taxable

- If you selected a Group code that is set to copy the taxable setting, then this field displays Yes.

- If the Sales tax code is at 0.00%, then No displays.

- Select No Default if the invoice is conditionally taxable and the decision needs to be made on a case-by-case basis.

Price type
Select one of the price types below to bill the job on a fixed price, time and material, cost plus, or unit price basis.
Fixed price
This is the default option unless you selected a Group code set to copy a different price type setting in Quick job setup, above.
Time + material
If you have the Time + Material module, the job will also be set up in Time + Material > Job Billing Maintenance.

- For true Time + Material jobs, labor is intended to be billed to customers at a billing rate per hour, rather than actual cost plus a mark-up.

- For jobs flagged as Time + Material in Jobs, payroll burden will not post to Time + Material. To have payroll burden update to Time + Material, the job can be set up as a Cost Plus job in this screen. More Info When the job is set up in this way, the payroll burden will be combined with the actual labor cost and updated through to Time + Material. So, burden will not appear as a separate transaction, but it will be included with the actual labor costs.

Cost plus
If you have the Time + Material module, the job will also be set up in
 Time + MaterialJob Billing
 Maintenance.
Unit price
Markups for Time + Material and Cost Plus jobs will be calculated in the Job Cost Transaction update.

Related information

- [Quick Job Setup Maintenance](/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/maintenance-overview/quick-job-setup-maintenance)

- [Job Main Properties](/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/jobs/job-properties/job-main-properties)
