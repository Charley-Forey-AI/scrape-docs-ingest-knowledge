---
title: "Before You Upgrade the Application Server | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/on-premises-deployments/installations/service-pack-installation/vista-servers/before-you-upgrade-the-application-server"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/on-premises-deployments/installations/service-pack-installation/vista-servers/before-you-upgrade-the-application-server"
---

# Before You Upgrade the Application Server

There are a number of things to consider before installing the selected Vista upgrade:

- Do not run the Application installation on a Terminal Services server or workstation.

- All items in standard directories are deleted during the upgrade. Move custom reports and/or custom document templates out of standard directories (that is, Viewpoint Repository\Reports\Standard or Viewpoint Repository\Document Templates\Standard). Custom changes you want to keep must be stored in their respective custom directories (for example, Viewpoint Repository\Reports\Custom or Viewpoint Repository\Document Templates\Custom).

- All users must be logged out of Vista before upgrading.Tip: To prevent users from logging in during the install process, select the Do not allow logins checkbox in the Configure Viewpoint Remote Service application prior to starting the install.

- Installation on the O/S drive (typically C:) requires least 500 MB available disk storage.

- During installation on your server(s), the system may install Microsoft Software Installer (MSI) 4.5, Microsoft .NET Framework 3.5 SP1, Microsoft .NET Framework 4.8, IIS, PowerShell 3.0 (and 4.0 if applicable), as well as some additional Windows roles and features. These are required for Vista to function. Once installed, you may need to reboot your system.Note: Since Microsoft .NET Framework versions are not cumulative, the wizard installs each required version you do not have. This can increase the time required to install.
