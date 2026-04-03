---
title: "Properties Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/job-cost/installation-overview/job-cost-installation---properties/properties-field-descriptions"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/project-management/job-cost/installation-overview/job-cost-installation---properties/properties-field-descriptions"
---

# Properties Field Descriptions

Use the Properties field descriptions when completing tasks on
 this screen.
Fields
Descriptions

Phase number mask
This field stores the display standard pattern of
 your phase code, and is used throughout Spectrum. Some users will
 define phases according to the Construction Specifications Institute
 (C.S.I.) standard, but this is not required. You can specify up to
 20 characters, including any dashes or other characters and up to
 two levels of summarization. Other users will define a single phase,
 particularly if the operation is a subcontract or specialty
 contractor with a focus on a limited variety of tasks. The phase
 code mask is not usually altered after initial installation. This
 standard phase mask will then default as new jobs are added in Jobs.
 If needs at your company change in the future, the default phase
 mask may be changed in this screen, then all new jobs set up
 thereafter will default as desired.
For example, you may plan to set up a six-digit
 phase code with two tiers of summarization and dashes for
 readability (0-22-000 0-26-000 1-16-000 etc); the mask for this
 phase code would be X-XX-XXX. Alternately, you may opt for a
 six-digit pattern for your phase code with the first two digits
 indicating the group subtotal point, (02-2000, 02-6010, 16-0000, and
 so forth); the mask for this phase cost configuration would be
 XX-XXXX. A third example might be simply a single phase 1; the mask
 in this case is X.
It is not necessary to set up all jobs with the
 same phase mask. When a new job is added, if another phase mask is
 desired, simply edit the "Phase Setup" in Jobs before costs are
 applied to the job.

Overhead allocation
 batch
The batch code is the default overhead allocation
 batch code to use when setting up new jobs. The job overhead
 allocation batch code is then used in conjunction with the
 Overhead Allocation Maintenance screen and
 update to post overheads by batch code. Leave this field blank if
 you do not wish to set a batch code automatically when adding a
 job.

Phase grouping

Major group start
 position
The software is prompting for the standard
 position, left to right, in which the major group starts. The
 response in this field will be either 1 or blank
 (zero), depending upon whether this company will utilize major group
 subtotals. Major group subtotals are necessary only when two tiers
 of group subtotals are desired. If only one tier of subtotals is
 desired, the minor group should be used; the major group positions
 are to be set to blank (zero). This standard position will then
 default as new jobs are added.
An example of a phase structure with major and
 minor group subtotals is X-XX-XXX. The starting position of the
 major group in this example is 1 (1-XX-XXX).

Major group end
 position
The software is prompting for the standard
 position, left to right, in which the major group ends. The response
 in this field will be either a digit or blank (zero), depending upon
 whether this company will utilize major group subtotals. Major group
 subtotals are necessary only when two tiers of group subtotals are
 desired. If only one tier of subtotals is desired, the minor group
 should be used; the major group positions are to be set to blank
 (zero). This standard position will then default as new jobs are
 added.
An example of a phase structure with major and
 minor group subtotals is X-XX-XXX. The ending position of the major
 group in this example is also a1 (1-XX-XXX).

Minor group start
 position
The software is prompting for the standard
 position, left to right, in which the minor group starts. The
 response in this field will be either a digit or blank (zero),
 depending upon whether this company will utilize minor group
 subtotals. If no group subtotals are desired, all four group
 positions should be set to blank (zero). This standard position will
 then default as new jobs are added.
An example of a phase structure with major and
 minor group subtotals is X-XX-XXX. The starting position of the
 minor group in this example is 2 (X-2X-XXX).
An example of a phase structure with only minor
 group subtotals is XXX-XXXX. The starting position of the minor
 group in this example is 1 (1XX-XXXX).

Minor group end
 position
The software is prompting for the standard
 position, left to right, in which the minor group ends. The response
 in this field will be either a digit or blank (zero), depending upon
 whether this company will utilize minor group subtotals. If no group
 subtotals are desired, all four group positions should be set to
 blank (zero). This standard position will then default as new jobs
 are added.
An example of a phase structure with major and
 minor group subtotals is X-XX-XXX. The ending position of the minor
 group in this example is 3 (X-X3-XXX).
An example of a phase structure with only minor
 group subtotals is XXX-XXXX. The ending position of the minor group
 in this example is 3 (XX3-XXXX).

Validate new phase code with standard
 phase list
Select this checkbox to prevent the user from
 entering a non-standard phase code on the Job
 Phases screen.

Utilize employee code for job
 personnel?
Selecting this checkbox allows you to verify the
 project manager, estimator, and superintendent fields in the Job
 Cost file against the employee codes in the Payroll file. This
 feature is helpful when you are using the job-based security feature
 in order to make sure that the personnel codes being used for the
 job are valid.Note: Validation is for
 single-company use only, not multi-company.

