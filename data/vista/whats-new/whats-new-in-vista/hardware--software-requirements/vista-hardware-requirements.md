---
title: "Vista Hardware Requirements | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/whats-new/whats-new-in-vista/hardware--software-requirements/vista-hardware-requirements"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/whats-new/whats-new-in-vista/hardware--software-requirements/vista-hardware-requirements"
---

# Vista Hardware Requirements

This article details the hardware requirements for running Vista applications, accessing servers, connecting to the internet, and printing / scanning.

## Vista Application and Database Servers

Important: The server that Vista is installed on cannot act as server for any other applications. This includes but is not limited to mail, fax, or terminal servers. It cannot serve as the primary or backup domain controller. It must be installed on a member server.

Capacity ConsiderationsIf you have fewer than 10 concurrent users, a single server may host both the Vista application and database.
If you have 10 or more concurrent users, we strongly recommend separating the Vista application and database servers into unique machines (virtual or physical).
Minimum Server RequirementsIf you are running only Vista,
 your server must meet the following minimum requirements.
Minimum Server Requirements
CPU
Intel 2 GHz Xeon or later – Quad processor is recommended

Optional: Core Duo and/or x64

Memory
16GB RAM – Recommended for each machine when the application and database servers are on separate machines

32GB RAM – Recommended when the application and database servers are on the same machine

Disk
(Dual partition recommended)
O/S: 100 GB (C:) – At least 10 GB free for upgrades

Data: 350GB available SCSI disk, RAID 1 or RAID 5 – Recommended SSD read/write 500 MB/sec; minimum acceptable 15k RPM 320MB/sec

10 GB free disk storage required for upgrades on the O/S drive (typically C:)

High-capacity backup

## Vista Remote Link (VRL) Reverse Proxy Server

A separate server is required if you are providing remote client internet access to the Vista rich client. Traditional LAN access does not require this additional server. The reverse proxy server's role cannot be filled by either the application or database server. For more information, see [About Vista Remote Link (VRL) On-premises](/en/vista/vista/on-premises-deployments/access-vista---vrl-on-premises/about-vista-remote-link-vrl-on-premises).
Minimum Reverse Proxy Server Requirements
CPU
2 VCPUs

Memory
8GB RAM

Disk
O/S: 40 GB (C:)

Vista Remote Link reverse proxy server
VRL reverse proxy server must:

- Have direct TCP/IP connectivity to your Viewpoint Application/Database server

- Be outside the domain

- Be inside the DMZ

## Client Workstations

Minimum Client Workstation Requirements
CPU
Pentium or Intel Core Duo Processors: 2Ghz or greater

Memory
8GB RAM

Resolution
Recommended 1024x768 XGA video

Display Configuration
100% (Windows 10 and later)

## Network

All deployment methods require internet connectivity.
VRL Connections (on-premises or cloud)Both VRL on-premises and VRL Cloud client connections should adhere to these client connection minimums:
Ideal
Acceptable
Unsupported

Bandwidth, download
≥10 Mbps
≥7.5 Mbps
<7.5 Mbps

Bandwidth, upload
≥1.5 Mbps
≥1.0 Mbps
<1.0 Mbps

Latency
≤30 ms
≤60 ms
>60 ms

Packet Loss
≤0.5%
≤1.5%
>1.5%

LAN ConnectionAll clients networked to server with TCP/IP protocols: minimum 100 Mbit required, 1 gigabit recommended.

## Printing and Scanning

Printing and Scanning
 Requirements
Printing

- Supported printer connections:
 networked, local, remote, and Citrix.

- HP Laser Jet printer family is
 recommended.

- Printer resolution, fonts, drivers,
 and margin capability may affect output.

- Citrix printing sensitivities may
 require additional testing with various printer
 drivers.

- Troy printers MICR fonts are not
 compatible with Crystal Reports .NET – other 3rd-party
 fonts must be used.

- The majority of testing is done with
 universal print drivers.

- *Not supported:* Dot matrix
 printers are not supported.

ScanningScanners must be TWAIN or WIA compliant. Note: You must be on
 Vista version 2024 R1.03 or higher
 to use WIA drivers. Previous Vista
 versions do not support WIA drivers.
