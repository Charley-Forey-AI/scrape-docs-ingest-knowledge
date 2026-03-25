---
title: "Reports Features | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2021-releases/whats-new-in-vista-2021-r2/system-tools/reports-features"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2021-releases/whats-new-in-vista-2021-r2/system-tools/reports-features"
---

# Reports Features

Vista 2021 R2 delivers on user-requested Reports enhancements, fixes, and other improvements

## More Secure Report Layout Generation

For security reasons, when you update a report design (by clicking Update Design on the Info tab), the report layout generation process no longer includes the report location. This reduces the possibility of exposing potentially sensitive information.

## Instantly Sync the SSRS Server with All Vista Security Settings

 You can now quickly and easily sync all current Vista report security settings to the SSRS report server. Learn more at [Sync Vista Report Security to the SSRS Server](/en/vista/vista/system-tools/reports/ssrs-overview-and-security-considerations/sync-vista-report-security-to-the-ssrs-server).

## Fewer Report Time-outs and Dropped Connections

VRL Cloud users can now see their relative position in a new report queue screen that appears when previewing both standard and custom Vista reports.
If your organization is experiencing dropped connections and opts to enable the queue (contact Support), the maximum number of report preview windows that can be open at any one time is 50. The Crystal Runtime maximum is 75, which reserves 25 for batch reporting availability.
If the company-wide report preview count is below 50, your report begins processing immediately and displays the preview when processing is complete.
If the preview count is above 50, your report enters the queue and the preview screen displays your queue position. Without any further action, once your position in the queue reaches 0, your report begins processing and displays the preview as soon as processing is complete.
When you close your preview, the next report in the queue begins processing. For as long as you keep your preview open, that license is occupied.

## Check Issue Status

To see a list of defects fixed in this version, go to the [Track Cases/Issues page](https://support.viewpoint.com/s/browse-cases-and-issues) of the Viewpoint Customer Portal. Use the filter options to select your product and module. In the Fixed in Version field, select this version, then select Apply Filters.
