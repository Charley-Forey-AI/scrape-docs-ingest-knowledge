---
title: "User Troubleshooting Guide for RDP Users | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/cloud-deployment/about-remote-desktop-rdp/rdp-user-guide/user-troubleshooting-guide-for-rdp-users"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/cloud-deployment/about-remote-desktop-rdp/rdp-user-guide/user-troubleshooting-guide-for-rdp-users"
---

# User Troubleshooting Guide for RDP Users

If you're an RDP user of Vista, Trimble Viewpoint hosts your application on a hosted server. You may encounter situations that require you to accomplish a task in a less familiar way.
The following list details scenarios that you may encounter when using Vista via RDP.

## Why can't I save files to my workstation?

While using Vista over RDP, your application is running on the hosted server and not your workstation. This means that you cannot save items from Vista directly to your workstation. For more information, see [About File Management with RDP](/en/vista/vista/cloud-deployment/about-remote-desktop-rdp/rdp-user-guide/about-file-management-with-rdp).

## Why can't I drag and drop files into Vista?

You can still do this, but when using Vista in RDP, the application is running in the cloud and not at your workstation. This means that you cannot drag and drop to Vista directly from your workstation, but instead you must do it from a location that is hosted in the cloud. For more information, see [Copy Local Files to the Cloud](/en/vista/vista/cloud-deployment/about-remote-desktop-rdp/rdp-user-guide/copy-local-files-to-the-cloud).

## Why can't I locate my printers in the print dialogue?

If you're connected to Vista via RDP, and before you can print from that remote location, you will need to enable printing from your workstation. For more information, see [Enable Workstation Printing](/en/vista/vista/cloud-deployment/about-remote-desktop-rdp/rdp-user-guide/enable-workstation-printing).

## Why are there two versions of Microsoft Word open in my workstation?

During the time you're connected to Vista over RDP, your instance of Vista is running in the cloud, and not from your workstation. Vista requires that a version of Microsoft Word (or any other Microsoft Office application, as applicable) is available in the same location, that is, the cloud. For more information, see [About Microsoft Office with RDP](/en/vista/vista/cloud-deployment/about-remote-desktop-rdp/rdp-user-guide/about-microsoft-office-with-rdp).

## Why am I having trouble scanning documents?

If you are having trouble scanning, try some of these options:

- Before you can scan over RDP, you will need to enable scanning from your workstation. See [Enable Workstation Scanning](/en/vista/vista/cloud-deployment/about-remote-desktop-rdp/rdp-user-guide/enable-workstation-scanning).

- Make sure that sleep mode is not enabled in the power settings for your scanner.

- If you use VirtualScan, use your Windows taskbar to confirm your VirtualScan Host application is in Ready status.

## How do I access SSRS reports?

While connected over RDP, Vista and any other Trimble Viewpoint applications are running on the hosted server.
To access your SSRS reports from your hosted server:

1. Select Start > All Programs > <your organization name> > Google Chrome.

1. In the browser address bar, enter the URL of your reports server location. If you do not know the location of the server, contact your system administrator.

1. Login to SSRS using your credentials.

## How do I export grids?

When using Vista via RDP, you can export the grid but you must save it to your cloud File Explorer. For more information on saving to this location, see [About File Management with RDP](/en/vista/vista/cloud-deployment/about-remote-desktop-rdp/rdp-user-guide/about-file-management-with-rdp).
