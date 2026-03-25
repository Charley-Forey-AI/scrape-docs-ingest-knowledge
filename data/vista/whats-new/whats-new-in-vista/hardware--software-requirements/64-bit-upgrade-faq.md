---
title: "64-Bit Upgrade FAQ | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/whats-new/whats-new-in-vista/hardware--software-requirements/64-bit-upgrade-faq"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/whats-new/whats-new-in-vista/hardware--software-requirements/64-bit-upgrade-faq"
---

# 64-Bit Upgrade FAQ

Learn about the upcoming changes associated with upgrading the Vista client, third-party applications, and Microsoft Office to 64-bit. These changes will be completed over the course of 2025.

## What is changing?

Trimble Viewpoint is transitioning to a 64-bit Vista client. Other components in your Vista setup must match this bitness. You must have the following:

- 64-bit version of the Vista client

- 64-bit third-party applications (such as scanning and attachment plugins for the Vista client)

- 64-bit version of Microsoft Office (if you have any Microsoft integrations)

In other words, 32-bit versions of any of the above components must be upgraded to 64-bit or they may not work correctly.

## When is this happening?

All 64-bit upgrades should be completed by the end of 2025.
After the Vista 2025 R2 release, the 32-bit Vista client will no longer be recommended.

## Who is impacted by this change?

All Vista customers—including cloud-hosted and on-premises—will be required to meet 64-bit compatibility for all aspects of their Vista setup in order to use Vista 2025 R2 and later versions.

## What actions do I need to take?

The actions you need to take depend on your Vista deployment method.
For cloud-hosted customers:*For VRL cloud-hosted customers only:*
Make sure your Vista setup meets compatibility requirements:

- Update any third-party applications to have 64-bit compatibility.

- Test any third-party integrations to make sure they still function in 64-bit.

- Update Microsoft Office to 64-bit (if you have any Microsoft integrations).

After completing these updates, you will be ready to install the 64-bit Vista client. You should transition to 64-bit as soon as possible to determine any potential issues with your setup and resolve them before the 32-bit client is no longer available after the 2025 R2 release.
*For all other cloud-hosted customers:*
We will update your Vista client and Microsoft Office applications to 64-bit as part of the Azure Remote Desktop Windows 11 migration. This migration is currently underway and will be completed by the end of 2025.
You should do the following before your migration date to make sure your Vista setup will meet compatibility requirements:

- Update any third-party applications to have 64-bit compatibility.

- Test any third-party integrations to make sure these still function in 64-bit.

See the [Azure Remote Desktop Windows 11 Migration FAQ](https://apim.viewpointplatform.com/help/v1/contents/urn:contentId:vista_60064) for more information about the migration and how you can prepare.
For on-premises customers:Make sure your Vista setup meets compatibility requirements:

- Update any third-party applications to have 64-bit compatibility.

- Test any third-party integrations to make sure these still function in 64-bit.

- Update Microsoft Office to 64-bit (if you have any Microsoft integrations).

After completing these updates, you will be ready to install the 64-bit Vista client. You should transition to 64-bit as soon as possible to determine any potential issues with your setup and resolve them before the 32-bit client is no longer available after the 2025 R2 release.

## How can I tell if my Vista client is 32-bit or 64-bit?

To determine if your Vista client is 32-bit or 64-bit, do the
 following:

1. Open Vista.

1. Open the Task Manager on your computer.

1. In the Apps section of the Task Manager, see that the
 Vista client is running. It
 will show as Launcher
 with the Vista icon.32-bitIf your Vista
 client is 32-bit, the application will show as Launcher (32
 bit).
64-bitIf your Vista
 client is 64-bit, the application will show simply as Launcher.

## Is this upgrade required?

To be able to use Vista 2025 R2 and later, yes, the upgrade to a 64-bit architecture is required.

## Why are we doing this?

The upgrade to 64-bit is part of a modernization and maintenance optimization initiative for Vista.

## Can I test the 64-bit version of Vista beforehand?

Yes. We encourage you to download the 64-bit Vista client (available now from the [Viewpoint Customer Portal](https://support.viewpoint.com/s/vista)) and test your system and third-party integrations as early as possible.
Note: If you are a cloud-hosted customer using Vista with 32-bit Microsoft Office integrations, while testing the 64-bit client, you may experience compatibility issues affecting functionalities such as the Microsoft Outlook integration and PM Create and Send.

## Will I have to update each Vista client on each workstation?

Yes. If you have the 32-bit version of Vista installed, you need to run the client installer on each workstation to upgrade to the 64-bit Vista client.
