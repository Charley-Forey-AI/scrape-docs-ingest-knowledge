---
title: "Vista Servers | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/on-premises-deployments/installations/service-pack-installation/vista-servers"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/on-premises-deployments/installations/service-pack-installation/vista-servers"
---

# Vista Servers

This section of the Vista installation instructions assists you with the upgrade
 process for the Vistaapplication and database servers.

During installation, the following important components are updated:

- Viewpoint Repository - This contains all Vista program and report files.

- Database Upgrade Scripts - The wizard runs these scripts to update your Viewpoint database to the applicable version.

- Viewpoint Remote Service and Viewpoint Service - The system uses these applications to keep the client software up to date.

- Identity Service (IIS) - Authenticates users logging in to Vista.

- Config Service - Stores and retrieves server configuration settings.

- VRLData (VRL only) - Pulls data from the Vista database to each local client, since each workstation doesn't have a direct database connection.

- VRLCrystal (VRL only) - Renders Crystal reports on the server, since each workstation doesn't have a direct database connection.

For the purposes of this document, we reference the database and application servers as separate servers, but depending on how you initially set up your specific instance of Vista, you may have the database and application loaded on a single server. If this is the case, run both installers on the same server.
If you are providing remote access to the Vista client using Vista Remote Link, your reverse proxy server is always separate from the application/database server(s). For more information, see [About Vista Remote Link (VRL) On-Premises](/en/vista/vista/on-premises-deployments/access-vista---vrl-on-premises/about-vista-remote-link-vrl-on-premises) in the online help.
