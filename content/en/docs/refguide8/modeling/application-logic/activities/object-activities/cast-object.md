---
title: "Cast Object"
url: /refguide8/cast-object/
parent: "object-activities"
weight: 10
tags: ["studio pro"]
---

{{% alert color="info" %}}
<img src="/attachments/china.png" style="display: inline-block; margin: 0" /> For the Simplified Chinese translation, click [中文译文](https://cdn.mendix.tencent-cloud.com/documentation/refguide8/cast-object.pdf).
{{% /alert %}}

{{% alert color="warning" %}}
This activity can only be used in **Microflows**.
{{% /alert %}}

## 1 Introduction

The cast object activity is used in a microflow after an [object type decision](/refguide8/object-type-decision/) to change the type of object from the generalized object type to the specialized object type of the path out of the object type decision.

To read more about specialization and generalization, see [Entities](/refguide8/entities/).

## 2 Properties

An example of cast object properties is represented in the image below:

![cast object properties](/attachments/refguide8/modeling/application-logic/activities/object-activities/cast-object/cast-properties.png)

There are two sets of properties for this activity, those in the dialog box on the left, and those in the properties pane on the right.

The cast object properties pane consists of the following sections:

* [Action](#action)
* [Common](#common)

## 3 Action Section{#action}

The **Action** section of the properties pane shows the action associated with this activity.

You can open a dialog box to configure this action by clicking the ellipsis (**…**) next to the action.

You can also open the dialog box by double-clicking the activity in the microflow or right-clicking the activity and selecting **Properties**.

### 3.1 Object Name

This is the name for the result of the cast. It can be used by all activities that follow this activity.

## 4 Common Section{#common}

{{% snippet file="/static/_includes/refguide8/microflow-common-section-link.md" %}}

## 5 Example

For example, there are three specializations of the **Question** object. Only an object of the specialized type **MultipleChoiceQuestion** needs to have some special actions performed on it. These will be done in a sub-microflow which has as the input type **MultipleChoiceQuestion**. Since an object of the type **Question** cannot get passed to the sub-microflow, the object first needs to be cast to the object type **MultipleChoiceQuestion**.

![Example of cast in a microflow](/attachments/refguide8/modeling/application-logic/activities/object-activities/cast-object/cast-example.png)