---
title: "Install the Vista Client Application on a Workstation | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/on-premises-deployments/access-vista---local-area-network-lan/install-the-vista-client-application-on-a-workstation"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/on-premises-deployments/access-vista---local-area-network-lan/install-the-vista-client-application-on-a-workstation"
---

# Install the Vista Client Application on a
 Workstation

The Vista
 client is a software application used to connect a workstation to the server. The
 client-server connection allows you to use Vista while accessing data
 stored at the server location.
Install the client as part of new user setup or when
 you have just re-installed the client on a workstation that's already been
 set up.Note: If your organization uses RDP
 or legacy cloud, you do not need to install the client because
 Trimble Viewpoint does this for you.
Before you proceed,
 download the application executable from the [Product Downloads](https://support.viewpoint.com/s/product-more-resources?product=Vista&type=Downloads&links=true&title=Downloads%20for%20Vista) section of
 the Viewpoint Customer Portal.
The following steps guide you through the
 installation process for the client application.

1. Locate and double click
 the VistaClient.2X.X.X.XXX.Rel.Msi file in the directory
 it was saved to when it was downloaded from Viewpoint Customer Portal. The system prepares
 the InstallShield Wizard.

1.  On the Viewpoint Client InstallShield Wizard, click Next.

1. In the Destination Folder screen, click Next to accept the default location.Note: If you are re-installing the client, changing the location is not typical. However, you can change the destination location by clicking Change and selecting a different location.

1. What you see next depends on whether you have Microsoft Outlook already installed on the workstation:

- If you do not have Microsoft Outlook installed on
 the workstation, or if you have a 64-bit version
 of Outlook, the system displays the Ready to
 Install the Program screen. In this case, proceed
 to the next step.

- If you have Microsoft Outlook installed on the workstation, the wizard displays the Custom Setup screen, where you can choose which components to install on the workstation. If you do not want to install the Outlook add-in, select the drop-down arrow to the left of the component and select the This feature will not be available option. Click Next when you are ready to proceed to the next step. For more information, see [About the Vista Add-in for Microsoft Outlook](/en/vista/vista/system-tools/document-management/dm-setup-and-maintenance/set-up-document-management/email-integration-with-microsoft-outlook/about-the-vista-add-in-for-microsoft-outlook).

1. On the Ready to Install the Program screen, click Install to begin installation. The Installing Viewpoint Client screen displays until the installation is complete.

1. On the InstallShield Wizard Completed screen, click Finish to close the wizard. Note: In some cases the installer may have automatically installed required applications. If this has occurred, the system may prompt you to reboot the workstation.

You must now configure the client to connect to the
 server. For instructions see [Configure the Vista Client for LAN Connection](/en/vista/vista/on-premises-deployments/access-vista---local-area-network-lan/install-the-vista-client-application-on-a-workstation/configure-the-vista-client-for-lan-connection). If your organization provides internet
 access to your Vista server, see [Access Vista - VRL On-Premises](/en/vista/vista/on-premises-deployments/access-vista---vrl-on-premises).
