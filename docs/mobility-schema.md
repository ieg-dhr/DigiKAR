---
authors:
  - Jakob Listabarth (IfL Leipzig)
  - Monika Barget (IEG Mainz, FASoS Maastricht)
---

# Schema mobility data

The different analytical lenses of the mobility data, follow a common data schema.
This page describes this schema in detail.

The basis of every datum is an event, which is related to a person and a place.
Hence, we group the columns the following categories, and prefix them accordingly:

- related to the event itself, prefix: `event_`
- related to the primary person of that event, prefix: `person_`
- related to place the event is assigned to: `place_`

## Event related columns (prefix: `event_`)

<SchemaEntry
name="event_id"
description="Unique identifier for the event."
type="string"
:examples="['stud2715', '123456']">

Every datum in the DigiKAR project gets a _unique_ identifier for the event.
This identifiers are prefixed.
For example, `stud2715` is a unique identifier for a student event.

:::warning
Is the prefix actually necessary? If so do we still need the `event_analytical_lens`?
:::

</SchemaEntry>

<SchemaEntry
name="event_date"
type="string"
description="Used if exact event date is known, mostly in YYYY-DD-MM format."
:examples="['1684-08-03', '1732', '1737-12-10']">

:::info
Explain here why this is a simple string, and not consistent
:::
</SchemaEntry>

<SchemaEntry
name="event_date_start"
type="string"
description="Used if the start point of an event is known"
:examples="[]">
</SchemaEntry>

<SchemaEntry
name="event_date_end"
type="string"
description="Used if the end point of an event is known"
:examples="[]">
</SchemaEntry>

<SchemaEntry
name="event_date_before"
type="string"
description="Used if it is known that the event happened before a certain date"
:examples="[]">
</SchemaEntry>

<SchemaEntry
name="event_date_after"
type="string"
description="Used if it is known that the event happened after a certain date"
:examples="[]">
</SchemaEntry>

<SchemaEntry
name="event_type"
type="string"
:examples="[]">
</SchemaEntry>

<SchemaEntry
name="event_value"
type="string"
description="flexible, research-dependent categorisation of events to foster a user-friendly visualisation"
:examples="[]">
</SchemaEntry>

<SchemaEntry
name="event_editorial_comment"
type="string"
description="Any editorial comments on the event"
:examples="[]">
</SchemaEntry>

<SchemaEntry
name="event_histogriographical_comment"
type="string"
description="Any histogriographical comments on the event"
:examples="[]">
</SchemaEntry>

<SchemaEntry
name="event_source"
type="string"
description="The source of the event"
:examples="[]">
</SchemaEntry>

<SchemaEntry
name="event_source_comment"
type="string"
:examples="[]">
</SchemaEntry>

<SchemaEntry
name="event_source_criticism"
type="string"
:examples="[]">
</SchemaEntry>

<SchemaEntry
name="event_source_quotations"
type="string"
:examples="[]">
</SchemaEntry>

<SchemaEntry
name="event_related_persons"
type="string"
:examples="[]">
</SchemaEntry>

<SchemaEntry
name="event_analytical_lens"
type="string"
description="Specifies from which analytical lense this event originates."
:examples="['Statecalendar Jahns', 'Matriculations Mainz']">

The "analytical lens" is a project-defined focus and reflects the research context in which the data were initially collected.

To get a better idea of the different types of ecclesiastical, academic, and political agents active in Electoral Mainz between the 16th and 18th centuries, our historians have manually collected biographic data relating to the Mainz government in the Eastern German exclave of Erfurt, Mainz officials represented at imperial institutions such as Reichstag (Imperial Diet), Reichshofrat and Reichskammergericht, and the organisation of the electoral court in Mainz itself. In addition, we have used XML data (harvested via API) and OCR technology to semi-automatically gather information on professors and students active at the early modern university of Mainz.

</SchemaEntry>

## Person related columns (prefix: `person_`)

<SchemaEntry
name="person_id"
:examples="[]">
</SchemaEntry>

<SchemaEntry
name="person_name"
:examples="[]">
</SchemaEntry>

<SchemaEntry
name="person_name_variants"
:examples="[]">
</SchemaEntry>

<SchemaEntry
name="person_function"
:examples="[]">
</SchemaEntry>

<SchemaEntry
name="person_title"
:examples="[]">
</SchemaEntry>

## Place related columns (prefix: `place_`)

<SchemaEntry
name="place_geonames_id"
:examples="[]">
</SchemaEntry>

<SchemaEntry
name="place_geonames_latitude"
type="number"
:examples="[]">
</SchemaEntry>

<SchemaEntry
name="place_geonames_longitude"
type="number"
:examples="[]">
</SchemaEntry>

<SchemaEntry
name="place_name"
:examples="[]">
</SchemaEntry>

<SchemaEntry
name="place_name_variants"
:examples="[]">
</SchemaEntry>

<SchemaEntry
name="place_type"
:examples="[]">
</SchemaEntry>

## Additional columns

<SchemaEntry
name="institution_name"
type="string"
:examples="[]">
</SchemaEntry>