- If the checkbox is selected, the
 Project
 manager, Superintendent, and Estimator
 fields in the Jobs screen will require
 a valid employee code from the current company to be
 entered, or left blank. If the checkbox is left clear, the
 Jobs fields will accept any entry.

- Furthermore, if this checkbox is
 selected, the project manager field in Job Cost is validated
 and the Accounts Payable > Print Subcontract Form prints the employee name under the Site
 Contact on the Subcontract Form.

Set projected costs, quantity, and hours to
 current estimate when adding a phase?
Select this checkbox to set projected costs,
 quantities, and hours equal to the current estimates when adding new
 phases to a job. This setting applies any time a new phase code/cost
 type combination is added to Spectrum.
If a phase is added when this checkbox is
 selected

- When writing to both the projected balance
 file and the projected history detail file, the projected
 costs and hours are set to use the current Job Cost
 processing date.

- The projected figures are also initialized
 using the Copy Phase utility or Project Setup > Job Setup Update.

- The system adds a record to the projected
 cost history file. No 'backing out' entry is created for the
 new phase, even if there are later projected dates for other
 phases on the job.

Project Setup module
The projection settings work differently in
 Project Setup because projections can be
 updated multiple times to the job. If projections already exist for
 this phase, then the difference between the existing amount and the
 current estimate is stored in the Projected Cost History file. This
 means that the projected cost amount in the phase is set to the
 current estimate, but the incremental amount is booked to the
 Projected Cost History file.
Accounts Receivable module
When the Accounts Receivable
 Installation screen is set to Contractor pricing update
 projected cost, then the system adds a record to the
 projected cost history file using the change request approval date
 when entering a change order or a change request (with an action
 type of 1, 2, or 3). No 'backing out' entry is created for the
 change, even if there are later projected dates for that phase on
 the job.Note: This may
 have the effect of increasing the total projected amount on the
 job depending on the approval date and the date requested for
 the Contract Status Report.

Set projected costs, quantity, and
 hours to actual when job is complete?
Select this checkbox to set projected costs,
 quantities, and hours equal to the actual cost when the job status
 is set to Complete.

Set projected cost to actual if actual
 is greater?
Use this field to specify whether projected costs
 should automatically be set equal to actual costs in any phase where
 actual cost-to-date is greater than the current projected cost
 during the Projected Cost update. If Projected Cost Entry is not
 used in this company, entry in this field is irrelevant.
Operations that store labor and burden in job cost
 as a single cost type will usually select this checkbox. These
 companies are likely to benefit from the automatic adjustment of
 projected cost when phases exceed 100% of planned cost. If actual
 cost is already greater than current projections, then the system
 will reset projected cost at 100% to equal current actual cost.
 Operations in which job cost is set up to store labor and associated
 burden in separate cost types, but the labor cost type estimates
 include burden, will typically leave this checkbox clear. The
 burden cost type in these companies will be over budget throughout
 the job, but the labor cost type will be correspondingly under
 budget.

Set projected cost to actual if actual
 is greater?
Select this checkbox to enter job-to-date
 quantities in Projected Cost Entry.

Enter additional quantity in projected
 cost entry?
This setting is used to control whether users may
 enter 'additional quantity' in [Projected Cost Entry (by Phase summary)](/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/data-entry-overview/projected-cost-overview/projected-cost-entry-by-phase-summary).
If selected, the Quantity field
 will be enabled in Projected Cost Entry when the job is built for
 Group summary = 'Phase' since quantity entry is not applicable for
 'major' and 'minor' group display.

Current estimate display
 only?
Select this checkbox to specify that the
 CurrentEstimates fields,
 contained in Job Phases, will always be display-only. If you select
 this checkbox, the CurrentEstimates fields
 in the Job Phases screen will not be accessible
 in Change mode. If you leave this checkbox clear, then the
 Job Phases screen will permit changes in
 the Current
 Estimates fields. This feature provides additional
 protection for cost revisions that are tracked using Change Request
 processing.

Utilize tax
 classification?
This checkbox designates whether or not the tax
 classification system will be used. If this checkbox is selected,
 enter a tax classification code specified during Jobs (instead of an
 A/R Sales tax code). Later, you will be prompted for a use tax code
 in Job Requisition Entry.
If this checkbox is not selected, you will enter
 an A/R sales tax code during Jobs. This will then allow you to set
 the exemption flags during Purchase Order Entry and A/P
 Invoice/Credit Memo Entry.

Validate job division with G/L
 department?
Decide whether to require that the division
 specified in the job master file is equal to the General Ledger
 department code. Companies that are not using the
 departmentalization feature in General Ledger should leave this
 checkbox clear. If your general ledger utilizes departments, you
 may elect to use the validation feature to assure that all costs for
 a given job are charged to its associated department in General
 Ledger. If this checkbox is selected, the system will confirm that
 the J/C division matches the G/L department in all entry screens.
 For example: if the G/L department is 02 for a given
 entry, the division of the job must also be 02. Furthermore,
 the Auto default G/L
 departmentand Set add-on G/L account from
 Payroll department checkboxes display if this check
 box is selected.
