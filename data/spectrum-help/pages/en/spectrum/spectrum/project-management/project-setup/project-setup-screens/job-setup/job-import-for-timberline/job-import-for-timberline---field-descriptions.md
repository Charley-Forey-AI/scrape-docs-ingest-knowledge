---
title: "Job Import (for Timberline) - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/project-setup/project-setup-screens/job-setup/job-import-for-timberline/job-import-for-timberline---field-descriptions"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/project-management/project-setup/project-setup-screens/job-setup/job-import-for-timberline/job-import-for-timberline---field-descriptions"
---

# Job Import (for Timberline) - Field Descriptions

Use the table below for reference when completing the fields on this screen.
Fields
Descriptions

Job
Entry in this field is required. Enter
 the Spectrum job number into which the estimated job will be imported. This may
 be an existing Spectrum job, or double-click to display the Search
 Jobs window and click New to add a job from here.
Estimate type
Use the drop-down menu to select the
 estimate type: Base
 contract or Change
 request. Estimates for base contracts will
 continue to be recorded in Job Cost > Phase File Maintenance. Estimates for change requests will be updated to Accounts Receivable > Change Request Log / Entry.
If you select Change
 request, the Reference field displays. In the Reference field, enter an
 eight-digit alphanumeric reference for the change request estimate or select
 from a list of valid change requests.
Note: Only
 users with the proper security settings can add change requests on-the-fly
 by clicking the Maintenance button in the
 Change Requests For Selected Contract window. The
 Maintenance button does not display for users with
 insufficient security.
 Estimates for base
 contracts will continue to be recorded in Job Cost > Phases. Estimates for change requests will be updated to Accounts Receivable > Change Request Log / Entry.

Labor cost type
Enter the Spectrum
 materials cost type to which Timberline costs should be assigned when
 importing. Entry in these fields are required. After a cost type code has been
 entered, the cost type description displays from the Cost Type File
 Maintenance screen.
Equipment cost type

Material cost type

Subcontractor cost type

Other cost type

Clear job setup spreadsheet?
Select this checkbox to clear the
 Job Setup before import. If the checkbox is left
 clear, the data being imported will append (add to the bottom) to the data that
 currently exists in the Job Setup. This allows users to
 import a base bid, then append alternate bids to the same Project
 Setup job and set up the job as one large job in Spectrum.
Price method
If the price method selected is
 Cost plus or
 Time + material,
 then when the Job Setup Update is run, the job will automatically be set up in
 the Time + Materials module.
Set projected contract quantities: Cost type
If this is a unit price job, enter the
 cost types to set projected contract quantities for. As a result, the projected
 contract will be used on all the Contract Status Reports instead of the
 original or revised contract amount.
