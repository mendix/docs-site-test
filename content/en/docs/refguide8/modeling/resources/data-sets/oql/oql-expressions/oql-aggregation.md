---
title: "OQL Aggregation"
url: /refguide8/oql-aggregation
parent: "oql-expressions"
tags: ["studio pro"]
---

{{% alert type="info" %}}
<img src="attachments/chinese-translation/china.png" style="display: inline-block; margin: 0" /> For the Simplified Chinese translation, click [中文译文](https://cdn.mendix.tencent-cloud.com/documentation/refguide8/oql-aggregation.pdf).
{{% /alert %}}

Aggregations perform specific calculations on the values of the retrieved column(s). The following aggregate functions are possible:

| AVG | average |
| --- | --- |
| COUNT | count |
| MAX | maximum |
| MIN | minimum |
| SUM | sum |

When you are using an aggregate expression in the SELECT clause, all expressions in the SELECT clause have to be either an aggregation OR part in the GROUP BY clause of the query.
