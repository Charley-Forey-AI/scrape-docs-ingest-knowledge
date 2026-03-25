---
title: "Upgrade the Reverse Proxy Server | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/on-premises-deployments/installations/major-release-installation/vista-servers/upgrade-the-reverse-proxy-server"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/on-premises-deployments/installations/major-release-installation/vista-servers/upgrade-the-reverse-proxy-server"
---

# Upgrade the Reverse Proxy Server

This section only applies to you if you are using VRL on-premises and have already installed and set up your remote proxy server.
 When new versions of the Vista application are released, you must download and install the designated file on your reverse proxy server if you are already providing remote access to the Vista client over the internet. However, before you install the executable on the Reverse Proxy server, please note the following:

- This server should be in a workgroup, not attached to a domain.

- You must use a system account, not a domain account, to perform the install; ensure that account has administrator access in order to perform the install.

The following steps guide you through the Vista reverse proxy server upgrade process as a part of the required steps to continue providing remote Vista access to your users, and assume you have already completed the prerequisite steps to install your remote proxy server.

1. Locate and run the Vista_ReverseProxyServer.22.x.x.xx.Rel.exe file on your Vista reverse proxy server. This file is located in the directory it was saved to when it was downloaded from the Viewpoint Customer Portal.It may take a few minutes for the system to prepare the InstallShield Wizard.

1. When the Vista_RemoteLink - InstallShield Wizard appears, select
 Next.The License Agreement screen
 displays.

1. Read the End User License Agreement and select the I accept... radio button.

1. Click Next.The Destination Folder screen displays.

1. Verify that the default location is correct and click Next to accept the location.Note: Changing the default location is not typical. However, if you need to change the location where the CoreConfigurationMonitor is installed, click Change. The system displays the Change Current Destination Folder screen, where you can browse to and select a different location.

The Application Server Hostname/Ports screen displays.

1. The system automatically defaults port values in the applicable fields. Do not change these values. Enter the Application Server's fully qualified domain name and click Next.
The Reverse Proxy Server Hostname/Ports screen displays.

1. In the Vista Reverse Proxy server fully qualitifed domain name field, enter the public URL you use for Vista Remote Link (VRL). Do not change the default Reverse Proxy Server SSL port value. Click Next.
The Choose a Certificate screen displays.

1. Select or supply a certificate using either of the following options:

- In the Select a detected certificate field, select a valid certificate from the list and click Next. No password is required if you select a certificate that is already displayed.

- Click Browse to select a certificate file, enter the password in the Certificate file password field, and click Next. The system installs the certificate once it validates the password you entered.

The Ready to Install the Program screen displays.

1. Click Install.The system begins the installation and displays the Installing Vista™ by Viewpoint Server Upgrade screen. The installation process may take several minutes to finish.

1. In the InstallShield Wizard Completed screen, click Finish.Note: In some cases, the wizard installs required applications. If this has occurred, you may receive and should follow any prompts to reboot the server before continuing.

1. Verify that Vista is running correctly when accessed remotely. To do this, apply the steps found in [Verify Upgrade Success](/en/vista/vista/on-premises-deployments/installations/major-release-installation/verify-upgrade-success).
