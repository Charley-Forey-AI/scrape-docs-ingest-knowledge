---
title: "Link Report Files to Vista | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/reports/report-setup-and-maintenance/link-report-files-to-vista"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/reports/report-setup-and-maintenance/link-report-files-to-vista"
---

# Link Report Files to Vista

Use the Report Titles form to establish the link between reports and/or other files and the Vista application.
If your deployment method is VRL Cloud, some steps are different than those on this page. If needed, see [Set Up New Custom Vista Reports in VRL Cloud](/en/vista/vista/cloud-deployment/about-vrl-cloud/vrl-cloud-user-guide/set-up-new-custom-vista-reports-in-vrl-cloud).
You can use the RP Report Titles form to create records that are then linked to reports, documents, and/or files that you have created using Crystal Reports, SQL Server Reporting Services, Excel, or other applications.Note: If you want to create a new report based on an existing standard or custom report, use the RP Report Copy form. For more information, see [Copying a Report.](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/create-a-custom-report)

1. Create the report using the appropriate application. Note: Make sure to place the report in the location that you specified for this type of report in RP Report Locations.

1. In RP Report Titles, enter an ID number in the Report ID field, using an available number in the 10,000 - 99,999 range. Tip: You can also enter N, New, or + for the system to generate the next number. However, the Report IDfield defaults to the next available ID, based on the last one created. For example, if you had available ID’s starting from 10,000, and you chose to use 11,000, the next ID created would default to 11,001. Numbers 10,000 – 10,999 would require manual selection.

1. Select the application that you used to create the report from the Application drop-down field.

1. Enter the location of the report in the Report Location field. Press F4 for a list of report locations.

1. Enter the report type in the Report Type field. Press F4 for a list of report types.

1. Enter the country that this report applies to in the Country field. Press F4 for a list of valid countries.

1. Enter a valid login name in the Owner field to identify the person who created this report title. Press F4 for a list of login names. Note: When adding a new report title, the report's Owner defaults to the current user login. If you want to change the owner of a report after you have created and saved the title, you must use the Change Owner option in the File menu. For more information, see [RP Change Report Owner ](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-change-report-owner-form).

1. Enter an informational memo about the report in the Memo field, as necessary.

1. Enter a description that explains the function of this report in the Description field. Note: For reports created using Crystal Reports or SQL Server Reporting Services, this description displays on the Report Info tab of the RP Report Launcher.

1. Check the Show On Menu box to have the report display in the Reports folder (Main Menu) of any module that the report is assigned to (Assigned Modules tab).

1. Specify an icon for the report in the Icon Key field. If you do not know the name of the icon, click Change Icon and select an icon from the Icon Viewer.

1. If you selected Crystal, My Viewpoint Report, or My Viewpoint OLAP Report from the Application drop-down field, click Update Design to update information on the Layout tab and, for the My Viewpoint reports, update the query information on the Queries tab. Note: The Layout tab displays the specified report’s design; this tab is for display purposes only and you cannot change the report’s actual layout here. Make sure to click Update Design each time changes are made to a report’s design.

1. Specify the parameters for the report on the Parameters related tab or on the RP Report Parameters form. Note: If you are creating a report title for a Crystal report, click Update Parameters to import the parameters into Viewpoint (RP Report Parameters) automatically.

1. Assign the report to [modules](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-reports-by-module-form) and [forms](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-reports-by-form-form), as necessary.

1. To change the printing and viewing settings for this report for specific users on the Printer/Viewer Options tab, edit the default printer name, paper source, paper size, default export format, duplexing, orientation (Portrait or Landscape), as well as viewer width and height. Generally, this step is unnecessary.

1. For Dashboard reports, assign the templates to associate this report with on the Assigned Templates tab. Enter the template name in the Template Name field, or press F4 for a list of templates. Check the Active box to have the report available for selection from a report part on the [Dashboard Work Center](/en/vista/vista/system-tools/work-centers/about-the-dashboard-work-center).

1. Save the record as normal. The report is automatically added to the RP Reports folder on the Main Menu. Note: You can delete report titles by selecting Records  Delete or by clicking the Delete button on the toolbar. Deleting a report title does not actually delete the report. Instead, it will remove only the title and the report parameters, as well as remove the report from any menu to which it was assigned. When you delete a report title, the system will ask if you want to remove all parameters. Click Yes to delete the report title, but the parameters are only removed from the RPRF database table, not from the report itself.

Note: If you assigned a custom report to an SM customer (in SM Customers), service site (in SM Service Sites), and/or invoice (in SM Invoice Review), you will receive a message indicating the report exists in SM and you will be unable to delete the report.

Related information

- [About the RP Report Titles Form](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-titles-form)

- [About the RP Reports by Form Form](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-reports-by-form-form)

- [About the RP Reports by Module Form](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-reports-by-module-form)
