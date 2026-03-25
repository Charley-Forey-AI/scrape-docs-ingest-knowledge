---
title: "Viewpoint Administration Features | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2022-releases/whats-new-in-vista-2022-r2/administration/viewpoint-administration-features"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2022-releases/whats-new-in-vista-2022-r2/administration/viewpoint-administration-features"
---

# Viewpoint Administration Features

Vista 2022 R2 delivers on user-requested Viewpoint Administration enhancements, fixes, and other improvements.

## Vista Prevents Entering Duplicate Emails

Since the email address is an element of the Trimble ID login credentials, it must not be used on any other Vista profile. Vista helps you by alerting you if you've entered an email address which is already in use by any other Vista user record.Note: This feature does not assess, enforce uniqueness upon, or provide alerts about existing email addresses. Any duplicates which happen to exist are permitted to remain. Enforcement is applied only upon attempting to save a new or changed email address which is already in use.

## MS Outlook Add-in Compatible with Trimble ID

Vista users who are set up to log in using single sign-on and Trimble ID can now rely on those same credentials when setting up Vista's Microsoft Outlook Add-in, or when authenticating an instance which is already set up.
All existing authentication methods remain, so if your organization does not yet use single sign-on with Trimble ID, your use of the Add-in is unaffected.

## Permission to Use VRL now Automatic

Since connecting workstations to the Vista database using Viewpoint Remote Link (VRL) is the preferred connection method, we've removed a potential obstacle to its use - the requirement by a System Admin to select the checkbox in the VA User Profile form.
The Allow Vista Remote Link login checkbox in the VA User Profile form is removed in this version, with the effect being all user profiles are allowed by default.Important: If you have custom reports or procedures which rely on or refer to this field, you will need to make any necessary changes and test that your custom work(s) remain functional.
