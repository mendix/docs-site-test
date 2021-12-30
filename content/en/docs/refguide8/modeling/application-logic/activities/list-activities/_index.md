---
title: "List Activities"
url: /refguide8/list-activities
parent: "activities"
menu_order: 20
tags: ["studio pro", "microflow", "list"]
---

{{% alert type="info" %}}
<img src="attachments/chinese-translation/china.png" style="display: inline-block; margin: 0" /> For the Simplified Chinese translation, click [中文译文](https://cdn.mendix.tencent-cloud.com/documentation/refguide8/list-activities.pdf).
{{% /alert %}}

## 1 Introduction

When working with the Mendix Platform, you can use microflows to manipulate not only single objects but whole lists of entities with a single activity.

Additional activities which work on lists, [commit object(s)](committing-objects), [delete object(s)](deleting-objects), and [retrieve](retrieve), are in the [Object Activities](object-activities) section of the toolbox. You can also [loop](loop) through a list to perform activities on the individual objects.

The activities described in this document are in the **List Activities** section of the **Toolbox**:

{{% image_container width="40%" %}}
![list activities toolbox](/attachments/refguide8/modeling/application-logic/activities/list-activities/list-activities-toolbox.png)
{{% /image_container %}}

The following are the list activities you can use in your microflow or nanoflow:

* [Aggregate List](aggregate-list) – calculates aggregated values over a list
* [Change List](change-list) – adds objects to, and removes objects from a list
* [Create List](create-list) – creates an empty list
* [List Operation](list-operation) – performs actions on a list and, if the result is a list, returns a new list containing the result

## 2 Read More

* [Activities](activities)
