---
title: "About File Management with RDP | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/cloud-deployment/about-remote-desktop-rdp/rdp-user-guide/about-file-management-with-rdp"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/cloud-deployment/about-remote-desktop-rdp/rdp-user-guide/about-file-management-with-rdp"
---

# About File Management with RDP

When working over an RDP connection, there are a few things to keep in mind about how you save, store, and retrieve your files for use across the different cloud-hosted applications.
When saving files from or adding files to Vista in an RDP environment, you must use the H: drive, which is the hosted location. This file storage location comes with your cloud environment and acts as your company's shared drive.
You need to use the H: drive because your Vista application is running at the hosted location and not your workstation. This means that you cannot save files directly to your workstation, but you can save them to the H: drive. The H: drive is located at the hosted location and is therefore accessible by both your Vista application and your workstation.
For instances where you have a file on your local workstation that you want to add to Vista, you must first copy it to the H: drive. From there, you can either drag the file into Vista or attach the file from within Vista using the Browse window.
Note:Vista's import function is another form of adding files into Vista from your workstation and therefore also relies on the source file being located somewhere on the H: drive. During the import process, you must direct the import wizard to the location on the H: drive that the source file is located.
