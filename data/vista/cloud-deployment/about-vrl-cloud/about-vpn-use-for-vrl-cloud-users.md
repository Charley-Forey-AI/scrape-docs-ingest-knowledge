---
title: "About VPN Use for VRL Cloud Users | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/cloud-deployment/about-vrl-cloud/about-vpn-use-for-vrl-cloud-users"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/cloud-deployment/about-vrl-cloud/about-vpn-use-for-vrl-cloud-users"
---

# About VPN Use for VRL Cloud Users

Take these steps so that VRL Cloud end users can use the applications that require access to the cloud-hosted Vista database.

- A VPN connection is required for each organization using who has one or more users requiring direct access to the Vista database.

- When you signed up for cloud deployment, Trimble Viewpoint set up a VPN for your company.

- Once Viewpoint set up your company's VPN, the cloud administrator for your company should have received an email that includes the IP address of your cloud server. This is the indicator that your VPN is operational.

- Save the IP address for future use when setting up applications that need to connect through the VPN.

Note: Using the VPN connection is not required for Vista-only use or for Vista users running Crystal Reports.The VPN connection is required for:

- Insight Spreadsheet Server (GSS)

- SAP Crystal Reports

- SSMS

-

- Anything with ODBC

In order for your Crystal Reports designers to access SAP Crystal Reports, a cloud administrator must create a distinct/dedicated SQL account. For instructions, see [Create a Vista Record and
 SQL Service Account - SAP Crystal Reports](/en/vista/vista/cloud-deployment/about-vrl-cloud/about-vpn-use-for-vrl-cloud-users/create-a-vista-record-and-sql-service-account---sap-crystal-reports).
