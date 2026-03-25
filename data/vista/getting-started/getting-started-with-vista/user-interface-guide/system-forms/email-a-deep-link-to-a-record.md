---
title: "Email a Deep Link to a Record | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/email-a-deep-link-to-a-record"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/email-a-deep-link-to-a-record"
---

# Email a Deep Link to a Record

You can send an email that contains a deep link to a specific record in a maintenance form using the Email Link to Record option in the Tools menu of the form. Deep links can be emailed from any maintenance form that is available from the Folders pane on the [Menu tab](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide) of the Main Menu. With maintenance forms that have header and detail panes, deep links can be emailed for header records.
Note: Senders must have MS Outlook installed on their client workstations.
Note: Recipients can use only MS Outlook to open the link and must have Outlook and Vista™ installed on the same client workstation. Recipients must also have the correct security permissions to access that form and data.
To send an email with a link to the selected record:

1. Open a maintenance form.

1. Select the record for which you want to send a deep link.

1. In the Tools menu, select Email Link to Record.An MS Outlook form or a Vista email form opens with the link to the selected record in the body of the form. Which form opens depends on whether MS Outlook is installed and how the Send Email Via SMTP checkboxes are set in [VA User Profile](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form/field-definitions-va-user-profile-form#ID-00049c6a--en) and [VA Site Settings](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/va-site-settings-form/field-definitions-va-site-settings-form#ID-000499e6--en).

1. Enter the recipient and subject line, and send the email.

Using link to record functionality in SSRS and Crystal Reports
Using this functionality, report writers can create queries that are then used to add deep links to Microsoft SQL Server Reporting Services (SSRS) report or SAP Crystal Reports. When the reports are used within in the Viewpoint Report Viewer, the deep links open Viewpoint maintenance forms to a specific record. For more information, see [Adding Deep Links to Reports](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/add-vista-deep-links-to-reports).
Cautions for recipients with multiple clients installed
Some recipients of emails with deep links may have more than one instance of a Vista™ client installed on a workstation. This might occur, for example, when a recipient is testing a beta version of the Vista client or while transitioning from one version to the next.
In this case, when the recipient clicks the deep link, it may open the record in a different version of the Vista client than what the sender may have intended.
Important: Before making any changes in the record that opens via clicking a deep link, recipients who have more than one version of the Vista client installed on their workstation should carefully check which version has opened when they click the link.
Important: To make sure the link will open the record in the correct instance:

1. Close all instances of Vista on your workstation.

1. Re-open only the instance of Vista that has the record the link should open.

1. Click the link in the email.

Related information

- [System Forms](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms)

- [Form Menu Options](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/form-menu-options)

- [Keyboard Shortcuts for Moving Through Form Fields](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/keyboard-shortcuts-for-moving-through-form-fields)

- [Shortcut Keys](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/shortcut-keys)

- [Date Field Shortcuts](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/date-field-shortcuts)

- [Toolbar Options](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/toolbar-options)

- [Function Keys](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/function-keys)

- [Status Bar](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/status-bar)

- [Record Deletion](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/record-deletion)

- [Batch Processing](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/batch-processing)

- [About the Form Properties form](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/about-the-form-properties-form)

- [Associate a Report with a Form](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/associate-a-report-with-a-form)

- [About the Field Properties Form](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/about-the-field-properties-form)

- [Field Validation](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/field-validation)

- [Schedule Data Changes for Fields](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/schedule-data-changes-for-fields)

- [Search Form Records](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/search-form-records)

- [Group Custom Fields](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/group-custom-fields)

- [Add a Standard Note to a Field](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/add-a-standard-note-to-a-field)

- [Form Grids](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/form-grids)

- [Add Vista Deep Links to Reports](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/add-vista-deep-links-to-reports)
