---
title: "Import Standard Job - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/project-setup/project-setup-screens/job-setup/import-standard-job/import-standard-job---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/project-management/project-setup/project-setup-screens/job-setup/import-standard-job/import-standard-job---field-descriptions"
---

# Import Standard Job - Field Descriptions

Use the table below for reference when completing the fields on this screen.
Fields
Descriptions

Job code
Entry in this field is required. Enter
 the Spectrum job number into which the estimated job will be imported. This may
 be an existing Spectrum job, or double-click to display the Search Jobs window
 and click New to add
 a job from here. If the Work Order module is present and
 the installation screen is set up to allow job work orders, the Job W.O.
 button displays and the Search Work Orders window will auto-open and allow
 you to select a work order.

Estimate type
Use the drop-down menu to select the
 estimate type: Base
 contract or Change
 request. Estimates for base contracts will
 continue to be recorded in Job Cost > Phase File Maintenance. Estimates for change requests will be updated to Accounts Receivable > Change Request Log / Entry.
If you select Change request, the
 Reference field
 displays. In the Reference field, enter an eight-digit alphanumeric reference
 for the change request estimate or select from a list of valid change
 requests.
Note: Only users with the proper
 security settings can add change requests on-the-fly by clicking the
 Maintenance button in the Change
 Requests For Selected Contract window. The
 Maintenance button does not display for users with
 insufficient security.

Import job with bid group?
Select this checkbox to default the
 billing item with a bid group during the import. If this checkbox is selected,
 the Bid group field
 displays.

- If this is select this option and enter a bid group,
 then that bid group will append to the front of the billing item.

- If you clear this option, then the first two
 digits of the billing item will be used as the bill group. Therefore, the
 billing item code needs to be at least 3 digits, preferably 4 digits.


Clear phase setup?
Leave this checkbox clear to append
 the imported data to information already in the Job Setup screen. If the check
 box is left clear, the data being imported will append (add to the bottom) to
 the data that currently exists in the Job Setup. This allows you to import a
 base bid, then append alternate bids to the same Project Setup job and set up
 the job as one large job in Spectrum.
Clear billing detail setup?
Leave this checkbox clear to append
 the imported billing detail data to information already in the
 Billing Detail Setup screen. If the checkbox is left
 clear, the data being imported will append to the billing data that currently
 exists in the file (add at the bottom). This allows you to import a base bid,
 then append alternate bids to the same file and set up the job as one large job
 in Spectrum.
Price method
If the price method selected is 'Cost
 plus' or 'Time + material', then when the Job Setup Update is run, the job will
 automatically be set up in the Time + Materials module.
Set projected contract quantities: Cost type
If this is a unit price job, enter the
 cost types to set projected contract quantities for. As a result, the projected
 contract will be used on all the Contract Status Reports instead of the
 original or revised contract amount.
