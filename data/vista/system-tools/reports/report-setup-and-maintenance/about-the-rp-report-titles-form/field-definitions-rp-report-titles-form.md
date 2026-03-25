---
title: "Field Definitions: RP Report Titles Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-titles-form/field-definitions-rp-report-titles-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-titles-form/field-definitions-rp-report-titles-form"
---

# Field Definitions: RP Report Titles Form

The following is a list of field descriptions for the RP
 Report Titles form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Report ID

 Enter an ID for the new report. Field defaults to the first report on the list.
 When creating a report ID, use a number in the 10,000 – 99,999 range. IDs 1 – 10,000 are reserved for standard Vista™ reports and are not available for selection.
Note: If you enter a new ID by typing “New” or “+,” the next available ID defaults, based on the last one created. For example, the there are available report IDs from 10,000 on, and you choose to use ID 11,000, the next ID create would default to 11,001. ID numbers 10,000 – 10,999 are still available for selection; however, they will require manual selection.

Related information

- [About the RP Report Titles Form](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-titles-form)

## Application

Specify the type of application used for this report title.

- Crystal – Select this option if this report title is for a report created through Crystal Reports.

- SQL Reporting Services – Select this option if this is a SQL Server Reporting Services report. This applies to both SSRS reports that you want to add to a Dashboard Work Center and reports that you want to launch from a Reports folder.

- Other – Select this option if this report title is for a document created through another application (e.g. Word, PDF, HTML, Visio, etc.).

- Dashboard OLAP Report – Select this option if the report title is for a Dashboard report based on the Business Intelligence (BI) module’s OLAP database.

Related information

- [About the RP Report Titles Form](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-titles-form)

## Report Location

Press F4 to select a report location from a list. Report locations are created and maintained using the [RP Report Locations](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-locations-form) form.

## FileName

 Enter the name of the report file, or click
 the Browse icon to select the report from a list. Only reports in the report location
 selected in the Report Location field will display in the list.
 If you are manually entering the file name, make sure the file name exists at the report location specified above.

Related information

- [About the RP Report Titles Form](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-titles-form)

## Title

Enter a title that easily identifies the report. The title can be up to 60 characters long.
By default this field populates with the file name when you are creating a new report.
Note: The title must be unique. For example, it cannot have the same name as a standard report.

Related information

- [About the RP Report Titles Form](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-titles-form)

## Report Type

Press F4 to select a report type from a list.
 Report types are created and maintained using the [RP Report Type
 ](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-type-form) form.
If this is a SQL Reporting Services report
 that you want to be able to add to a Dashboard Work Center, you should select My VP.

## Country

Enter the country that this report applies to
 or press F4 to select it from a list.
This report will only display in the application if the country setting in [HQ Company Setup](/en/vista/vista/administration/headquarters/company-setup/hq-company-setup-form) matches the country selected in this field.

Related information

- [About the RP Report Titles Form](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-titles-form)

## Owner

Use this field to set the owner of the report. Only the owner of the report can modify or delete it.
This field defaults with your user account when you create a new report.
This is a required field.

## Memo

 Enter a memo for the report, up to 255 characters. This field is informational only; it is not used anywhere in Vista™ software.

Related information

- [About the RP Report Titles Form](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-titles-form)

## Description

Enter a description of the report.
Spelling Check
 Click the Spelling icon on the toolbar or
 select Tools > Spelling
  to spell check the text in this field.

Related information

- [About the RP Report Titles Form](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-titles-form)

## Show on Menu

Select this checkbox if the report should display in the Reports folder in the modules where it is assigned. Reports are assigned to module menus using the Assigned Modules tab.
Do not select this checkbox if you do not want this report to show on any Report menu.

Related information

- [About the RP Report Titles Form](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-titles-form)

## Office License Required

The Office License Required checkbox in the RP Report Titles form.
This checkbox is not applicable for enterprises whose license model is
 Concurrent User License (CUL) since all licenses are full access, that is 0-Office. Nearly all on-premises
 deployments use the CUL license model.
The checkbox is relevant only if all the following apply:

- your enterprise license model is Named User License (NUL),

- you have purchased one or more PM-only licenses, AND

- you have set the License
 Type field to 1-PM on one or more user records in the VA User Profile
 form.Note: Only the NUL license model provides the
 option to distinguish between full access (0-Office) and limited access
 (1-PM). To learn more, see [License Types](/en/vista/vista/getting-started/getting-started-with-vista/vista-licensing/license-types).

The ability to change whether it's selected or not depends on the report Status, that is, Standard or Custom.

### Standard Reports

The checkbox is disabled on all reports created by Viewpoint. It is selected for each of these reports which are intended for use only by full-access (0-Office) users.
Security permissions you have assigned to the user ultimately determine whether they can run the report and what data they can see in the rendered report. This means that if a PM-license user with security access to a report runs a standard report which has this checkbox selected, they will still be able to view the report.
However, the system records that user as being a Office-license user for that day.
For more insight to your license usage, see instructions in [Assess License Usage](/en/vista/vista/getting-started/getting-started-with-vista/vista-licensing/assess-license-usage). For general information, see [Vista Licensing ](/en/vista/vista/getting-started/getting-started-with-vista/vista-licensing).

