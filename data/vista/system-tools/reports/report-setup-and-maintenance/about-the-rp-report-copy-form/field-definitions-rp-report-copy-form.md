---
title: "Field Definitions: RP Report Copy Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-copy-form/field-definitions-rp-report-copy-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-copy-form/field-definitions-rp-report-copy-form"
---

# Field Definitions: RP Report Copy Form

The following is a list of field descriptions for the RP
 Report Copy form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Source Report: Report ID

Use this field to select the report that you
 would like to copy. Press F4 to select a report from a list.
 Standard SSRS reports display in the list only if the Business Intelligence module is
 turned on.
If you launched this form using the Copy Report
 button the [RP Report Titles](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-titles-form) form, this field defaults to the report
 that you selected on the RP Report Titles form.

Related information

- [About the RP Report Copy Form](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-copy-form)

## New Report: Report ID

This field displays the ID number of the report that will be created, and it automatically defaults to the next available number.

Related information

- [About the RP Report Copy Form](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-copy-form)

## Title

 Enter the title of the new report. The title can be up to 60 characters long and must be unique.

Related information

- [About the RP Report Copy Form](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-copy-form)

## Location

 This field displays where the new report will
 be saved. Press F4
 to select a different location from a list.
Locations are created and maintained using the
 [RP Report Locations](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-locations-form) form. You can open this form by
 pressing F5 in this field.
When copying an SSRS report
Custom folder
When copying an SSRS report, this location will default to the Custom folder on the SSRS Report Server. This is where all custom SSRS reports should be stored. Any reports saved in the Standard folders on the SSRS Report Server will be deleted when you upgrade to a new version of Vista™.
Dual SSRS Report Servers
If you have dual SSRS Report Servers, you
 cannot copy a report from one SSRS Report Server to another. This means that you cannot
 select a location in this field that is associated with a different server.
For information on how to copy a report from
 one SSRS server to another, see [SSRS - Copy a report to a different SSRS Server](/en/vista/vista/system-tools/reports/ssrs-overview-and-security-considerations/copy-an-ssrs-report-to-a-different-server).

Related information

- [About the RP Report Copy Form](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-copy-form)

## File Name Prefix

 Use this field to add a prefix to the file name that is created. By default this field is "Custom".
For example if the prefix is Custom and the
 file name is JCjmsum.rpt, the file name of the copied report will be CustomJCjmsum.rpt. You
 can see the path and file name of the copied report in the New Path
 field.

Related information

- [About the RP Report Copy Form](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-copy-form)

## File Name

 Enter the name of the report file. The prefix
 will be added to the text in this field. You can see the path and file name of the copied
 report in the New
 Path field.
The file name must not already exist at the
 location selected in the Location field.

Related information

- [About the RP Report Copy Form](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-copy-form)

## Report Type

 Press F4 to select a report type (e.g. Acctg,
 Audit, Form, etc.) from a list. By default, this field will populate with the report type
 of the report being copied.
Report types are created and maintained using
 the [RP Report Titles](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-titles-form) form. You can open this form by pressing
 F5
 in this field.
When copying SSRS Reports
Select My VP in this field if you would like to
 add the SSRS report to a Dashboard Work Center.

Related information

- [About the RP Report Copy Form](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-copy-form)

## Report Owner

 This field displays the owner of the report. By default, it populates with your user account.
The owner is the only user that can make changes to the report after it has been copied.
Once the report has been copied, you can change the owner of a report only by using the [RP Change Report Owner ](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-change-report-owner-form) form.

Related information

- [About the RP Report Copy Form](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-copy-form)

## Memo

 Enter a memo, up to 255 characters. This field is informational only; it is not used anywhere in Vista.

Related information

- [About the RP Report Copy Form](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-copy-form)

## Description

Enter a description that explains the function of this report. Space allowance is virtually unlimited. This description can be viewed in the “Report Information” report.

Related information

- [About the RP Report Copy Form](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-copy-form)

## Show On Menu

 Select this checkbox if the new report
 should display in the Reports folder for each module that it is assigned to. You can assign
 reports to module menus using the Assigned Modules tab in [RP Report Titles](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-titles-form).
If the Assigned Modules box is checked, the
 modules associated with the source report will be copied to the new report.

Related information

- [About the RP Report Copy Form](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-copy-form)

## Icon Key

Use this field and the Change Icon
 button to select the icon that is associated with a report. This is the icon that will
 display next to the report in the Reports folders in the application.
To change the icon that is associated with the
 report, click the Change Icon button and then select an icon from a list. Once you have
 selected an icon, the key will populate in this field.

Related information

- [About the RP Report Copy Form](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-copy-form)

## Copy Options

This section of the RP Report Copy form allows you to copy particular settings from the Source Report. Available copy settings are discussed below.

- Assigned Forms w/Parameter Defaults – This option assigns the same forms and parameter defaults to the new report as the source report. To assign additional forms, use RP Reports by Form.

- Assigned Modules – This option assigns the same modules to the new report as the source report. To assign additional modules, use RP Reports by Module.

- Report Security – Check this box to copy the security of the source report to the new report.

When copying an SSRS report
When copying an SSRS report, checking this box means that security will be copied and pushed to the SSRS Report Server.
If you do not check this box, security will not be copied. This means you will have to set up security on the report using the [VA Report Security](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-report-security-form) form after it has been copied.

- Printing Preference – This option assigns the printing preferences (set on the Printer/Viewer Options tab in RP Report Titles) of the source report to the new report.

 These fields default as checked for all source reports that have associated parameters. You can override this setting using a system or user override in the [Field Properties](/en/vista/vista/system-tools/user-interface-guide/system-forms/about-the-field-properties-form) (F3) form.

Related information

- [About the RP Report Copy Form](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-copy-form)
