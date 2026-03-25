---
title: "Create a Vista Record and SQL Service Account - SAP Crystal Reports | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/cloud-deployment/about-vrl-cloud/about-vpn-use-for-vrl-cloud-users/create-a-vista-record-and-sql-service-account---sap-crystal-reports"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/cloud-deployment/about-vrl-cloud/about-vpn-use-for-vrl-cloud-users/create-a-vista-record-and-sql-service-account---sap-crystal-reports"
---

# Create a Vista Record and
 SQL Service Account - SAP Crystal Reports

Crystal Reports application users in VRL Cloud must use the Crystal Reports service account in order to modify reports or to change the data source. This app-specific record provides access to the cloud-hosted database using the VPN.
Note: The VPN connection is required for SAP Crystal Reports, but not for Vista-only use.

A Vista user with access to the VA User Profile form must create this service account record.

1. Open the VA User Profile form.

1. Select the New Record icon.

1. In the Full Name field, enter crystal.svc.

1. Select Save.A prompt appears indicating there is no matching SQL record and that a new one will be created.

1. Close the prompt.A password creation window appears.

1. Enter a password for the user.Note: Passwords must meet the following guidelines:

- must not contain the account name of the user.

- at least eight characters long.

- contains characters from at least three of these categories:

- uppercase letters (A through Z)

- lowercase letters (a through z)

- base 10 digits (0 through 9)

- non-alphanumeric characters such as !, $, #, %.

1. Select OK.

1. If needed, select Save.

You’ve established the connection to your server using the VPN. You now have access to you VRL Cloud database server for using the desired 3rd-party application(s).Note: The VPN connection you have just established is not permanent. You must re-connect each time you need to access any of the 3rd-party applications on the server.

Before you can modify reports:

1. Log into your VRL Cloud Vista account and create a SQL user for use with SAP Crystal Reports.Note: For example, a suggested format is 'CrystalODBC.svc'.

1. Open 32-bit ODBC on the system that has Crystal Designer on it, and configure ODBC with your cloud server IP address and the new SQL user you created in the previous step.Note: The cloud administrator for your company should have received an email from Viewpoint that includes the IP address of your cloud server.
Use the name and password you just created when prompted for the ODBD name and password while editing each Crystal Report.
