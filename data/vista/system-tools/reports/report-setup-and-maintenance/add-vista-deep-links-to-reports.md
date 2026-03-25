---
title: "Add Vista Deep Links to Reports | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/reports/report-setup-and-maintenance/add-vista-deep-links-to-reports"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/reports/report-setup-and-maintenance/add-vista-deep-links-to-reports"
---

# Add Vista Deep Links to Reports

Using the Vista™ deep linking functionality, report writers can add hyperlinks into Microsoft SQL Server Reporting Services (SSRS) reports or SAP Crystal Reports that open Vista maintenance forms to a specific record.
With maintenance forms that have header and detail panes, deep links can be created for header records. These links then function when using these reports within the Viewpoint Report Viewer.
Report users who have security permissions to see the report must also have the appropriate security permissions to see the maintenance form that the deep link opens.
Note: The information in this topic assumes that users have received intermediate level training or have previous experience in developing Crystal Reports and/or SSRS Reports.

## Query Structure for Creating Hyperlink Fields

The structure of a query that you would use in Crystal or SSRS to create a hyperlink field looks like this:
dbo.vfLinkToRecordPrefix(FormName) + Company + ‘/KeyName=’ + dbo.vfURLEncode(Field) from View
The query contains:

- dbo.vfLinkToRecordPrefix(FormName) — generates the base prefix of a Viewpoint link for the given form name For example, dbo.vfLinkToRecordPrefix('PMProjectLoc') would produce viewpoint://record/PMProjectLoc/

- dbo.vfURLEncode(Field) — encodes special characters such as whitespace and slashes to make them URL compatible. Any column name that can have a space or special character must be wrapped in the vfURLEncode function.

- ‘/KeyName=’ — placeholder for field names obtained from the record within Viewpoint.

- View — placeholder for the view name obtained from the form within Viewpoint.

For example, to create a hyperlink to a record in the PM Project Locations form, the query would look like this:
select dbo.vfLinkToRecordPrefix('PMProjectLoc') + cast(PMCo as varchar(3)) + '/Project=' + dbo.vfURLEncode(Project) + '/Location=' + dbo.vfURLEncode(Location) from PMPL
In the above example, you can see the FormName “PMProjectLoc”, the PM Company number "1", the two KeyName fields “Project” and “Location”, and the View name “PMPL”.

## Locating the Form Name, KeyName Fields, and View Name

Before you can add deep links to SSRS or Crystal reports, you know the form name, keyname fields, and view name. The following describes how to find this information.Note: You must have MS Outlook installed on your client workstation
 to perform the first step.

1. In the menu bar of the maintenance form to which you want to create the link, select Tools > Email Link to Record.This generates an email containing a link. Here is an example generated from the PM Project Locations form:
viewpoint://record/PMProjectLoc/1/Project=%201988-/Location=Gifford
This link includes the form name “PMProjectLoc”, company "1", and the KeyName fields “Project” and “Location”.

1. In the menu bar of the form, select Tools > Form Properties. In the Form properties window, select the Fields tab. The View column displays the View name. In our example, this would be “PMPL”.

With this information, you can now add a Vista deep link to an SSRS report or Crystal Report.

Related tasks

- [Add a Vista Deep Link to a Crystal Report](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/add-vista-deep-links-to-reports/add-a-vista-deep-link-to-a-crystal-report)

- [Add a Vista Deep Link to an SSRS Report](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/add-vista-deep-links-to-reports/add-a-vista-deep-link-to-an-ssrs-report)

Related information

- [Email a Deep Link to a Record](/en/vista/vista/system-tools/user-interface-guide/system-forms/email-a-deep-link-to-a-record)

- [Reports](/en/vista/vista/system-tools/reports)

- [Crystal Reports Overview](/en/vista/vista/system-tools/reports/crystal-reports-overview)

- [SSRS Overview and Security Considerations](/en/vista/vista/system-tools/reports/ssrs-overview-and-security-considerations)
