---
title: "Field Definitions: RP Report Locations Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-locations-form/field-definitions-rp-report-locations-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-locations-form/field-definitions-rp-report-locations-form"
---

# Field Definitions: RP Report Locations Form

The following is a list of field descriptions for the RP
 Report Locations form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Location

The Location field in the RP Report Locations form.
Enter a report location, up to 10 characters. This field is for informational purposes only.
If you see a red-colored READ ONLY label, the form and its assigned locations are read-only
 and you are not able to change any field values. You can change this setting in the
 Viewpoint Configuration form on the server.

Related information

- [About the RP Report Locations Form](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-locations-form)

## Location Type

Specify the location type for this report location.

- UNC – Network Path — Select this
 type if your documents/files/reports are located on a network path. Use this option
 for Crystal Reports.

- URL – Web Address — Select this
 type if your documents/files/reports are located on a web address (i.e. URL path).
 Use this option with SQL Server Reporting Services reports.

Related information

- [About the RP Report Locations Form](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-locations-form)

## Report Path

The Report Path field in the [RP Report Locations](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-locations-form) form identifies the actual location of each directory and/or web address.
Note: Your company's Vista deployment method affects which actions you should take on this page. Your deployment method is shown at the bottom of the Main Menu in the status bar.

- For network path locations, you can either enter the path manually or, if your deployment method is LAN, click Browse to locate and select the directory where your reports/files are stored. This must be a complete UNC path and cannot be a mapped drive. If you used the Browse For Folder window, click OK to enter the location.

- For web address locations, enter the web address.

Important:Do not save your custom reports to the standard Viewpoint reports directory (Viewpoint Repository\Reports\Standard). Each time you install a release, the update overwrites this directory, thereby removing your custom reports.
Instead, save your custom reports to the Viewpoint Repository\Reports\Custom directory. If you want, you can create additional folders within this custom directory for storing custom reports by module or company\module (for example, Viewpoint Repository\Reports\Custom\Company A\AP, and so on).
The function of this field varies depending on if you are creating a Crystal Reports or an SSRS report location.
Crystal Reports
Enter the full path of the reports (e.g. \\servername\Viewpoint Repository\Reports\Custom), or use the Open Folder icon to locate and select the directory in which your reports are located.
SSRS
If this is an SSRS Report Server, do not enter the entire path - only enter the root path on the SSRS Report Server and any subfolders. For example, if you are creating a location for custom reports that are saved on the SSRS Report Server in "VCS\Custom\BobsReports", enter "VCS/Custom/BobsReports" in this field.
You can also see examples of the portion of the path that should be entered in this field by viewing the standard RS_Custom report location.
Once you have entered a report path, select
 the SSRS Report Server in the RS Server Name field.

Related information

- [About the RP Report Locations Form](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-locations-form)

## Server Name

This field applies only to locations that point to an SSRS Report Server.
Press F4 to select the SSRS Report Server.
 Servers are created and maintained using the [RP RS
 Server](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/rp-rs-server-form) form. You can open this form by pressing F5 in this
 field.

Related information

- [About the RP Report Locations Form](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-locations-form)
