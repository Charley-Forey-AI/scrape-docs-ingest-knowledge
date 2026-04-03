---
title: "Job Labor Billing Rates | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/list-of-web-services/time--materials-services/job-labor-billing-rates"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/list-of-web-services/time--materials-services/job-labor-billing-rates"
---

# Job Labor Billing Rates

Use this service to add or edit job-specific labor billing rates.

## Connection Information

URL = https://<SPECTRUM-SERVER>:8482/TimeMaterial/AddJobLaborTM
Authentication: [Basic Authentication](/en/spectrum/spectrum/api-web-services/authentication/basic-authentication), [Enhanced Authentication](/en/spectrum/spectrum/api-web-services/authentication/enhanced-authentication)
Supported methods: POST
Supported formats: JSON

## Sample JSON Body

```
`{
 "timeMaterialJobLabors": [{
 "Company_Code": "2nd",
 "Job_Number": "1A",
 "Billing_Code": "JOBLABOR",
 "Description": "TESTJOBLABOR",
 "Markup_Type":"P",
 "Reg_Bill_1":"1",
 "Reg_Bill_2":"10",
 "Reg_Bill_3":"100",
 "Reg_Bill_4":"1000",
 "Reg_Bill_5":"100000",
 "OT_Bill_1":"20",
 "OT_Bill_2":"20",
 "OT_Bill_3":"20",
 "OT_Bill_4":"20",
 "OT_Bill_5":"20",
 "DT_Bill_1":"30",
 "DT_Bill_2":"30",
 "DT_Bill_3":"30",
 "DT_Bill_4":"30",
 "DT_Bill_5":"30",
 "Markup_1":"5",
 "Markup_2":"10",
 "Markup_3":"25",
 "Markup_4":"29",
 "Markup_5":"35"
 }]
} `
```

## Underlying File Maintenance

- System Administration > Installation > Time + Material > Job Labor Billing Rates