### Custom Reports

The checkbox is enabled on all your custom reports and is not selected by default. All custom reports have these traits:

- Report ID is 10,000 or greater

- Status is Custom

For custom reports, this checkbox controls entries in the Audit Log. Select the checkbox if you want the system to create an entry for each instance this custom report gets run by a user with license type of 1-PM. For instructions on viewing the audit log, go to [View the Audit Log Using the VA Audit Log Viewer Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/maintenance/view-the-audit-log/view-the-audit-log-using-the-va-audit-log-viewer-form).
As with standard reports, security access settings ultimately determine whether the user can run the custom report and what data they can see in the rendered report.

## Force Local Render

The Force Local Render checkbox in the RP Report Titles form.

Select this checkbox if the selected report should render locally on your system with custom applied fonts when printing.
Do not select this checkbox if you want reports to render on the cloud using standard Vista fonts.
Note: This option applies to Crystal Reports only. If you have not customized the font on a report, the report will render with the standard Vista fonts on both the cloud and locally.

## Transactional Report

The Transactional Report checkbox on the RP Report Titles
 form, Info tab.

Important: The
 Transactional Report checkbox works only if you have a
 Vista Enterprise Database. The Vista Enterprise Database is a secondary reporting
 database only available to cloud-hosted customers who have purchased the setup. To
 learn more about this offering, contact your account representative.

Select this checkbox to run a report against the primary transactional Vista
 database *instead* of the Vista Enterprise Database. Executing reports against the
 transactional database allows for real-time reporting with the latest data.
Note: This option applies to Crystal Reports
 only. For non-Crystal reports, this checkbox is grayed-out and disabled.

This checkbox is selected by default for the following reports:

- Payroll batch / check printing process reports

- Batch reporting process reports

For more information about choosing a database for your reporting, see
 [Choose a Database to Run Crystal Reports](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/choose-a-database-to-run-crystal-reports).

## Icon Key

This field and the Change Icon button are
 available only for custom reports that you own. Look for your user account in the [Owner](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-titles-form/field-definitions-rp-report-titles-form#ID-0003dd2f--en) field and Custom in the Status field.
Use this field and the Change Icon
 button to select the icon that is associated with a report. This is the icon that will
 display next to the report in the Reports folders in the application.
To change the icon that is associated with the
 report, click the Change Icon button and then select an icon from a list. Once you have
 selected an icon, the key will populate in this field.

Related information

- [About the RP Report Titles Form](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-titles-form)

## User ID

This fields defaults automatically to your
 user ID when you print the report shown in the Report ID field. It is not editable.

Related information

- [About the RP Report Titles Form](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-titles-form)

## PrinterName

 Enter the default printer. This field defaults to the last printer used by your login.

Related information

- [About the RP Report Titles Form](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-titles-form)

## Paper Source

 Select the specified printer’s paper source from the drop-down list.

Related information

- [About the RP Report Titles Form](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-titles-form)

## Paper Size

 Select the paper size from the drop-down list.

Related information

- [About the RP Report Titles Form](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-titles-form)

## Default Export Format

 Select the default export format from the drop-down list for this report.

Related information

- [About the RP Report Titles Form](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-titles-form)

## Duplex

 Select a duplex print option from the drop-down list.
Duplex printing is printing on both sides of a sheet of paper. Simplex printing is printing on a single side of a page.

Related information

- [About the RP Report Titles Form](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-titles-form)

## Orientation

 Select either Portrait or
 Landscape from the drop-down list.

Related information

- [About the RP Report Titles Form](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-titles-form)

## Last Accessed

 This field displays the last time the report was printed for your login. Field is for informational purposes only.

Related information

- [About the RP Report Titles Form](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-titles-form)

## Zoom

 Enter the zoom factor for the Report Viewer.

Related information

- [About the RP Report Titles Form](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-titles-form)

## Viewer Width

 Specify the width of the Report Viewer based on your monitor’s settings.

Related information

- [About the RP Report Titles Form](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-titles-form)

## Viewer Height

 Specify the height of the Report Viewer based on your monitor’s settings.

Related information

- [About the RP Report Titles Form](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-titles-form)

## Queries: Data Set Name

This field applies to Dashboard Reports only.
Enter the data set that the query belongs to.
 This field defaults the data set name for the Dashboard report when you click Update Design
 on the Info tab.

Related information

- [About the RP Report Titles Form](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-titles-form)

## Queries: Query Text

This field applies to Dashboard Reports only.
Enter the text of the query. This field
 defaults the text of the query for the Dashboard report when you click Update Design
 on the Info tab.

Related information

- [About the RP Report Titles Form](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-titles-form)

## Assigned Templates: Template Name

This field applies to Dashboard Reports only.
Enter the Dashboard template that you want to
 associate this report with. Press F4 for a list of templates.

## Assigned Templates: Active

This field applies to Dashboard Reports only.
Select this checkbox if you want this report for available for selection on the specified Dashboard template.

Related information

- [About the RP Report Titles Form](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-titles-form)
