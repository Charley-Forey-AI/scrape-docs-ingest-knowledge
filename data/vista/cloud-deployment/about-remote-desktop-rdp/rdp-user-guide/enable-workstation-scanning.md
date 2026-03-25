---
title: "Enable Workstation Scanning | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/cloud-deployment/about-remote-desktop-rdp/rdp-user-guide/enable-workstation-scanning"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/cloud-deployment/about-remote-desktop-rdp/rdp-user-guide/enable-workstation-scanning"
---

# Enable Workstation Scanning

If you're an RDP user, scanning documents in Vista over RDP is different due to the nature of the connection between your workstation and the server.
In order to scan documents into Vista while connecting via RDP, you must enable scanning on your workstation. This requires that you download and install the VirtualScan Host application on your workstation.
If you are unsure if you need to enable scanning, contact your system administrator.
Prerequisites:

- You must have access to Viewpoint Customer Portal. If you do not have access, contact your system administrator.

- You must know whether your Windows version is 32-bit or 64-bit. If you do not know, go [refer to this Microsoft resource](https://support.microsoft.com/en-us/help/15056/windows-7-32-64-bit-faq).

To install your scanner client:

1. Download your Windows-version-specific [VirtualScanHost executable](https://app.box.com/shared/zbctlxl15q5y4ycb3dt1xd2thta7iwfu/1/8200705805/68099179633/1) from Viewpoint Customer Portal.

1. Run the VirtualScanHost executable on your workstation.The install welcome window appears.

1. Select Next to open the End-User License Agreement.

1. Read the license agreement and select I accept the terms....

1. Select Next.The Select Installation Folder dialog appears.

1. From the Select Installation Folder dialog, accept the default installation location or choose a different directory by selecting Browse....

1. Select Next.

1. From the Network Setup dialog, clear the Use RDP Virtual Channel checkbox.The Server Address or Name field is activated.

1. In the Server Address or Name field, paste this URL: scan-vec.viewpointforcloud.com.

1. Select Test Server Connectivity.A pop-up message indicates a successful connection.Important: Do not change the Server Port number.

1. Select Next.The Software Update window appears.

1. Select your update preferences, and then select Next.The Ready to Install window appears.

1. Select Install and accept the security pop up message, if prompted.

1. Select Finish and start the software.

You can now scan documents and images into Vista.
