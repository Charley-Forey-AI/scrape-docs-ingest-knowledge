---
title: "Job Cost Analysis Inquiry - Job Info window | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/inquiries-overview/job-analysis/job-cost-analysis-inquiry---job-info-window"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/inquiries-overview/job-analysis/job-cost-analysis-inquiry---job-info-window"
---

# Job Cost Analysis Inquiry - Job Info window

The details about the selected job (address, contact information, etc.) display in this window. No entry is allowed.
Fields
Descriptions

Job
The job number displays, no entry is allowed.
Job is the key field for the job file. The job number will be used throughout
 Spectrum. In Payroll > Time Card Entry, job numbers can be entered to indicate the specific job on
 which an employee worked. In Accounts Payable, job numbers can be entered to
 ensure that invoices are charged to the appropriate job. In
 Accounts Receivable, job numbers are used in
 setting up contracts, for change orders, and for draw requests. For Time +
 Material jobs, the job number is used in the Time + Material module.
 Purchase orders may be charged to a specific job, where appropriate. In the
 Equipment Control module, the job number is used to track the usage of
 equipment. Throughout the system, this job number is used for job costing
 purposes and will appear on various reports.

Address

Division
The division code is optional. It allows for the possibility of associating several jobs to one division. For example, a large construction company might have two divisions: one that specializes in pile driving, and another that specializes in environmental cleanup. Another company might set up divisions based on the type of work performed: drilling, steel erection, concrete, and so forth. Some of the available reports have the option of printing all jobs for a selected division.
Based on the Job Cost screen, "division" can be tied to the General Ledger department, if desired (for example, division 1 and General Ledger department 1).
If the cost center feature is enabled in the Enterprise
 Installation screen, the Cost Center assigned to the job will
 appear to the right of this field.

Master
When multiple sub-jobs are performed for one large job, the sub-jobs may be
 linked to the master job using the number of the master job here, for
 purposes of the Contract Status Report. In this case, the master job must be
 set up in the system before any sub-jobs may be associated with it. This may
 be used, for example, when constructing an apartment complex. Each
 individual building could be assigned a separate job number; all would be
 linked to the master "complex" job number. If the master job is a Time +
 Material job, any labor billing rates or equipment billing rates set up in
 the Time + Material module will be used on the sub-job providing the sub-job
 does not have rates of its own. This field can be left blank, if
 desired.

Address
The site address for this job displays, it is not necessarily the same as the billing address. No entry is allowed.

Phone
The primary telephone number for this job displays. No entry is allowed.

Fax
The primary fax number for this job displays. No entry is allowed.

Site phone Site
The site code for the selected job will appear in this field. Click the lookup icon to open the View Site window.
This field will only be visible if the Work Order module is present for the
 current company.

View site
Use the View Site window to review work site details,
 including the site address, billing address, directions to the site, and so
 forth. For more details about the New/Edit/View Site
 window, review the New/Edit Site topic in the Work
 Order online Help file.

Properties

Customer
The customer code stored in Jobs displays.

Contract #
The contract number for this job displays.
The contract number will print on the Job File Listing and is a user-defined field. This number is also used in the numbering of subcontract billings. The default invoice number for subcontracts is established by the system using the convention a*b, where "a" is the contract number (as found in Jobs) and "b" is the payment number.

Contract type
The type of contract used for this work displays. No entry is allowed.
For example, this field may be used for Fixed Bid or Cost Plus jobs. Another use of this field could be for a company having city, state, government, and private contracts. Another company might have residential and commercial contracts.

Contract date
The contract date displays from the job file. No entry is allowed.

Price
The pricing method for this job displays, no entry is allowed. Options include:

- Fixed price Select Fixed price if the job will be billed on a fixed price basis.

- Time + material
 SelectTime +
 materialif the job will be billed on a time and
 materials basis. This job will also be set up in Time + Material > Job Billing
 Entry when this option is selected and Time + Material module
 is present.

- Cost plus Select
 Cost plus
 if the job will be billed on a cost plus basis. This job will also be
 set up in Time + Material > Job Billing
 Entry when this option is selected and Time + Material module
 is present.

- Unit price Select Unit price if the job will be billed on a unit price basis.

Job status
The job status for this job displays (Active, Inactive, Complete).

Certified?
This checkbox tells you whether or not this job is certified. No entry is allowed.
The system will use this information to ensure that Payroll > Time Card Entry is performed in the correct format so that a Certified
 Payroll Report can be printed. The certification flag in Payroll > Time Card Entry will default based on this field unless a phase override is
 specified.

Superintendent
The superintendent for this job displays. Many of the Job Cost reports may be selected for specific superintendents.
If the Utilize employee code for
 job personnelcheckbox is selected in the Job Cost
 Installation screen, the superintendent field is verified
 against the employee codes in the Payroll file. This feature is helpful when
 you are using job-based security in order to make sure that the personnel
 codes being used for the job are valid.

Estimator
The estimator for this job displays. Many of the Job Cost reports may be selected for specific estimators.
If the Use employee code for job
 personnel checkbox is selected in the Job Cost
 Installation screen, the estimator field is verified against
 the employee codes in the Payroll file. This feature is helpful when you are
 using job-based security in order to make sure that the personnel codes
 being used for the job are valid.

Project manager
The project manager for this job displays. This name prints on the job listing; many reports can be selected for specific project managers.
If the Use employee code for job
 personnel  checkbox is selected in the Job Cost
 Installation screen, the project manager field is verified
 against the employee codes in the Payroll file. This feature is helpful when
 you are using job-based security in order to make sure that the personnel
 codes being used for the job are valid.

Notes
Click this button to display the Note Topics window.
 Use this window to review, add, and edit job descriptions and comments.

Contract Notes
Click this button to view any additional job contract descriptions and comments.

Related information

- [Job Cost Center Setup](/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/maintenance-overview/job-cost-center-setup)
