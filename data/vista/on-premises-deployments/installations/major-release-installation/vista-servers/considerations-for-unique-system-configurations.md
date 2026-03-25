---
title: "Considerations for Unique System Configurations | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/on-premises-deployments/installations/major-release-installation/vista-servers/considerations-for-unique-system-configurations"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/on-premises-deployments/installations/major-release-installation/vista-servers/considerations-for-unique-system-configurations"
---

# Considerations for Unique System Configurations

For users with unique system configurations, there are additional items should be considered before installation.
Important:Vista does not support multiple Viewpoint databases in a single SQL instance. Do not install a test database to your production instance - it will cause your production instance to fail.

- If you are running in a Clustered Server environment, you must run the Vista update on the primary application Server (as described in the installation instructions). You must then failover to the secondary server and run the Vista update again.

- If you are running replication, you must turn off database replication before performing the upgrade process for the database server. After the update, you must establish a fresh copy of the Vista database and restore this onto the replication server. Make sure to flush the transaction logs and then turn database replication back on.

- Viewpoint service accounts will be added and deleted during the installation process, impacting the targeted environment.
