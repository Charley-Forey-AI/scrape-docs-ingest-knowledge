---
title: "About VRL Cloud | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/cloud-deployment/about-vrl-cloud"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/cloud-deployment/about-vrl-cloud"
---

# About VRL Cloud

Vista Remote Link (VRL) Cloud is a method for connecting to the Vista application in Trimble Viewpoint's cloud.
Trimble Viewpoint hosts your Vista application and database servers in Microsoft Azure data centers, instead of you having to maintain these servers on premises.
Each user workstation has a locally installed Vista rich client application which communicates with Viewpoint's cloud over the Internet, using HTTPS.
For a video guided tour through some of the differences between using a local Vista client to using a cloud connection, follow these steps:

1. [Go to the video](https://academy.viewpoint.com/learn/course/external/view/elearning/3557/vista-cloud-transformation-guided-tour) in the Trimble Construction Academy.

1. Select Enroll.

1. Sign in using your Trimble Construction Academy credentials.

## Simpler User Experience

VRL access results in a simplified day-to-day user experience compared to RDP.

## File-sharing Security

 Since it is occurring over the internet, file sharing that occurs in Vista must necessarily be made more secure. Vista offers a way to restrict the types of files that can be uploaded within your network. See [About the File Extension White List Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/maintenance/about-the-file-extension-white-list-form).

## Network File Storage Requirements

Because Trimble Viewpoint hosts your database and application servers, file management and storage methods are different than when your users have immediate access to your company servers (such as with a LAN deployment). Specifically, any process that retrieves files from the database server is affected.
If you've come from a LAN deployment to a VRL cloud deployment, the differences in appearance and function of these forms may be relevant to you:

- IM Auto Import Profile Setup - see [About Importing Files Automatically](/en/vista/vista/administration/imports/setup-and-maintenance/about-importing-files-automatically).

- PM Create & Send Locations - see [PM Create & Send Locations Form](/en/vista/vista/project-management/create-and-send/pm-create--send-locations-form).

- RP Report Locations - see [Set Report Locations - VRL](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/set-report-locations/set-report-locations---vrl).

## VPN Connection is included with VRL Cloud

As a standard part of your cloud deployment, Trimble Viewpoint provides a VPN connection from your office so that third-party applications which are not hosted by Viewpoint within the environment can access your Vista server in our Cloud.
The Vista client connects without a VPN.
For further details, see [About VPN Use for VRL Cloud Users](/en/vista/vista/cloud-deployment/about-vrl-cloud/about-vpn-use-for-vrl-cloud-users).

## Internet Performance Requirements

Successful VRL Cloud operations are dependent in part upon your organization's network performance. While your sales representative can walk you through a more comprehensive evaluation, these performance standards are provided for your convenience.
Free web services are available to you that provide internet access performance metrics. Compare your test results from your location (where Vista will be used, and not from an off-site location or from a hot spot) to the benchmarks below.

- Test bandwidth using [www.speedtest.net](https://www.speedtest.net/).

- Test packet loss and latency using [www.azurespeed.com](https://www.azurespeed.com).

- If you are a U.S.-based company, check all U.S. and Canadian regions.

- If you are an Australia-based company, check only Australian regions.Note: We currently have data centers in multiple locations, but not all Azure locations in each region. Your data is situated as close to your place of business as geographically possible.

Table 1. Performance Metrics GuideIdealAcceptableUnsupported
Packet Loss<0.5%0.5-1.5%>1.5%
Latency<30 ms31-60 ms>60 ms
BandwidthDownload>10 Mbps7.5-10 Mbps<7.5 Mbps
Upload>1.5 Mbps1.0-1.5 Mbps<1.0 Mbps

Related concepts

- [VRL Cloud User Guide](/en/vista/vista/cloud-deployment/about-vrl-cloud/vrl-cloud-user-guide)
