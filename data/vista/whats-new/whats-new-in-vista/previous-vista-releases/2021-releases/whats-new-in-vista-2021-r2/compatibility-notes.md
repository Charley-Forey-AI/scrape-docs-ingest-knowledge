---
title: "Compatibility Notes | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2021-releases/whats-new-in-vista-2021-r2/compatibility-notes"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2021-releases/whats-new-in-vista-2021-r2/compatibility-notes"
---

# Compatibility Notes

Please consider every item in this section for relevancy to your specific situation.

## Security Improvements Affect Use of Secondary Databases

To improve security, multiple databases on a single server is no longer supported. Please note:

- The Show Database field no longer appears in the login screen.

-  In order to connect to a secondary database, you will need to create a separate test environment for Vista, with a dedicated database and application server.

-  On-premises test environments are not supported without a separate contract.

-  For Cloud test environments, you may purchase a separate, full test environment, at a greatly reduced cost.

## Changes to Microsoft Products Support

- Vista is now compliant with 64-bit versions of Microsoft products.

- Windows Server 2012 - In 2022, Viewpoint will discontinue support of Windows Server 2012.

## Future Vista Development Impacts all LAN Connections

In a future Vista release, direct connections to the Vista database from Vista clients, known as the 'LAN' connection method, will no longer be supported. Instead, all Vista users will connect through the Vista Remote Link (VRL) mechanism, which requires the install of the VRL Reverse Proxy server.
Please note, this method is available now and does not require cloud hosting of Vista. If you are not already using Vista Remote Link (VRL) to provide Vista to your end users, Viewpoint highly recommends that you begin the process of planning and implementing it as soon as possible.
For complete information, please see the 2021 R2 Hardware/Software Requirements document, available at the [Downloads page](https://support.viewpoint.com/s/product-more-resources?product=Vista&type=Downloads&links=true&title=Downloads%20for%20Vista) of the Viewpoint Customer Portal. This resource is helpful during the planning stage of any installation.
