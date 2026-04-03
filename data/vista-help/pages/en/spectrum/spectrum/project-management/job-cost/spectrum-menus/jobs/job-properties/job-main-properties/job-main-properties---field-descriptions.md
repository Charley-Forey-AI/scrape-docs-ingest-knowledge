---
title: "Job Main Properties - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/jobs/job-properties/job-main-properties/job-main-properties---field-descriptions"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/jobs/job-properties/job-main-properties/job-main-properties---field-descriptions"
---

# Job Main Properties - Field Descriptions

Fields
Descriptions

Classification

Division
You can use this optional code to associate
 several jobs to one division.
Example: A large construction company might
 have two divisions: one that specializes in pile driving, and
 another that specializes in environmental cleanup. Another
 company might set up divisions based on the type of work
 performed: drilling, steel erection, concrete, and so forth.
Enter or edit the division code, double-click
 in the field to select from a list of available divisions, or
 press Enter to accept the current division.
Caution: This code should not be changed once a job has
 obtained costs or billing. A change to the division requires
 adjustments in the General Ledger module.
The division can be tied to the General Ledger department (for
 example, division 1 and General Ledger department 1). Select
 the Validate
 job division with G/L department checkbox in
 Job Cost Installation. Entry in
 this field must then be a valid G/L department. The
 Search G/L Departments window is
 available to look up and select G/L department codes.

Master
Enter the master job number in this optional
 field to link multiple sub-jobs to one large (master) job. The
 job name displays to the right.
This information displays on the Contract
 Status report. On the [Contract Status Report](/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/reports-overview/contract-status-report) screen, select the Print job master
 summary checkbox to view the report grouped by
 master jobs.
The master job code must not be the same as a
 sub-job, have a different phase length than the current job, and
 have a job status of 'Complete' (unless the current job also has
 a status of 'Complete').
The master job must be set up in the system
 before any sub-jobs can be associated with it. Example of when
 this would be used: Constructing an apartment complex: Each
 individual building could be assigned a separate job number; all
 would be linked to the master "complex" job number.
If the master job is a time + material job,
 any labor billing rates or equipment billing rates set up in the
 Time + Materials module would be used on the sub-job as long as
 the sub-job does not have its own rates.

Cost center
This field displays if your company is using
 cost centers.

Job location

Address 1
Address 2
City
State
Zip
When editing, enter the job's site address,
 city (up to 25 characters), and 2-letter state abbreviation.


Telephone
Fax
Site Phone
When editing, enter the primary phone, fax,
 and site phone numbers without parenthesis or dashes.

Primary customer

Customer
 If you have more than one contract, the number of additional
 contracts displays in the heading. Click the link to open
 the Contract Detail Inquiry
 screen.
Enter the code of the primary customer that will be charged for this
 job. You can also define the customer code in Accounts Receivable > Customer Maintenance.
If you enter a customer code when this job is
 first set up, Spectrum automatically sets up a contract; so a
 duplicate entry in the Accounts Receivable files is
 unnecessary.
Invoices created in Accounts Receivable are sent to the address in the Accounts Receivable > Customer Maintenance screen.
Customer status protection prevents entry of a customer code when the
 status is set to Not used
 in the Accounts Receivable > [Customer Main Properties](/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/maintenance-overview/customers/customer-properties/customer-main-properties) screen. A warning displays, but
 entry is still allowed when the customer status is set to
 Inactive.

Contract #
 The contract number prints on the Job File
 Listing and is a user-defined field. Up to 30 characters are
 allowed.
This number is also used in the numbering of
 subcontract billings.
The default invoice number for subcontracts is
 established by the system using the convention a*b, where "a" is
 the contract number (as found in Jobs) and "b" is the payment
 number.

Contract type
The type of contract for this work displays on
 the [Contract Status Report](/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/reports-overview/contract-status-report) .
 Examples of contract types for different
 companies:

- Fixed bid or cost plus jobs

- City, state, government, or private
 contracts

-  Residential or commercial contracts


Owner name
Enter the owner name here. This name will
 appear on all lien release formats (vendor, subcontractor, and
 owner), when specified. If no name is specified here, the
 customer name will appear instead on the form.

Site
This optional field displays if the Work Order
 module is present. Enter the site ID, and the name displays.

Other information

Comment
You can enter up to two lines of text.

Price type
As a keyboard shortcut, enter the first letter
 of the price type.
Fixed price: Select the Fixed price method if
 the job will be billed on a fixed price basis.
