---
title: "Vista Remote Link (VRL) System Requirements | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/on-premises-deployments/access-vista---vrl-on-premises/about-vista-remote-link-vrl-on-premises/vista-remote-link-vrl-system-requirements"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/on-premises-deployments/access-vista---vrl-on-premises/about-vista-remote-link-vrl-on-premises/vista-remote-link-vrl-system-requirements"
---

# Vista Remote Link (VRL) System Requirements

If you are considering using a reverse proxy server to allow your Vista users to work anywhere there is a Wi-Fi connection, review these requirements. This information will help you as you prepare to provide access to the Vista client over the internet.
Before you enable remote connectivity for the Vista™ client using (VRL) there are a number of items to consider. The following provides a list of items that you must consider prior to taking advantage of VRL.

## Internet Performance Requirements

You must confirm that the network bandwidth and latency (ping) in each applicable remote location meets the minimum requirements for suitable performance. Viewpoint suggests using www.speedtest.net, a free web service that provides internet access performance metrics. Compare your test results from each location to the benchmarks below.
Network Capability LevelBenchmarks (Mb = megabits)
High - fully capable of supporting VRLLocations with these results should have minimal or no problems running the Vista client remotely.
Download> 10 Mbps
Latency0 - 20 ms
Upload> 1.5 Mbps
Marginal - capable but possible performance issuesLocations with these results may have some issues running the Vista client remotely.
Download7.5 - 10 Mbps
Latency21 - 40 ms
Upload1.0 - 1.5 Mbps
Low - NOT VRL capableLocations with these results are unable to run the Vista client remotely without significant performance issues.
Download< 7.5 Mbps
Latency> 40 ms
Upload< 1.0 Mbps

## Vista Reverse Proxy Server

You need a reverse proxy server to enable Vista Remote Link, which allows internet data transmission without compromising security. This is a server separate from the server(s) you are using to host your Vista application and database. In order for the remote Vista client to connect correctly, you must set up the reverse proxy server outside your domain, but within the DMZ.
Minimum specifications for the Vista Reverse Proxy Server are found in the Hardware/Software Requirements Guide at the [Viewpoint Customer Portal](https://support.viewpoint.com/s/vista).

## IIS Certificate

Purchase and set up an HTTPS certificate for your IIS server that is valid for the external URL that you are hosting. Map this certificate to the publicly accessible URL you are using for VRL.
Important: For best results, purchase your certificate from a certificate authority. Viewpoint does not recommend or support use of a self-assigned certificate.

## Crystal Reports Requirements

- Install a PDF viewer on each VRL-enabled workstation that is used to print reports. The client-side PDF viewer reduces maintenance on and increases serviceability of your server.

- Remote users who modify or create reports for you using Crystal Reports must set up VPN access to your Crystal Reports server.

## Firewall and Network Configuration

Open these ports as directed to allow VRL to manage data transmission among the application, database, reverse proxy servers, and your remote users without compromising security.
Your Server Configuration
Network Firewall Rules

Application Server
OPEN Ports from Reverse Proxy Server:
51519 | 51516 | 51515 | 808 | 88 | 443

Database Server
OPEN Port from Reverse Proxy Server: 80

Note: If your application and database are on a single server, open these ports on the combined server.

Once you have met these prerequisites, you can [Enable Vista Remote Link (VRL) Access](/en/vista/vista/on-premises-deployments/access-vista---vrl-on-premises/about-vista-remote-link-vrl-on-premises/enable-vista-remote-link-vrl-access).

Related concepts

- [About Vista Remote Link (VRL) On-Premises](/en/vista/vista/on-premises-deployments/access-vista---vrl-on-premises/about-vista-remote-link-vrl-on-premises)
