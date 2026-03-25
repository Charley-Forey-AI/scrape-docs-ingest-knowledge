---
title: "Modify Service Accounts | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/on-premises-deployments/installations/major-release-installation/vista-servers/modify-service-accounts"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/on-premises-deployments/installations/major-release-installation/vista-servers/modify-service-accounts"
---

# Modify Service Accounts

By default, all Vista services are run under the built-in Network Service account. Changing these accounts is not typical, is not recommended, and is for advanced configuration only.
If you must change the accounts these services run under, follow these instructions. Otherwise, proceed to the section about the [Vista Client Application](/en/vista/vista/on-premises-deployments/installations/major-release-installation/vista-client-application).

1. On the Service Accounts screen, select Change Accounts.The Service Accounts Change screen displays.

1. Select Change next to the field you want to change.

- Viewpoint Windows Services: Runs the Vista windows services (VP Service and Remote Service). To change the network service account, first confirm that the new account has Port Sharing permissions. Two methods of providing these permissions are:

- Include this account in either the Administrators or IIS_IUSRS groups, which have these permissions by default. Then restart services to put the change into effect.

- Add the account to the configuration file for SMSvcHost: SMSvcHost.exe.config. Find the correct copy of SMSvcHost.exe.config and edit it correctly. For more information on editing the config file, search the [MSDN Blogs](http://blogs.msdn.com/). After editing the file, restart services to put the change into effect.

- Vista Identity Service: Runs the Vista Identity Service.

- Vista Data Access Service: Runs the IIS Application Pool for the VRLData IIS service.

- Vista Crystal Access Service: Runs the IIS Application Pool for the VRLCrystal IIS service.

1. On the Service Accounts screen, select the service account.

- Network Service - This option is selected by default.

- Domain Account - If you select this option, enter a Username and Password. When changing the Viewpoint Windows Services account, the login credentials must represent a network service account that has Port Sharing permissions.

1. Select OK.

1. [Upgrade the application server](/en/vista/vista/on-premises-deployments/installations/major-release-installation/vista-servers/upgrade-the-application-server).
