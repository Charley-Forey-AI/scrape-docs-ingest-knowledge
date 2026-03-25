---
title: "Changing the SSRS Port | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/reports/report-setup-and-maintenance/changing-the-ssrs-port"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/reports/report-setup-and-maintenance/changing-the-ssrs-port"
---

# Changing the SSRS Port

The Port field in PR RS Server form holds the
 port number for the SQL Server Reporting Service, and defaults to 80.
Generally, you should not have to change the value
 in this field, but you can if necessary. If you do change the value in this field,
 then you must make sure that it matches the value in the TCP
 Port field on the Web Service URL tab of the Microsoft SQL Server
 Reporting Services Configuration Manager.
To change the value in the TCP
 Port field on the Reporting Services Configuration Manager:

1. Change the port number in the Port field of the RP RS Report Server form.

1. On the SSRS server, open the Microsoft SQL Server Reporting Services Configuration Manager.

1.  In the TCP Port field on the Web Service URL tab, change the port number to match the new port number in the Port field of RP RS Report Server form.

1. Navigate to the RSReportServer.config file. For example, this might be D:\Program Files\Microsoft SQL Server\MSRS12.MSSQLSERVER\Reporting Services\ReportServer\RSReportServer.config

1. In the RSReportServer.config file, edit this: <UI>
<CustomAuthenticationUI>
<loginUrl>/Pages/UILogon.aspx</loginUrl>
<UseSSL>False</UseSSL>
</CustomAuthenticationUI>
<ReportServerUrl>http://vs2016q1db01/ReportServerQA</ReportServerUrl>
</UI>
To
<UI>
<CustomAuthenticationUI>
<loginUrl>/Pages/UILogon.aspx</loginUrl>
<UseSSL>False</UseSSL>
</CustomAuthenticationUI>
<ReportServerUrl>http://vs2016q1db01:NEWPORT/ReportServerQA</ReportServerUrl>
</UI>

1. Restart the SQL Server Reporting Service.

Related information

- [RP RS Server Form](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/rp-rs-server-form)

- [SSRS Overview and Security Considerations](/en/vista/vista/system-tools/reports/ssrs-overview-and-security-considerations)
