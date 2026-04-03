---
title: "Setting up Spectrum for Remote Users | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/getting-started/general-reference/setting-up-spectrum-for-remote-users"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/getting-started/general-reference/setting-up-spectrum-for-remote-users"
---

# Setting up Spectrum for Remote Users

There are two primary options to access Spectrum remotely:

- Access via a corporate VPN

- Direct access via the Internet

## VPN Access

Accessing Spectrum via a corporate VPN is the simplest and most secure solution if you already have VPN access to your corporate network. You simply need to connect to your corporate network using your VPN software, and then launch Spectrum in your browser as you normally would from within your office.

## Direct Access

If you set up direct access to Spectrum from the Internet, make sure you keep your Spectrum server updated with the latest Spectrum and Windows updates to ensure the highest level of security possible.
Accessing Spectrum directly from the Internet is a two-step process.

- Configure your firewall to allow access to the Spectrum server from the Internet

- Create an external DNS "A" record for your Spectrum URL

The most common way to allow external access to Spectrum is to configure your firewall to forward the appropriate traffic to your Spectrum server (that is, port forwarding). The default ports used by Spectrum, and the ports needing to be forwarded, are 80/TCP (HTTP) and 443/TCP (HTTPS) (Port 80 redirects to Port 443). If you need external access to SDX, Port 8482/TCP will also have to be forwarded.
DNS allows you to use a user-friendly URL in place of an IP address when connecting to a resource (for example, spectrum.xyz.com instead of 10.1.1.10). Creating an external DNS "A" record for your Spectrum URL will allow you to use the URL from outside your corporate network. This is required because Spectrum uses a secure connection (HTTPS) and the address used in your browser must match the URL on the SSL certificate used by Spectrum.
To create an external DNS "A" record, you will need to contact your domain registrar (the company that issued your domain). Most domain registrars have online utilities that will allow you to create DNS records. In the utility, you will need to create an "A" record where the host is your Spectrum URL (for example, spectrum.xyz.com) and the value is your external "public" IP address. This will direct traffic going to your Spectrum URL to your external "public" IP address where your firewall will receive and forward it to your Spectrum server.
Note: It may take hours or even days to propagate DNS changes throughout the
 Internet.
