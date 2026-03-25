---
title: "Interaction Between Group and User Level Security Settings | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/viewpoint-administration/application-security/user-security/interaction-between-group-and-user-level-security-settings"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/viewpoint-administration/application-security/user-security/interaction-between-group-and-user-level-security-settings"
---

# Interaction Between Group and User Level Security Settings

Security groups apply the same security settings to all associated users.
However, some users may require specific security settings that no one group provides. In this case, you can keep the user associated with the group, but override group security settings at the individual user level in VA security forms.
Generally, the user-level settings take precedence over the group settings. However, there are some exceptions to note:

- Where the user’s access level or permission setting is set to None, the group setting takes precedence.

- If both user and group are set to None for a form, the user cannot access the form. In forms where there are attachments, and both user and group access settings are set to None, the user cannot add, edit, or delete attachments.

- If a user belongs to more than one group, the group with the least restrictive setting takes precedence over the other group's settings.

- A security group cannot be assigned a setting of Denied.
