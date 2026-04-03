---
title: "Expand Phase Code for Job | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/utilities-overview/expand-phase-code-for-job"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/utilities-overview/expand-phase-code-for-job"
---

# Expand Phase Code for Job

When you first select this screen, the Code
 Change Warning window displays. This window reminds you that any changes you
 make in this utility screen will affect the entire Spectrum system.
After the warning closes, the Expand Phase Code for
 Job screen displays. Use this screen to enlarge the phase coding scheme for
 a job even if it already has costs applied to it. This screen allows you to expand the
 phase code mask up to a maximum of 20 characters (including dashes) for any job that has
 already been set up. However, phase codes cannot be shortened.
After entering the job number and the new phase mask for this job, the system will proceed to append additional zeros to the existing phase codes associated with this job throughout Spectrum.
For example: If a job with phase 12-3456 was expanded by three digits, the new phase would display as 12-3456-000 after this update was performed. Likewise, if a job with phase mask XX was changed to XXXX-XXXX, six trailing zeros would be appended to all the existing phases.
In addition, if pay groups are used, the system will optionally add zeros to phases specified in Pay Group File Maintenance when the pay group code exactly matches this job code. Caution should be exercised when performing this function.
The update includes unlimited phase notes. Phase notes will be removed when the last cost type for a given phase is deleted using the [Delete Unused Phases](/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/utilities-overview/delete-unused-phases) utility.
Important: This update should never be performed while
 others are in Spectrum.