Note: This checkbox displays only if
 the cost centers feature is not enabled.
The system sets the department code for you if the
 Auto default G/L
 dept checkbox is selected. You do not have to know
 the department of a job before entry; the system will automatically
 set it for you. You must set the payroll departments up with the
 first character in the department (for example, PR dept = 01JC,
 02JC, where 01 and 02 are the G/L department and equal the division
 in the job file). The system will then change the code during
 Payroll Time Card Entry.

Auto default G/L
 department?
The system sets the department code for you if
 this checkbox is selected. You do not have to know the department of
 a job before entry — the system will automatically set it for you.
 In addition, the payroll departments will be replaced just like a
 G/L code, so you must set the payroll departments up with the first
 character in the department (for example, PR dept = 01JC, 02JC,
 where 01 and 02 are the G/L department and equal the division in the
 job file). The system will then change the code during Payroll Time
 Card Entry.

Set add-on G/L account from Payroll
 department?
This checkbox displays if the Validate job division with
 G/L department checkbox is selected. Select this
 checkbox to have the system default in the appropriate G/L
 department based on the Payroll department.
If both these checkboxes are selected, after
 processing and updating the Payroll cycle, review the G/L
 Distribution Report. Note that different time cards using non-direct
 add-on codes as the pay type will be expensed to the same G/L
 account.

Auto-update 'actual quantity complete'
 from

All inventory and purchase transactions
 No automatic update
The administrator can specify whether Spectrum
 will record actual quantities in Job Cost during the Job Cost
 Transaction Update. In Accounts Payable > Subcontract Phase Details, if you select the first option, the Update job qty
 complete column will not display.

Phase code fill

Leading zeros
Trailing zeros
Select to pad phase codes with either Leading zeros or
 Trailing
 zeros. When you change between the use of leading
 and trailing zeros, a message displays to inform you that existing
 phase codes will NOT be affected and therefore any incompatibilities
 should be worked out before making this change in order to avoid
 problems later on. Changes made here will affect phase entry
 throughout the system.
For example, if leading zeros is selected and the
 number 2 is entered for a phase with a mask XX-XXXX, the system
 fills the blank portions of the mask with zeros to look like
 00-0002. Likewise, if trailing zeros are selected and the number 2
 is entered for a phase with mask XX-XXXX, the system fills the blank
 portions of the mask with zeros to look like 20-0000.

Unit price projection method

Change from estimated to actual after %
 complete
Enter the percent complete a phase should reach
 when Spectrum should update the projection method from Estimated to
 Actual. If the value is zero, the projected cost method
 will not be changed when projected costs are updated. If the value
 is more than zero, then the projected cost method will be set to
 Actual
 during the update for each phase with a completion percentage
 greater than the percentage entered in this field.

Default for new phases
Select a default projected method for new
 phases:

- Actual

- Projected

- Estimated

Tax class
 default

By job
By vendor
This field allows you to designate whether the
 primary default for use tax coding should be based on job or vendor.
 The tax classification is the location where the Accounts Receivable
 and Accounts Payable tax codes are set up and the cost
 type/phase-based Accounts Payable exemptions are stored.

-  If By job is
 selected, the system uses the Accounts Payable tax code (use
 or sales tax) associated with the job. It also allows for
 tax exemptions based on cost type/phase.

-  If By vendor
 is selected, the system first looks to tax code setup for
 the vendor; if no tax code is present the system looks at
 the job's tax classification code.
Note: This prompt is only available if the
 Utilize
 tax classification checkbox is
 selected.

If the cost center feature is enabled, the following fields
 display below the Phase code
 fill selection.

Fields
Descriptions

Cost center inter-posting G/L
 account
This field is used to define a default cost center
 inter-posting account code for the selected company. Enter the
 default cost center inter-posting account code or press F4 to select from
 a list of available G/L account codes. This field is available only
 if cost centers are activated in the current company.
Click the Override button
 to enter override G/L account codes fro each cost center set up in
 the software. The Override buttons displays only if the Allow G/L account overrides
 by cost center checkbox is selected in the
 Cost Center Settings window on the
 Enterprise
 Installation > Company tab.

Overrides
Click this button to display the Cost
 Center to G/L Overrides window for either cost center
 inter-posting accounts or for retained earnings. When this window
 displays, G/L override accounts can be entered for each cost center
 set up in the company. If you do not want to designate an override
 account for a cost center, leave the G/L account field
 for the cost center blank.
This window is available only if the Allow G/L account overrides
 by cost center checkbox is selected on the
 Cost Center Settings window on the
 Enterprise
 Installation > Company tab.
