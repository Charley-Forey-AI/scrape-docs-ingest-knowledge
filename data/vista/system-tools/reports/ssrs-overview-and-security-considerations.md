---
title: "SSRS Overview and Security Considerations | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/reports/ssrs-overview-and-security-considerations"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/reports/ssrs-overview-and-security-considerations"
---

# SSRS Overview and Security Considerations

SSRS (SQL Server Reporting Services) is a server-based report generation application that is included with Microsoft SQL Server version 2008 R2 and later.
If you have the Business Intelligence module and you
 run the Viewpoint SSRS Reports installer, a library of standard reports is installed on
 the SSRS Report Server. These reports are specifically designed to be added to Dashboard
 Work Centers in Vista™, but they can also be emailed to a list of users at
 regular intervals.
Before setting up security on SSRS reports, you should know the following:

- To view an SSRS report in Vista™, a user needs access to the
 report in both Vista and the SSRS Report Server.

- Security is pushed to all SSRS Report Servers that are set up on the RP RS
 Servers form. For example if you have dual SSRS Report Servers, security will
 automatically be pushed to both of the servers.

- When you set up security on an SSRS report using the VA Report Security
 form, the system automatically sets up security on the SSRS Report Server only if
 the Sync
 Security checkbox is selected in RP RS Server. See [Sync Security](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/rp-rs-server-form/field-definitions-rp-rs-server-form#ID-0003deae--en) for more information.

- When you set security on an SSRS report in Vista, the system
 sets up security using item level security. This means that the SSRS report will no
 longer inherit security from the parent folder. If a user has been granted access to
 an SSRS report only at the folder level, that user will no longer be able to access
 the report once Vista changes security on that report to item level.

- There is no company level security on SSRS Reports. If a user can run an
 SSRS report, they can run it for any company. This means when setting up security on
 reports using the VA Report Security form, do not use the Company options to try to
 set up security on a specific company.

- All SSRS security should be maintained using Vista so that the
 security in the application and in the SSRS Report Server stay in sync. The only
 time that you should set up security using the SSRS Report Manager is when a user
 should only be able to access a report using the SSRS Report Manager - for example
 if they are not a Vista user.

- Custom security allows users who log into Vista™ using a SQL login to view SSRS
 reports in Vista. If Custom Security is desired, administrators should
 [submit a support
 case](http://clearview.viewpoint.com/learning-support/submit-support-case) with Viewpoint SupportCustom Security on the SSRS Reports
 Server.

The system will set up a Vista user as a system administrator on the SSRS Report Server when you give them access to any of the following forms:

- VA Report Security

- RP Report Titles

- RP Report Copy

Note: The user needs access to only one of these forms to be a
 system administrator on the SSRS Report Server. For example if they are denied access to
 VA Report Security but can access the RP Report Titles or RP Report Copy form, they will
 still be set up as a system administrator on the SSRS Report Server.
The system will also give the user access to the VCS folder on the SSRS Report Server. This means the following:

- The user will be able to change folder level security on any subfolder in
 the VCS folder.

- The user will be able to access any subfolder or report in the VCS folder
 that has not been set up with item level security. Item level security means that
 there is security set up on a specific folder or report, and that folder or report
 will no longer inherit security from the parent folder.

- If you have set up security on the SSRS reports using Vista, the user
 will only be able to access the reports in the VCS folder that they have been
 explicitly given access to. When you set up security on a report using Vista, the system
 sets item level security on the report. This means security set up at the folder
 level will no longer apply to the report and the user will only be able to access
 the reports that they have been given access to in Vista.

The Viewpoint SSRS Report installer adds a vcsSSRS
 user to the SSRS Report Server. This is the admin account that Vista uses to push
 security to the SSRS Report Server. The system prevents deletion of this account.

Related information

- [Reports](/en/vista/vista/system-tools/reports)

- [Crystal Reports Overview](/en/vista/vista/system-tools/reports/crystal-reports-overview)

- [RP RS Server Form](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/rp-rs-server-form)

- [About the RP Report Copy Form](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-copy-form)

- [VA Report Security Form](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-report-security-form)

- [Add Vista Deep Links to Reports](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/add-vista-deep-links-to-reports)

- [Troubleshooting an SSRS Report Subscription](/en/vista/vista/system-tools/reports/ssrs-overview-and-security-considerations/troubleshooting-an-ssrs-report-subscription)

- [Changing the SSRS Port](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/changing-the-ssrs-port)
