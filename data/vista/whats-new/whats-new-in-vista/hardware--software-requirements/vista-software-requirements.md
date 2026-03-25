---
title: "Vista Software Requirements | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/whats-new/whats-new-in-vista/hardware--software-requirements/vista-software-requirements"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/whats-new/whats-new-in-vista/hardware--software-requirements/vista-software-requirements"
---

# Vista Software Requirements

This article details the currently supported versions of the third-party software products that are required to operate Vista applications, servers, and client workstations.
Customers should *not* upgrade to newer
 versions of these software products until directed by Trimble. As new releases of these components become available,
 Trimble provides compatibility
 information upon request and advises when a new version is required.
Important: This list is periodically
 updated. New third-party products are added to take advantage of new features, while
 older versions of the third-party software on this list may be removed in upcoming
 Vista releases.

## Vista Application and Database Server Requirements

Server Requirements
Operating System

- Windows Server 2022 – recommended
 version

- Windows Server 2016 – minimum supported version

*Not supported:* Windows Small Business Server / Windows Server
 Essentials

Microsoft SQL Server
*Standard or Enterprise versions only*

- SQL Server 2022 – recommended,
 compatible with Vista version 2024 R1 or
 later

- SQL Server 2016 SP2 64-bit –
 minimum supported version

Note: When installing SQL Server:

-  Full Text Search must be installed

- Make sure that the default language is English and that server collation is set to Latin1_General_BIN

- SSRS is required only if you use SSRS reports

ODBC Driver
ODBC Driver 17 for SQL Server – for Vista version 2025.6 and later

Microsoft .NET
.NET Framework 4.8

.NET Framework 3.5.1 and/or 4.5.1 is required for SSRS reporting depending on your version of Microsoft SSRS.

ASP.NET Core 8.0 Runtime Windows Hosting Bundle is required to be installed on the Vista Application server.
SMTP Mail Engine
SMTP mail engine is required to take advantage of all application features.

Crystal Reports
We do not recommend installing Crystal Reports Professional on any Viewpoint server console or Terminal Server.

Microsoft Edge
Latest version

## Vista Remote Link (VRL) Reverse Proxy Server Requirements

Applies only if you are providing remote client access via the internet (VRL). Traditional LAN access does not require use of a reverse proxy server. For more information, see [About Vista Remote Link (VRL) On-premises](/en/vista/vista/on-premises-deployments/access-vista---vrl-on-premises/about-vista-remote-link-vrl-on-premises).
Reverse Proxy Server Requirements
Operating System

- Windows Server 2022 – recommended
 version

- Windows Server 2016 – minimum
 supported version

*Not supported:* Windows Small
 Business Server / Windows Server Essentials

## Client Workstation Requirements

Client Workstation Requirements
Operating System

- Windows 11 – recommended version

- Windows 10 – clients with Windows 10 must have .NET Framework 3.5 installed
 separately, using Windows media

- Windows 2019 Terminal Services Client

Microsoft Outlook and Microsoft Office for Vista*Supported only when using the applications locally*

- 64-bit versions of Microsoft
 Office 2019 and above – recommended, compatible with
 64-bit Vista client

- 32-bit versions of Microsoft
 Office – compatible with 32-bit Vista client

- 2016/2019 versions of all
 Microsoft Office programs – minimum supported
 versions

Microsoft .NET Framework
.NET Framework 4.8 – install before installing the Vista client

ODBC DriverODBC Driver 17 for SQL Server – for
 Vista
 version 2025.6 and later

For creating Custom Reports
Crystal Reports:

- Crystal Reports Designer 2016, which includes its own runtime for running
 Crystal Reports

SSRS Reports:
*At least one of the following is required.*

- Microsoft SQL Server Data Tools for Visual Studio

- Microsoft SQL Server Report Builder – latest version, or the version that
 goes with your Microsoft SSRS version

For running Crystal Reports
Crystal Reports Runtime 2016 SP25 – for
 Vista version 2025.6 and later, matching the bitness of your
 Vista
 client

Microsoft Edge WebView2 Runtime
Evergreen Standalone
 Installer

Web browser for accessing online Vista Help
Latest versions of Chrome, Firefox, Edge, Safari
