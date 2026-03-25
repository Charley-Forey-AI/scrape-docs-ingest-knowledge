---
title: "Installation Instructions for Major Releases: Overview | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/on-premises-deployments/installations/major-release-installation/installation-instructions-for-major-releases-overview"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/on-premises-deployments/installations/major-release-installation/installation-instructions-for-major-releases-overview"
---

# Installation Instructions for Major Releases: Overview

The following provides a high-level overview of the installation process for each release.
Important: If you have made extensive
 customizations (reports, custom triggers, etc.) you should install this release
 on a test system to verify your customizations are working correctly before
 installing the release in a live environment.

1. Review the release notes. You can access the
 release notes here on Viewpoint
 Help:

1. From the left side menu, select What's New.

1. On the main What's New page, select the
 module links to access the release notes for each module.

1. Review the [Hardware / Software Requirements](/en/vista/vista/whats-new/whats-new-in-vista/hardware--software-requirements).

1. Back up your Vista database, Viewpoint Repository folder, and Viewpoint Remote Services folder.

1. Download the Vista installation file(s) from the Viewpoint Customer Portal. Make sure to download any prerequisites before installing the Vista client. Specifics are provided in the [Vista Installation Files Download](/en/vista/vista/on-premises-deployments/installations/major-release-installation/vista-installation-files-download) section.

1. Upgrade your Vista database and application servers. For specifics, see the [Vista Servers](/en/vista/vista/on-premises-deployments/installations/major-release-installation/vista-servers) section.Note: Make sure that all users are logged out before beginning. The upgrade process can take one (1) hour or more to complete.

1. Install the File System API. For instructions, see [Install the Vista File System API](/en/vista/vista/on-premises-deployments/installations/major-release-installation/vista-servers/install-the-vista-file-system-api).

1.  If you are providing remote Vista client internet access using Vista Remote Link, upgrade your Vista reverse proxy server. Refer to [Upgrade the Reverse Proxy Server](/en/vista/vista/on-premises-deployments/installations/major-release-installation/vista-servers/upgrade-the-reverse-proxy-server) for specifics.Note: If you have Vista Remote Link set up, stop the Internet Information Services (IIS) server or the default website in IIS before proceeding with your upgrade to prevent users from logging on during the process.

1. If you use SSRS reports, you're not required to run the SSRS installer, but doing so will do no harm. If and when an SSRS reinstall is required, we will specify in a future version of this install guide.
