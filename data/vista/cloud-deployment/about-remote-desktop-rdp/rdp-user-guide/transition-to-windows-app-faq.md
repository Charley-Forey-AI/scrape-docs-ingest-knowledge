---
title: "Transition to Windows App FAQ | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/cloud-deployment/about-remote-desktop-rdp/rdp-user-guide/transition-to-windows-app-faq"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/cloud-deployment/about-remote-desktop-rdp/rdp-user-guide/transition-to-windows-app-faq"
---

# Transition to Windows App FAQ

Learn about the upcoming transition to using Windows App
 for Remote Desktop Protocol (RDP) connections. This transition impacts cloud customers
 using RDP to access Trimble's Azure
 Virtual Desktop (AVD) environments.

## General Transition Questions

Why is the Remote Desktop Client (MSRDC) being
 replaced?Microsoft is consolidating its remote connection tools
 into a single, unified gateway called Windows App. This change provides a more secure framework and a
 more consistent experience across Windows, macOS, iOS, and web
 browsers.
Does this impact me? If so, what action do I need to take?If you use the Remote Desktop Client to access Trimble's Azure Virtual
 Desktop (AVD) environments, you should switch to using Windows App to access
 your Trimble AVD
 environment(s). Download and install [Windows App from the
 Microsoft Store](https://apps.microsoft.com/detail/9N1F85V9T8BN).
When is the deadline to switch?The legacy Remote Desktop Client (MSRDC) reaches End
 of Support on March 27, 2026. After this date, the legacy client may no
 longer receive security updates or be able to connect to our Azure
 Virtual Desktop (AVD) environments.

## Setup and Troubleshooting

I downloaded, installed, and signed into Windows App, but it says "No devices found." Where are my apps?This is the most common point of confusion. Windows
 App defaults to the Devices tab (for full desktops).
What to do? Look at
 the sidebar on the left side of the window. Select the Apps icon (it
 looks like a grid of squares). Your Vista and other RemoteApps will
 appear there.
What is my login/username?Continue using your standard Trimble cloud identity.
 The format is typically: first.lastname.cloudCode@viewpoint.cloud.
Do I need to uninstall the old "Remote Desktop" app first?While not required for Windows App to
 function, uninstalling the legacy client may avoid confusion and
 potential protocol conflicts.
To uninstall: On you local Windows computer, go to Settings > Apps > Installed Apps, find "Remote Desktop," and select Uninstall.
I'm getting a "Workspace Not Found" or discovery error
 during sign-in.This usually happens if there is a typo in the email
 address or there is a cached credential issue.

1. Double-check your @viewpoint.cloud email
 address.

1. If it persists, ensure your local machine has a
 stable internet connection and is not blocking Microsoft's discovery
 URLs via a local firewall.

## Features and Performance

Does Windows App support multiple monitors?Yes. Windows App fully supports multi-monitor setups.
 You can configure display settings by right-clicking the app icon within
 Windows App dashboard and selecting Settings.
I use a high-resolution (4K) monitor. Will the text look blurry?No. Windows App features improved High DPI scaling and
 Dynamic Resolution, which automatically adjusts the virtual session to
 match your local screen resolution and scaling settings.
Can I still use my local printer and scanner?Yes. See the following pages for more information:

- [Enable Workstation Scanning](/en/vista/vista/cloud-deployment/about-remote-desktop-rdp/rdp-user-guide/enable-workstation-scanning)

- [Enable Workstation Printing](/en/vista/vista/cloud-deployment/about-remote-desktop-rdp/rdp-user-guide/enable-workstation-printing)
