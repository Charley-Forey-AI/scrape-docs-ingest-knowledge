---
title: "Process the Viewpoint OLAP Database | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/process-the-viewpoint-olap-database"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/process-the-viewpoint-olap-database"
---

# Process the Viewpoint OLAP Database

BI dashboard reports rely on the Viewpoint OLAP database.
OLAP information is static; the system processes the Viewpoint OLAP database in specified intervals. Processing can be resource-intensive, so it typically occurs during off-hours.
You may want to do this when you add new users to the system or update security for the BI dashboard reports. Refreshing the Viewpoint OLAP database takes a significant amount of time and system resources. Make sure that you pick a time that will cause minimal disruptions to your organization’s daily activities.
Note: To process the Viewpoint OLAP database, you must log into Vista using a domain login. This login must be a member of the sysadmin group on your SQL Server. In addition, you must assign a domain user login to the Viewpoint Remote Service. For more information on setting up domain logins, see [Create a Trusted Connection Domain User](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/account-creation/create-a-vista-domain-user).
To process the Viewpoint OLAP database prior to the scheduled interval:

1. Open VA Business Intelligence.

1. Click the Process and
 Secure button. The system automatically
 processes and refreshes the Viewpoint OLAP database. If you have established
 datatype security (VA Data Security Access), the system applies the security
 to the SSAS Database during processing.

Related information

- [VA Business Intelligence Mgmt Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/va-business-intelligence-mgmt-form)

- [Identify the SSAS Server](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/identify-the-ssas-server)

- [VA Data Security Access Form](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/va-data-security-access-form)
