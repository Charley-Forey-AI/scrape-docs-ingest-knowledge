---
title: "Disable or Enable Audit Triggers | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/system-administration/administrator-utilities/create-a-test-company/disable-or-enable-audit-triggers"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/system-administration/administrator-utilities/create-a-test-company/disable-or-enable-audit-triggers"
---

# Disable or Enable Audit Triggers

Only under very specific circumstances should you disable audit triggers, and only very temporarily.
Disabling (and re-enabling) the audit triggers requires:

- access to Microsoft SQL Server Management Studio (SSMS)

- a SQL login that has read/write access to your database

- the contents of the *Disable All OmniAudit
 Triggers.sql* script and the *Enable All
 OmniAudit Triggers.sql* script, accessible by download from the [Viewpoint Customer Portal](https://support.viewpoint.com/s/)

Note: If your instance of Spectrum is hosted by Trimble Viewpoint, you can get read/write access by requesting the SQL Credential Authorization form from Support.

By design, changes to database tables are recorded. This recorded history enables audit activities should they become needed. Disabling the audit triggers prevents the system from logging any changes.During the process of a company data copy, for example, you might want to disable the recording of changes since there will be so many all at once, and will dramatically increase the size of the audit log tables, and subsequently your Spectrum database.
In any case, disabling audit triggers should always be followed up turning them back on. If left disabled, no history will be recorded, and any needed audit activities will not be possible.
To disable the audit triggers:

1. Using SQL Server Management Studio (SSMS), connect to the Spectrum database.

1. Select the Spectrum database and open a New Query window.

1. Choose one:

- To disable the triggers, copy the contents of the *Disable All OmniAudit Triggers.sql* script and paste it into the query window.

- To enable the triggers, copy the contents of the *Enable All OmniAudit Triggers.sql* script and paste it into the query window.

1. Select Execute.

The Results tab displays the Triggers which were affected. The value in the Disabled column indicates each trigger's current status:

- 1 - the trigger is disabled

- 0 - the trigger is active
