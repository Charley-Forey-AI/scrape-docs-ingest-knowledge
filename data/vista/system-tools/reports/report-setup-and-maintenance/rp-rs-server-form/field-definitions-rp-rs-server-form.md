---
title: "Field Definitions: RP RS Server Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/reports/report-setup-and-maintenance/rp-rs-server-form/field-definitions-rp-rs-server-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/reports/report-setup-and-maintenance/rp-rs-server-form/field-definitions-rp-rs-server-form"
---

# Field Definitions: RP RS Server Form

The following is a list of field descriptions for the RP RS
 Server form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Server Name

The entry in this field is created by the Viewpoint SSRS Reports installer. Generally, you should not have to change the value in this field.
This field holds the name the SSRS Report
 Server. The name is used to select the Report Server when associating it with a location
 using the RS Server
 Name field on the [RP Report Locations](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-locations-form) form.
The server name can be up to 255 characters long.

## RS Server

The entry in this field is created by the Viewpoint SSRS Reports installer. Generally, you should not have to change the value in this field.
This field holds the address of the SSRS Report Server.
If you do enter a new value in this field, do not include any \'s in the path in this field, For example, "\\ServerName" would be entered as ServerName.

## Port

This field holds the port number to the SSRS Server name. The entry in this field is created by the Viewpoint SSRS Reports installer, and defaults to 80. Generally, you should not have to change the value in this field.
If you do change the value in this field, then
 you must make sure that it matches the value in the TCP Port field on the Web Service URL tab
 of the Microsoft SQL Server Reporting Services Configuration Manager. For information on
 how to make this change, see [Changing the SSRS
 Port](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/changing-the-ssrs-port).

## Report Server Directory

The entry in this field is created by the Viewpoint SSRS Reports installer. Generally, you should not have to change the value in this field.
This field holds the directory of the SSRS Report Server instance.

## Report Manager

The entry in this field is created by the Viewpoint SSRS Reports installer. Generally, you should not have to change the value in this field.
This field holds the name of the SSRS Report Manager instance.

## Custom Security

This box is always disabled and is checked if you installed Custom Security when you ran the Viewpoint SSRS Reports installer. See [Custom Security on the SSRS Reports Server](/en/vista/vista/system-tools/reports/ssrs-overview-and-security-considerations) for more information about the Custom Security.

## Sync Security

The Sync Security checkbox in the RP RS Server form.
Defaults to unchecked. If left unchecked, Vista will not sync report security for SSRS reports on the selected RS Server when applying report security in VA Report Security. It will also not sync changes to the SSRS server when running any program that updates report security. This includes, for example, deleting a user in VA User Profile and adding or deleting a user from a group.
However, leaving the checkbox unselected will also allow report security updates to run faster. This is useful when:

- You maintain SSRS report security manually, or

- You do not have SSRS servers set up.

 If the checkbox is selected, Vista syncs SSRS report security automatically when applying report security in VA Report Security or running any program that updates report security.

Related information

- [Sync Vista Report Security to the SSRS Server](/en/vista/vista/system-tools/reports/ssrs-overview-and-security-considerations/sync-vista-report-security-to-the-ssrs-server)

- [RP RS Server Form](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/rp-rs-server-form)

- [VA Report Security Form](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-report-security-form)

- [Apply Report Security Settings](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/apply-report-security-settings)
