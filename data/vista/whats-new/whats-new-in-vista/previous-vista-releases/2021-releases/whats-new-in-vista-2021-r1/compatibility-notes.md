---
title: "Compatibility Notes | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2021-releases/whats-new-in-vista-2021-r1/compatibility-notes"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2021-releases/whats-new-in-vista-2021-r1/compatibility-notes"
---

# Compatibility Notes

Please consider every item in this section for relevancy to your specific situation.

## Security Improvements Affect Use of Secondary Databases

To improve security, multiple databases on a single server is no longer supported. Please note:

- The Show Database field no longer appears in the login screen.

-  In order to connect to a secondary database, you will need to create a separate test environment for Vista, with a dedicated database and application server.

-  On-premises test environments are not supported without a separate contract.

-  For Cloud test environments, you may purchase a separate, full test environment, at a greatly reduced cost.

## Viewpoint For Content Management (VCM) no longer supported

As previously communicated, support for VCM ended May 31, 2020.
 Viewpoint's focus is on improving your document management and AP invoice approval experience.

## Changes to Microsoft Products Support

- Vista is now compliant with 64-bit versions of Microsoft products.

- Windows Server 2012 - In 2022, Viewpoint will discontinue support of Windows Server 2012.

- Microsoft Windows 7 - Microsoft ended support for Windows 7 on January 14, 2020. As of the Vista 2020 R2 release, Viewpoint no longer supports Windows 7. If you use Windows 7 in Vista 2020 R1 or later versions, you may may experience issues.If you haven't already, Viewpoint strongly recommends that you upgrade to Windows 10 as soon as is practical.

- SQL 2014 - Viewpoint is discontinuing support of SQL 2014 with this release (Vista 2020 R2).

## Future Vista Development Impacts all LAN Connections

In a future Vista release, direct connections to the Vista database from Vista clients, known as the 'LAN' connection method, will no longer be supported. Instead, all Vista users will connect through the Vista Remote Link (VRL) mechanism, which requires the install of the VRL Reverse Proxy server.
Please note, this method is available now and does not require cloud hosting of Vista. If you are not already using Vista Remote Link (VRL) to provide Vista to your end users, Viewpoint highly recommends that you begin the process of planning and implementing it as soon as possible.
