---
title: "Setting Up Customized SSRS Reports | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/reports/ssrs-overview-and-security-considerations/setting-up-customized-ssrs-reports"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/reports/ssrs-overview-and-security-considerations/setting-up-customized-ssrs-reports"
---

# Setting Up Customized SSRS Reports

If you used Report Builder to create a new SSRS report from
 scratch, use the following information to set up the application so that you can add
 the report to a Dashboard Work Center.
You can also quickly create customized SSRS reports
 by copying a standard SSRS report and then modifying the copy. See
 [Copying a Report](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/create-a-custom-report) for more
 information.

1. Make
 sure that the SSRS report that you created is not saved in
 the Standard folder (VCS/Standard) or any of its
 subdirectories. The reports in this folder are deleted when
 new versions of the reports are installed.

1. Open the Report
 Manager. By default the URL is:
 http://<your_server_name>/Reports.Note: The URL of
 the Report Manager was set up when the BI report
 parts were installed. You can find this URL by
 opening the Reporting Services Configuration
 Manager and selecting the Report Manager URL menu
 option.

1. The custom SSRS
 report should not be in the Standard folder - for
 example you can save it in the Custom folder.
 Custom SSRS reports in the Standard folder will be
 deleted whenever a new version of Vista is installed.

1. Add the
 SSRS report to the application.

1. Open the RP Report
 Titles form in the Reports module. This is the
 form that establishes the link between Vista and the SSRS Report
 Server.

1. Each standard SSRS
 report will display as an item in this form. The
 steps in this process will just add a similar item
 for the new SSRS report.

1. Open the Info tab and
 click the New Record icon ().

1. The Report
 ID populates with a value. The system
 uses this unique value to identify each report.


1. Select SQL Reporting
 Services in the Application drop down.

1. Press F4
 in the Report
 Location field and select the location
 that represents where the SSRS report is saved on
 the SSRS Report Server. For example if you saved
 the report in the Custom folder, select RS_Custom from the list. Note: If the
 report location is not on the list, for example a
 subfolder in the Custom folder, press F5
 to open the RP Report Locations and
 then use that form to create the new
 location.

1. Enter the path of the
 SSRS report in the File
 Name field, and do not include the
 file extension - for example "AR Aging by
 Week-Bobs_Custom".

1. Enter the title of
 the report in the Title field. You will use the title
 to select the SSRS report when adding it to a
 Dashboard Work Center.

1. Press F4
 in the Report
 Type field and select My
 VP. Only SSRS reports with a
 My
 VP type can be added to a Dashboard
 Work Center.

1. By default your user
 name will populate in the Owner field. Only the owner of the
 report can make changes to it after it has been
 saved.

1. (Optional) Enter a
 description of the SSRS report in the Description field - for example a
 description of what the report displays or if this
 is a copy of a standard SSRS report, a description
 of the changes made to the standard.

1. Click the Update
 Parameters button. This will open the
 RP Parameter Update form.

1. Select the Get New
 Parameters option and then click the
 Update button.

1. Open the Assigned
 Templates tab.

1. Add the "1 Report"
 and/or "4 Report" templates to the grid and make
 sure the Active box is checked on both line
 items. The "1 Report" and "4 Reports" templates
 are used for displaying SSRS reports in a
 Dashboard Work Center.

1. Click the Save icon when complete.

1. Administrator: This step needs to be
 performed by someone with access to the Viewpoint
 Administration module. Set up security on each report using
 the VA Report Security form. Users will be able to add SSRS
 reports to their Dashboard Work Center only if they have
 been granted access to them.

1. Add the
 SSRS report to a Dashboard Work Center. Click [here](/en/vista/vista/system-tools/reports/ssrs-overview-and-security-considerations/add-standard-ssrs-reports-to-work-centers) for more
 information.

Related information

- [SSRS Overview and Security Considerations](/en/vista/vista/system-tools/reports/ssrs-overview-and-security-considerations)

- [Add Standard SSRS Reports to Work Centers](/en/vista/vista/system-tools/reports/ssrs-overview-and-security-considerations/add-standard-ssrs-reports-to-work-centers)

- [About the RP Report Titles Form](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-titles-form)

- [About the RP Parameter Update Form](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-parameter-update-form)

- [About the RP Report Locations Form](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-locations-form)

- [VA Report Security Form](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-report-security-form)
