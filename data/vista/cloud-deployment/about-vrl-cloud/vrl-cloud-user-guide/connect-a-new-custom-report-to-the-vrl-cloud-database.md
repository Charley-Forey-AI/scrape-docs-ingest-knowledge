---
title: "Connect a New Custom Report to the VRL Cloud Database | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/cloud-deployment/about-vrl-cloud/vrl-cloud-user-guide/connect-a-new-custom-report-to-the-vrl-cloud-database"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/cloud-deployment/about-vrl-cloud/vrl-cloud-user-guide/connect-a-new-custom-report-to-the-vrl-cloud-database"
---

# Connect a New Custom Report to the VRL Cloud Database

If you create custom reports and if your deployment method is VRL Cloud, you need to configure each new custom report.
You will need a VPN connection to your server and a SQL login account in order to connect the Crystal Reports application to the D1 server. If you do not have these, request them from your system administrator.In order to connect each custom report to the proper database, the same Data Source Name (DSN) that Viewpoint personnel already created on your organization's cloud server must match the DSN on the computer where you are running the Crystal Reports designer.

If you need to set up your local DSN, complete the following:

1. From the Start menu on your local computer, go to Control Panel > Administrative Tools > Set up ODBC data sources (32-bit).The ODBC Data Source Administrator (32-bit) window opens.

1. Select the System DSN tab and choose Add.

1. In the Create New Data Source window, select the driver. Choose from:

- SQL Server

- ODBC Driver 17 for SQL Server

1. Select Finish.

1. In the Name field, enter VistaCrystal. Optionally, you can add a description of the data source.

1. Set the Server to <cloud server address>,<SQL port for VPN>.For example: code-sql.viewpointdata.cloud,1234

1. Select Finish.

1. Review the configuration for the new ODBC data source, then select OK.

To make your local DSN match the DSN on your server for a Crystal Report, complete the following:

1. Log into your VPN. You can skip this step if you are already connected to your corporate network.

1. Open the report in the Crystal Report editor.

1. Navigate to Database > Set Datasource Location.The Set Datasource Location window appears.

1. Under Replace with, expand Create New Connection, then expand ODBC (RDO).The Data Source Selection window appears.

1. In the Data Source Name list, select whichever DSN appears in your list (this was created by Viewpoint personnel):

- Viewpoint

- VistaCrystal

1. Select Next. The Connection Information window appears.

1. Enter your password.Note: These credentials are not saved with the report. They grant you access to the database and table explorer within the Crystal Report editor. At run time, Vista enforces security using the credentials of the logged-in user.

1. Select Finish.The system returns you to the Set Datasource Locations window.

1. Under Current Data Source, select the existing database connection.Under Replace with, select the new database connection.

1. Under Replace with, select the new database connection.

1. Select Update.The entry in the Current Data Source field updates with the name of the new connection.

1. Select Close.

The DSN on your local computer now matches that of your server.
You must now test the report from within the Crystal Reports application, save the report, and [upload it to the Vista Application Server](/en/vista/vista/cloud-deployment/about-vrl-cloud/vrl-cloud-user-guide/upload-custom-crystal-report-files-to-vista-in-vrl-cloud).Note: While in the Crystal Reports application, you should change a default setting for new reports. For each new custom report, go to File and clear the Save Data with Report checkbox. Save the report after changing this setting.
