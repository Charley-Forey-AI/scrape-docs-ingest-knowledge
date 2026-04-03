---
title: "Error Messages | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/project-setup/troubleshooting-overview/error-messages"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/project-management/project-setup/troubleshooting-overview/error-messages"
---

# Error Messages

The Error Messages section is a quick way to find solutions for some of the error messages in Spectrum.

## Error - Customer Code Entered Is Not Available For Use

If a customer with the status of Not
 used is entered, this message displays. This error message disallows
 further data entry.
To change the customer's status, click Accounts Receivable > Maintenance > Customer > Properties. Select either Active or Inactive in the Status section.

## Error - G/L Account Code Entered Is Not Available For Use

If a General Ledger account code with the status of Not used is entered, this message
 displays. This error message disallows further data entry.
To change the General Ledger account code's status, click General Ledger >  Maintenance >  Master File to open the G/L Master File
 Maintenance screen. Select either Active or Inactive in the Status section.

## Error - Job Entered Has A Completed Status

If a job code with a status of Complete is entered, this message displays. This error message disallows
 further data entry.
To change the job code's status, click Job Cost >  Maintenace >  Job >  Properties. In the Status
 section, click either Active
 or Inactive.

## Error - Phase Code Entered Is Not Available For Use

If a phase code with a status of Complete is entered, this message displays. This error message disallows
 further data entry.
To change the phase's status, click Job Cost >  Maintenance >  Phase >  Properties and select either Active or Inactive in the Status section.

## Error - Vendor Code Entered Is Not Available For Use

If a vendor code with the status of Not
 used is entered, this message displays. This error message disallows
 further data entry.
To change the vendor's status, click Accounts Payable >  Maintenance >  Vendor >  Properties and select either Active or Inactive in the Status section.

## Error - All Billing Details Must Be Assigned

This error message displays when the key field is missing from the revenue records.
To resolve this issue, complete the following steps.

1. On the Site Map screen, click Project Setup  >  Job Setup.

1. Click the Billing button.

1. On the Billing Detail Setup screen, review the information for
 accuracy. Note: For fixed price jobs,
 entry in the Billing item field is required. For unit price jobs, entry in the
 Billing group and Billing items fields is required.

1. Click OK to return to the Job Setup screen and then click the Update
 button.

1. On the Select Estimate for Update window, complete the
 Job, Estimate type,
 and Reference fields as required and then click OK. Note: The Reference field displays only if the
 Estimate type field is set to
 Change.

1. On the Update Project Setup screen, complete the fields as
 required and then click OK to update the job setup. Note: Remember to select Continue before
 clicking OK.

## Error - All Costs Must Be Assigned Before Proceeding

This error indicates that a required field (Phase or Cost type) is missing on the Job
 Setup screen. To resolve this error, complete the following steps.

1. On the Site Map screen, click
  Project Setup  >  Job Setup.

1. On the Job Setup screen, review the
 data and make any required changes.

1. Click OK until the Update button displays and then click the
 Update button.

1. On the Select Estimatefor Update
 window, complete the Job, Estimate
 type, and Reference fields as required and then click OK. Note: The Reference field displays only if the Estimate type field is set
 to Changeequest.

1. On the Update Project Setup screen, complete the fields as
 required and then click OK to update the job setup. Note: Remember to select Continue before clicking
 OK.

## Error - Invalid Vendor Code Exists

If Project Setup locates an invalid vendor code in Subcontract Setup during Update
 Project Setup, this message displays.
The invalid vendor code error displays when one of the following is
 true:
If the Vendor
 code is blank
When exiting the Subcontract Setup
 screen, you may be prompted to “Clear Subcontract Numbers from Records with No
 Vendor”. This message will appear whenever you attempt to exit the screen when
 there exists phases with subcontract cost types not assigned to a Vendor/Subcontractor.
 The prompt will default to clear these records. However, if you selected to not clear
 records, the system assumes that you will return to work on these and, therefore
 prevents the update until you assign or clear these lines.
If you access this screen and select a non-subcontract cost
 type, for example, Labor should accept the default of Clear Subcontract Number. If you
 don't select this option, then Spectrum assumes that you are still working on these
 records and will not allow the final update to proceed.
Resolution
Assign a different Vendor code to this record.
– OR –

1. On the Site
 Map screen, click Project Setup  >  Job Setup.

1. Click the Listing button.

1. Verify that the Report Type is set to Subcontract.

1. Click Print or Preview.

1. The Additional
 Selections prompt will appear. When the system prompts you for the
 Subcontract cost
 type, type ALL.

1. Review the listing to identify the phase and cost type
 combinations that do not have a vendor code assigned.

1. On the Site
 Map screen, click to Project Setup  >  Job Setup  >  Subcontract > Setup.

1. Enter the Cost
 type(s) that you identified on the listing as "unassigned" and
 update the detail portion of the screen, making sure to assign a Vendor code to these lines.

1. Once you have assigned all subcontractors, click OK to exit the screen.

1. If the system prompts to Clear subcontract numbers,
 accept the default.

1. Perform the Update Project Setup again.

1. If the Vendor
 code is assigned an INACTIVE or NOT USED status.
Your options are to either set the vendor to the status of
 Active or assign the
 record a different vendor code.
Resolution

1. On the Site
 Map screen, click Accounts Payable  >  Maintenance >  >  Vendor.

1. At the Vendor code field, enter
 the vendor whose status you are updating or press F4 to search and select a
 vendor code. Press Enter.

1. Click the Properties button.

1. In the Status
 section of the screen, select the Active option.
