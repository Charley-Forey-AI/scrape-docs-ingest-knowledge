---
title: "Prepare for installation on the reverse proxy server | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/access-vista---vrl-on-premises/about-vista-remote-link-vrl-on-premises/enable-vista-remote-link-vrl-access/prepare-for-installation-on-the-reverse-proxy-server"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/access-vista---vrl-on-premises/about-vista-remote-link-vrl-on-premises/enable-vista-remote-link-vrl-access/prepare-for-installation-on-the-reverse-proxy-server"
---

# Prepare for installation on the reverse proxy server

Take these preparatory steps before installing Vista on the
 reverse proxy server.
The steps listed on this page are part of the process outlined in [Enable Vista Remote Link (VRL) Access](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/access-vista---vrl-on-premises/about-vista-remote-link-vrl-on-premises/enable-vista-remote-link-vrl-access).

- Review [Vista Remote Link (VRL) System Requirements](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/access-vista---vrl-on-premises/about-vista-remote-link-vrl-on-premises/vista-remote-link-vrl-system-requirements).

- Run the Vista application installer on the application server according
 to the step-by-step instructions in the Upgrading the Application Server section of the
 installation manual. Pay particular attention to the steps that are unique to VRL
 setup.

Important: If you have already installed Vista on your application server using the 'Default' setting, you need to uninstall and reinstall it using the 'Custom' setting in order for VRL to function. Do not use the Change function in the installer.



- Install any needed application or database server operating system updates.
 For minimum requirements, see the Vista Software Requirements section of the installation
 manual.

- Create a local firewall rule to allow TCP traffic through port 443 to the
 internet. This should be mapped to the publicly accessible URL you are using for
 VRL.

- Enter the FQDN and the application server short name in the %windir%\system32\drivers\etc\hosts file for the Vista Application Server system
 and, if different, the Vista Database System too. For example:

- Format: <IP> <Fully Qualified Domain Name>
 <simpleName>

- Example: 172.25.0.197 VSQAVISTAWA07.coaxis.net
 VSQAVISTAWA07

- Install .NET 4.5/HTTP Activation Windows feature; you will likely need the
 Windows Installation media available to do this.

- Install .NET 3.x NON/HTTP Activation Windows feature.

- Ensure you have the FQDN for both the application server and reverse proxy
 server.
