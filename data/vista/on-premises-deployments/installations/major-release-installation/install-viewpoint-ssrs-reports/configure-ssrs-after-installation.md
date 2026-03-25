---
title: "Configure SSRS After Installation | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/on-premises-deployments/installations/major-release-installation/install-viewpoint-ssrs-reports/configure-ssrs-after-installation"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/on-premises-deployments/installations/major-release-installation/install-viewpoint-ssrs-reports/configure-ssrs-after-installation"
---

# Configure SSRS After Installation

If you have run the Viewpoint SSRS Reports installer, you should configure SSRS.
The following guides you through the steps you need to take to configure SSRS. Click the links in each step for more detail.

1. [Set up form security on Admin Users in Vista](/en/vista/vista/on-premises-deployments/installations/major-release-installation/install-viewpoint-ssrs-reports/configure-ssrs-after-installation/set-up-form-security-on-admin-users-in-vista).

1. [Set up report security in Vista](/en/vista/vista/on-premises-deployments/installations/major-release-installation/install-viewpoint-ssrs-reports/configure-ssrs-after-installation/set-up-report-security-in-the-ssrs-report-manager).The Viewpoint SSRS Reports installer does not apply security on any SSRS reports. Even If if you were using SSRS reports before the upgrade, you should set up security on your SSRS reports again using Vista.

1. [Set up report security in the SSRS Report Manager](/en/vista/vista/on-premises-deployments/installations/major-release-installation/install-viewpoint-ssrs-reports/configure-ssrs-after-installation/set-up-report-security-in-the-ssrs-report-manager).This applies only if you have users who access SSRS reports using only the Report Manager.

1. [Verify the custom report locations are correct](/en/vista/vista/on-premises-deployments/installations/major-release-installation/install-viewpoint-ssrs-reports/configure-ssrs-after-installation/verify-custom-report-locations-are-correct).

1. [Verify that the data source on custom reports is correct](/en/vista/vista/on-premises-deployments/installations/major-release-installation/install-viewpoint-ssrs-reports/configure-ssrs-after-installation/verify-data-sources-are-set-up-correctly).

1. [Set up any remaining custom reports](/en/vista/vista/on-premises-deployments/installations/major-release-installation/install-viewpoint-ssrs-reports/configure-ssrs-after-installation/set-up-remaining-custom-reports).Note: If you are not using custom security and want the security you set up in Vista to sync with the SSRS Report Server, you must:

- Set up the account running the Viewpoint Remote Service as an administrative account on the SSRS Report Manager Site Settings and;

- Assign this account a Content Manager role for each individual report in the SSRS Report Manager.

If the Viewpoint Remote Service is running as a "NT Authority\Network Service", and the SSRS Report Server does not reside on the same machine, the account name should be in this format: <Domain>\<MachineName>$.
