---
title: "Upgrade the Application Server | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/on-premises-deployments/installations/major-release-installation/vista-servers/upgrade-the-application-server"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/on-premises-deployments/installations/major-release-installation/vista-servers/upgrade-the-application-server"
---

# Upgrade the Application Server

When new versions of the Vista application are released, you must download and install the designated file(s) on your application server and your database server. If you are providing remote access to the client over the internet, you must also install the designated files on your reverse proxy server.
 If you are providing remote access to the client over the internet, you must also install the designated files on your reverse proxy server. For more information, see [Upgrade the Reverse Proxy Server](/en/vista/vista/on-premises-deployments/installations/major-release-installation/vista-servers/upgrade-the-reverse-proxy-server).
The following steps guide you through upgrading the Vista application server.
Note: You can also use these steps when installing the Vista application on a server for the first time.

1. Locate this version's executable file on your Vista application server. This file is located in the directory it was saved to when it was downloaded from the Viewpoint Customer Portal.

1. Right-click the install file and select Run As Administrator.It may take a few minutes for the system to prepare the InstallShield Wizard.

1. When the Vista Application Server InstallShield Wizard appears, click Next.The License Agreement screen displays.

1. Read the End User License Agreement and select the I accept... radio button.

1.  Click Next.The Setup Type screen displays.

1. Do one of the following:

- If you want your users to access the database via the LAN only, leave Default selected, click Next, and proceed to the next step.

- If you are also providing your users remote client internet access to the database using Remote Link, select Custom and click Next.Important: Select Custom only if you already installed and set up your remote proxy server for a previous version of Vista. The steps that follow are not suitable for a new installation, and assume you have already read and completed the prerequisite steps to install your remote proxy server. The steps you need to take before selecting Custom are described in [About Vista Remote Link (VRL) On-Premises](/en/vista/vista/on-premises-deployments/access-vista---vrl-on-premises/about-vista-remote-link-vrl-on-premises).

- In the Custom Setup screen that appears, click the down arrow next to Vista Remote Link features and select This feature, and all subfeatures, will be installed on local hard drive. Click Next.

1. In the Repository Destination Folder screen, verify that the default location is correct. Click Next to accept the location.Note: Changing the default location is not typical. However, if you need to change the location in this or any subsequent steps, click Change. The system displays the pertinent screen, where you can browse to and select a different location

1. In the Remote Services Destination Folder screen, verify that the default location is correct. Click Next to accept the location.

1. If your system detects that IIS is not installed, a prompt appears. Click Install IIS.

1. In the Vista Web Services Directory screen, verify that the default location is correct. Click Next to accept the location.

1. When the Database Server screen appears, do the following:

1. In the Database server that you are installing to field, enter the machine name of your Vista database server or click Browse to locate the server. Make sure this is the machine name and not the Fully Qualified Domain Name.

1. Select an option in the Connect using section:

- If you do not know the password for the sa login ID, and if your Windows login has sufficient permission, select the Windows authentication... radio button.

- If you select the Server authentication... radio button, the system defaults to the sa login ID. Enter the password for the sa login.

1. The Name of the database catalog field defaults to Viewpoint. Accept the default database, or click Browse to search for the database name.

1. Click Next.

1. If the system detects that your attachments database is on a different server than the server the database is on, the Attachments Database Server screen displays. Do the following:

1. Select the Server authentication... radio button.

1. If necessary, update the password for the sa login.

1. Click Next.

If your attachments database is on the same server as your database server, skip to the next step.

1. In the Identity and Data Services Hostname/Ports screen, the system places default values in the fields. Click Next.Note: In the unlikely event that an error message displays, click OK on the message. Enter the correct value in the port field in the Identity and Data Services Hostname/Ports screen, and click Next. The following is a description of each field.

- Fully Qualified Domain Name - The fully qualified domain name of the machine you are installing the application server on

- Identity Service HTTP port number - The port to which the Identity Service site is bound

- Identity Service SSL port number - The SSL port number to which the Identity Service site is bound. Used to secure communication between the Viewpoint Services and the Identity Service

- VRL Data HTTP port number - [VRL only] - The HTTP port to which the Data Access site is bound

- VRL Data NET.TCP port binding - [VRL only] - This is the NET.TCP port binding information for the Data Access site

- VRL Crystal HTTP port number - [VRL only] - The HTTP port to which the Crystal Access site is bound

- Enterprise ID - Your organization's unique ViewpointOne identifier. Do not change

1. In the Service Accounts screen, verify that the default account is correct. Click Next to accept the account.Important: Changing accounts is not recommended. If you must change accounts, see the instructions in [Modify Service Accounts](/en/vista/vista/on-premises-deployments/installations/major-release-installation/vista-servers/modify-service-accounts) and then resume with the next step.

1. If you selected Custom in the Setup Type screen to enable remote client internet access, and your company-specific URL isn't already mapped to the VRL service, the Remote Link URL screen appears at this point. Otherwise skip to the next step.

- If you know the base URL provided by your sysadmin, enter it now in the Remote Link base URL field and click Next.

- If you do not know your base URL, enter TBD. At a later stage, you can replace TBD with your company-specific URL provided by your sysadmin. Do not leave this field blank. Click Next.

1. If you are installing on a production server, review the Production or Test Install screen. Click Next.If you are installing on a test server, stop here and refer to [Install the Vista Application on a Test Server](/en/vista/vista/on-premises-deployments/installations/major-release-installation/vista-servers/install-the-vista-application-on-a-test-server) for the final steps.

1. Read the warning provided in the Production Environment screen. Click Continue when ready.

1. If you opted to change service accounts, an informational screen appears. Click Next.

1. In the Ready to Install the Program screen, click Install.The system begins the installation and displays the Installing Vista™ by Viewpoint Server Upgrade screen. The installation process may take several minutes to finish.

1. In the InstallShield Wizard Completed screen, click Finish.Note: In some cases, the wizard installs required applications. If this has occurred, you may receive and should follow any prompts to reboot the server before continuing.

1. If this is the first time you've installed the Vista application on this server, you must grant your domain users access to the Viewpoint Repository folder.

1. Locate the Viewpoint Repository folder. This folder is located in the directory it was saved to when it was downloaded from the Viewpoint Customer Portal.

1. Right click on the folder name and select Properties.

1. Select the Sharing tab, click Share, and grant 'Read Only' access to your domain users. Click Share.

1. Select the Security tab, click Advanced, and grant 'Read and Execute' access to your domain users.

1. Set Network Service to Full Control.Important: If your Vista application services are run by a domain service account, also make sure that account has full control to this folder as well.

1. If you are providing remote access to the Vista client using Vista Remote Link (VRL), do each of the following:

1. On your application server (or a server that the application server has access to), install the File System API. For instructions, see [Install the Vista File System API](/en/vista/vista/on-premises-deployments/installations/major-release-installation/vista-servers/install-the-vista-file-system-api).

1. On your reverse proxy server, install the Reverse Proxy Server upgrade. For instructions, see [Upgrade the Reverse Proxy Server](/en/vista/vista/on-premises-deployments/installations/major-release-installation/vista-servers/upgrade-the-reverse-proxy-server).Note: For instructions connecting the local client to your VRL server, see [Access Vista - VRL On-Premises](/en/vista/vista/on-premises-deployments/access-vista---vrl-on-premises).

1. Verify that Vista is running correctly. Refer to [Verify Upgrade Success](/en/vista/vista/on-premises-deployments/installations/major-release-installation/verify-upgrade-success). Note: If problems occur, [submit a Vista support case](https://support.viewpoint.com/s/submit-a-case).