Time + Material: Select this option if the job
 is billed on a time and materials basis.
If you have the Time + Material module and select this option, the job
 will also be set up in Time + Material > Job Billing Maintenance.
For true Time + Material jobs, labor is
 intended to be billed to customers at a billing rate per hour,
 rather than actual cost plus a mark-up.
For jobs flagged as Time + Material in Jobs,
 payroll burden will not post to Time + Material. To have payroll
 burden update to Time + Material, the job can be set up as a
 Cost Plus job in this screen. More Info When the job is set up
 in this way, the payroll burden will be combined with the actual
 labor cost and updated through to Time + Material. So, burden
 will not appear as a separate transaction, but it will be
 included with the actual labor costs.
Cost Plus: Select if the job will be billed on
 a cost plus basis.
If you have the Time + Material module and select this option, the job
 will also be set up in Time + Material > Job Billing Maintenance.
Unit Price: Select if the job will be billed on
 a unit price basis.
Markups for Time + Material and Cost Plus jobs
 will be calculated in the Job Cost Transaction update.

Job units
Add or edit the total number of units allotted for this job (for
 example, 1000). The total job units are used on the Report
 Calculations - Job Cost Analysis Report (Non-Projected Cost)
 to calculate the cost per unit, such as $75.00 per square
 foot.

Unit of measure
Add or edit a description of the units-of-measure used for this job,
 such as square feet (sf) or cubic yards (cy). A search
 window is available to view and select predefined units of
 measure set up in Accounts Receivable > Unit of Measure File Maintenance.

Override calculation for contract status and profitability
 reports?
% complete
Projected cost
If you select this checkbox, the % complete
 and projected cost fields become available.

Status

Status
Select a status for the job:

- Active

- Inactive

- Complete

Access to this option group is limited to users who have the minimum
 required security level. If you don't have the required
 security level, you can still view the data, but cannot make
 changes. Security is set in the Site Map > Admin - Security tab  > Function Security Maintenance > Function Links Security window.
If you try to assign a new transaction to this
 job while Inactive is selected, you will receive a warning, but
 can continue entering data.
If you try to assign a new transaction to this job while
 Complete is selected, further
 entry is not allowed. If Equipment Tracking is being used,
 you cannot set the status to 'complete' if there is any
 chargeable equipment currently 'issued' to the Job (or
 Phase), and you will be alerted to 'return' equipment from
 the job site, which will generate the 'final billing'
 stand-by charges for the Job (or Phase).
If a job is set to Complete, and the
 Set projected costs, quantity, and hours to
 actual when job is complete check box is
 selected in the Installation screen, then the projected
 quantity is automatically set to equal the actual quantity
 amount.
If the current job is a sub-job and the status is
 Complete, disallow the status to
 be changed if the master job status is also
 Complete. If the current job is a
 master job, the status cannot be changed to
 Complete is any of its sub-jobs
 are set to Active or
 Inactive. All sub-jobs must be
 completed before closing the master job.
If a workflow is in progress, this field will
 be unavailable.

Disallow revenue entry?
If the selected status is Complete, select this
 checkbox to specify that revenue entries are disallowed.
 When this option is selected, Spectrum will validate whether
 users are authorized to record revenue transactions for the
 job in Accounts Receivable.

Actual complete date
This field is available when you have security
 access and select the Complete
 status, above. The date defaults to the current Job Cost
 processing date. This date will remain the same if the status is
 changed.
The [Contract Status Report](/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/reports-overview/contract-status-report) can print completed jobs based
 on the completion date entered here. The reports look at the
 current status setting plus the complete date to determine
 where to include the job on the report (for example, among
 Active and Inactive,
 or Complete jobs). Therefore, when a job is
 set to Complete and the Contract Status Report is
 reprinted for an earlier date, the job appears within
 Active jobs even though it has been
 completed.
This date can be entered in the Job Milestones
 section on the [Job Dates](/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/jobs/job-properties/job-dates) screen.
If you purge a job, you must record an actual
 complete date first.

Global positioning

Latitude
Longitude
Enter the GPS latitude and longitude settings
 for the selected job site. Some companies use GPS to
 pinpoint the current location of equipment in order to compute
 the distance to the next job site.

Legal description

Legal description
Enter a legal description for the job here.
 This description will appear on all lien release formats
 (vendor, subcontractor, and owner), when specified. If no
 description is specified here, the job address will appear
 instead on the form.
