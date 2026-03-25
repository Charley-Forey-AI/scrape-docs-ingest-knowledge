---
title: "Job Billing Features | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2024-releases/whats-new-in-vista-2024-r1/costs-and-contracts/job-billing-features"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2024-releases/whats-new-in-vista-2024-r1/costs-and-contracts/job-billing-features"
---

# Job Billing Features

Vista 2024 R1
 delivers on user-requested Job Billing enhancements, fixes, and other
 improvements.

## New Bill Control Options to Limit Which Users Can Add,
 Edit, and Delete Bills

You can now limit which users have permissions to add, edit, and
 delete closed-month bills or bills assigned to other users in Job Billing. These
 settings are located on the new Bill Control Options tab on the JB Company
 Parameters form.

Bill control settings apply to both Progress and T&M bills.
 You can enable two different bill control settings, which work independently of each
 other. You can choose to configure them either individually or simultaneously to
 place further limitations on which users can add, edit, and delete bills. These
 settings are optional and apply at the JB company level.
Limit which users can edit or delete bills assigned
 to other usersEnable the Restrict Bill Changes By
 User setting and enter an optional All
 Bills Access Role to control which users can change
 or delete bills assigned to other users.
For more information, see [Set Bill Controls to Restrict Changes to Bills Assigned to Other
 Users](/en/vista/vista/costs-and-contracts/job-billing/setup-and-maintenance-of-job-billing/set-up-job-billing/set-bill-controls-to-restrict-changes-to-bills-assigned-to-other-users).
Limit which users can add, edit, or delete bills in
 closed monthsEnable the Closed Mth Bill
 Control setting, input a closed month, and enter an
 optional Closed Mth
 Bill Access Role to control which users can add,
 edit, or delete bills in closed months in JB.
This setting allows you to close the month in JB
 independent of the last month closed in GL.
For more information, see [Set Bill Controls to Restrict Changes to Bills in Closed
 Months](/en/vista/vista/costs-and-contracts/job-billing/setup-and-maintenance-of-job-billing/set-up-job-billing/set-bill-controls-to-restrict-changes-to-bills-in-closed-months).

For details about each of these bill control fields, see [Field Definitions: JB Company Parameters Form](/en/vista/vista/costs-and-contracts/job-billing/setup-and-maintenance-of-job-billing/set-up-job-billing/jb-company-parameters-form/field-definitions-jb-company-parameters-form#concept-l5w65xul--en).

## New Field on JB Progress Billing and T&M Bill Edit:
 Assigned To

The Assigned To field was added to the JB
 Progress Billing and JB T&M Bill Edit forms, to indicate the owner of the bill.
 The Assigned To user can change or delete the bill. When you
 create a new bill, the Assigned To field automatically
 populates with your username as the owner of the bill.
For existing bills, if someone initializes or edits the bill, the Assigned
 To field defaults to the Created By user. For
 bills where Created By is blank, Assigned
 To populates with the user who saves the record.
If additional Bill Control Options are enabled in JB Company Parameters:

- Other users may have permissions to change or delete bills assigned to
 you.

- Even if you are assigned to a particular bill, you may not have permissions
 to change or delete the bill if the JB month has closed.

For more information about this new field, see [Field Definitions: JB Progress Billing](/en/vista/vista/costs-and-contracts/job-billing/billing/progress-billing/jb-progress-billing-form/field-definitions-jb-progress-billing-form#concept-ixj2fi00--en) or [Field Definitions: JB T&M Bill Edit](/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-bill-edit-form/field-definitions-jb-tm-bill-edit-form#concept-x3rquq1q--en).

## Check Issue Status

To see a list of defects fixed in this version, go to the [Track Cases/Issues page](https://support.viewpoint.com/s/browse-cases-and-issues) of the Viewpoint Customer Portal. Use the filter options to select your product and module. In the Fixed in Version field, select this version, then select Apply Filters.
