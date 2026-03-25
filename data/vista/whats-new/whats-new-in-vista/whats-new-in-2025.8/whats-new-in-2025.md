---
title: "What's New in 2025.8 | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/whats-new/whats-new-in-vista/whats-new-in-2025.8/whats-new-in-2025.8"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/whats-new/whats-new-in-vista/whats-new-in-2025.8/whats-new-in-2025.8"
---

# What's New in 2025.8

The Vista 2025.8 release includes several enhancements and new features, as well as defect fixes that apply to all geographies.
Some of the new features in this release include the new Smart Payroll feature with timecard validation, adding Trimble Pay access to Accounts Payable and Subcontract Ledger, and updating email settings to support SMTP OAuth, as well as other enhancements to help improve your workflow.
Form fields may
 be added, removed, or shifted as a result of new features in this release. These
 updates may change the layout of the form and could impact your user-defined UD
 fields. You may need to adjust the position of your UD fields to ensure they still
 display correctly.
Note: With the June release (Vista 2025.6), we introduced the new release cadence for Vista, where the version number now reflects the year and the month of release. For more information, review the [Changes to Vista
 Releases in 2025 FAQ](/en/vista/vista/whats-new/whats-new-in-vista/whats-new-in-2025.6/changes-to-vista-releases-in-2025-faq).

Important: Please be advised that due to a series of defect fixes made just before the final release, the 2025.8 installation files and the Vista application will display the release number as 2025.9. However, it is in fact, the 2025.8 release. When submitting a case or contacting Support, please reference version 2025.8.

## General Features

This release delivers on general user-requested enhancements,
 fixes, and other improvements.
Renamed Viewpoint Help Option in Vista Help Menu to Trimble Help
The Viewpoint Help option displayed in the Help menu of Vista forms and the main menu is now
 labeled Trimble Help. This was
 done to reflect the renaming of the Help site to Trimble Help.

## Accounts Payable

This release delivers on user-requested Accounts Payable enhancements, fixes, and other improvements.
Access to Trimble Pay™ Now Available in Accounts Payable (US only)You can now access Trimble Pay from AP Transaction Entry and AP
 Unapproved Invoice. Both forms now include a  button (upper right of form), that when
 selected, takes you to the Trimble Pay login page.

## Headquarters

This release delivers on user-requested Headquarters enhancements, fixes, and other improvements.
New State Compliance Form
In support of the new Smart Payroll feature being introduced in this release, a new [HQ State Compliance](/en/vista/vista/administration/headquarters/company-setup/hq-state-compliance-form) form was added to the HQ module. This form is used to set up state compliance information, including Department of Labor, Department of Revenue, and Meal Break requirements that will be used by the system when validating timecard batches.
In addition, a new Compliance tab was added to the HQ States form. This tab provides access to the new HQ State Compliance form. You can add or update compliance records using this tab or double-click in the grid to open the HQ State Compliance form.
For information about the Smart Payroll feature, see the [New Smart Payroll Feature](/en/vista/vista/whats-new/whats-new-in-vista/whats-new-in-2025.8/whats-new-in-2025.8#concept-3e40d5f4-2cab-400f-8118-2c6b39ffa9c4--en__PR-RN_SmartPayroll) section in the Payroll release notes.

## Imports

This release delivers on user-requested Imports enhancements, fixes, and other improvements.
Added Field Ticket to the JCCOSTADJ Import
The JCCOSTADJ import form (JC Cost Adjustments) now includes a new FieldTicket column (Identifier #73).
 Upon installation of this release,all existing templates using the JCCOSTADJ import form will be updated to include the new identifier.
Added FLSA Exempt to the PREmpl ImportAs part of the enhancement that adds Smart Payroll functionality to Vista, the PREmpl (PR Employees) import form now includes a new FLSAExemptYN column (Identifier #800).
Upon installation of this release, all existing templates using the PREmpl import form will be updated to include the new identifier.
For information about the Smart Payroll feature, see the [New Smart Payroll Feature](/en/vista/vista/whats-new/whats-new-in-vista/whats-new-in-2025.8/whats-new-in-2025.8#concept-3e40d5f4-2cab-400f-8118-2c6b39ffa9c4--en__PR-RN_SmartPayroll) section in the Payroll release notes.

## Payroll

This release delivers on user-requested Payroll enhancements, fixes, and other improvements.
New Smart Payroll FeatureThis release introduces the Smart Payroll feature. This
 feature is designed to enhance your operational efficiency, help you stay
 compliant, and support you in making informed decisions about your
 payroll.​Smart Payroll is being released in
 several phases. In this release, we introduce the ability to
 automatically identify timecard discrepancies based on defined rules and
 compliance settings, which you can then accept or correct before you
 post the timecards.
In future releases, you can
 expect the following capabilities:

-  ML Powered Data Remediation

- Automated Workflows

- Data Analytics and Reporting

The auto-validation of timecards feature
 introduced in this release enables the system to track timecard
 transactions in real time to help prevent errors before they are posted.
 New timecard entries are compared against the employee's history and/or
 compliance rules (depending on enabled rules and compliance settings),
 and the system highlights any differences. You can then choose to accept
 or adjust the flagged records.
Implementation
 of this functionality includes the following:

- HQ State Compliance (United States only) -
 This new form is used to set up state compliance information,
 including Department of Labor, Department of Revenue, and Meal
 Break requirements. These are set up by country, state, and
 effective date. For more information, see [HQ State Compliance Form](/en/vista/vista/administration/headquarters/company-setup/hq-state-compliance-form).

- HQ States - A new Compliance tab was added
 that provides access to the new HQ State Compliance form. You
 can add or update compliance records using this tab or
 double-click in the grid to open the HQ State Compliance
 form.

- PR Company Parameters - Added a new
 Enable
 Timecard Compliance checkbox and Timecard
 Compliance tab.Selecting the Enable Timecard
 Compliance checkbox (Info tab):

- Enables the Timecard Compliance
 feature. This feature identifies discrepancies on
 timecards based on the employee's history and/or
 compliance rules (depending on enabled rules and
 compliance settings), and then allows you to accept
 them or correct them before you post the
 timecards.

- Enables access to the Timecard
 Compliance tab and PR Timecard Validation Rules
 form.

Note: If the
 Enable
 Timecard Compliance checkbox is not
 selected, you will be unable to access the Timecard
 Compliance tab or the PR Timecard Validation Rules
 form.

- PR Timecard Validation Rules - This new form
 is used to select validation rules and set their severity
 levels and parameter values. The severity level determines how timecard discrepancies
 are handled when they are encountered in a timecard batch and the parameters define how the system uses historical data during timecard validation. For
 more information, see [PR Timecard Validation Rules Form](/en/vista/vista/hr-and-payroll/payroll/time-entry/trimble-smart-payroll/smart-payroll-forms/pr-timecard-validation-rules-form).

- PR Employees - Added a new FLSA Exempt
 checkbox to PR Employees, Add'l Info tab. Selecting this
 checkbox indicates that the employee is exempt under the Fair
 Labor Standards Act (FLSA). The system will use this checkbox
 when validating timecard batches for certain compliance
 discrepancies, such as those defined in HQ State
 Compliance.

- PR TimeCard Compliance - This new form
 provides a list of violated timecard rules and is displayed once
 you select to process a timecard batch. However, it will only
 display if all of the following conditions are met:

- You enabled timecard compliance
 (that is, you selected the Enable Timecard
 Compliance checkbox in PR Company
 Parameters).

- The severity level for the violated
 rules is either Allowed With
 Warning or Not
 Allowed.

- Discrepancies were found in the
 timecard batch based on employee history, enabled rules,
 and/or compliance settings.

You will need to accept, correct, or
 delete all records in the grid before you can submit the
 changes and post the batch. For more information, see [PR TimeCard Compliance Form](/en/vista/vista/hr-and-payroll/payroll/time-entry/trimble-smart-payroll/smart-payroll-forms/pr-timecard-compliance-form).

- PR Pay Period Control - Added a new
 Compliance tab that displays violated timecard rules for the
 selected PR group and pay period, providing an audit record of
 discrepancies that were acknowledged and accepted without being
 corrected. For more information, see [PR Pay Period Control Form](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/pr-pay-period-control-form).

New Race/Ethnicity Category Added to PR Race CodesThe EEO Category dropdown in PR Race Codes now includes a new MENA (Middle Eastern & North African) race/ethnicity category. This option, N-Middle Eastern/North African, applies to individuals with origins in any of the original peoples of the Middle East or North Africa.

## Purchase Order

This release delivers on user-requested Purchase Order enhancements, fixes, and other improvements.
Expanded 'Requested By' Character Allowance
To accommodate longer user names, the following fields now support a 128-character limit:FormField
PO Requisition EntryRequested By
PO Requisition InitializeRequestor

This enhancement prevents the truncation of user
 names (from VA User Profile) that auto-populate the Requested By field
 (in PO Requisition Entry) when you enter and initialize requisitions in
 PM Material Detail.

## Subcontract Ledger

This release delivers on user-requested Subcontract Ledger enhancements, fixes, and other improvements.
Access to Trimble Pay™ Now Available in Accounts Payable (US
 only)You can now access Trimble Pay from AP Transaction Entry and AP
 Unapproved Invoice. Both forms now include a  button (upper right
 of form), that when selected, takes you to the Trimble Pay login page.

## Viewpoint Administration

This release delivers on user-requested Viewpoint
 Administration enhancements, fixes, and other improvements.
Introducing SMTP OAuth for Vista & Changes to Email SettingsReview the following updates that make sending emails
 through Vista simpler and more secure for your organization.

- Email Settings consolidated
 onto new tab in VA Site Settings: The new
 Email
 Settings tab contains all current and new email
 controls. For more details about these
 fields, see [Field Definitions: VA Site
 Settings](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/va-site-settings-form/field-definitions-va-site-settings-form#ID-000499e6--en).

- New email settings for SMTP
 OAuth: Admins can now configure OAuth settings
 in order to securely send emails from Vista. We recommend
 choosing an email provider that supports SMTP OAuth. For more details about configuring these
 settings, see [Configure SMTP OAuth Email Settings in
 Vista](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/set-up-vista-to-send-emails/configure-smtp-email-settings/configure-smtp-oauth-email-settings-in-vista).
Important:Attention all customers using Microsoft 365 as
 your email provider:If your current email client is
 Microsoft 365, you *must set up SMTP OAuth before March 2026*. At this time, the
 current Basic Auth configuration will be retired, and your emails will no longer
 work.
We've enhanced our email settings and provided
 options for setting up [SMTP OAuth](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/set-up-vista-to-send-emails/configure-smtp-email-settings/configure-smtp-oauth-email-settings-in-vista) in order to assist you with this transition. We encourage
 you to reconfigure your email relays as soon as possible before the deadline.
 Look for additional communications as this date approaches.

- Test email option added
 to VA Site Settings: The new Send Test
 Email option at the bottom of the Email Settings
 tab simplifies testing your email relay to make sure it works
 before changing your existing configuration. For more details about sending test
 emails, see [Test Your Vista SMTP Email Configuration](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/set-up-vista-to-send-emails/test-your-vista-smtp-email-configuration).

Review the new Email Settings tab layout on the VA
 Site Settings form.

## Check Issue Status

To see a list of defects fixed in this version, go to the [Track Cases/Issues page](https://support.viewpoint.com/s/browse-cases-and-issues) of the Viewpoint Customer Portal. Use the filter options to select your product and module. In the Fixed in Version field, select this version, then select Apply Filters.
