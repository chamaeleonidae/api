# Segmentation Filter Expressions

**A filter expression is a type of codified query used for user segmentation, that contains a combination of keys and values that instruct the query builder how to query the User Profile data.**

------



## Schema :id=schema

| Property | Type | Description |
| --- | --- | --- |
| `id` | ID | The Chameleon ID |
| `created_at` | timestamp | When this happened or when this was added to the Database |
| `updated_at` | timestamp | The last time any property was updated |
| `kind` | string | The type of Segmentation filter item: One of `property`, `event`, `tour`, `action`, `intercom`, or `segment` |
| `integration` | string | The data partner if any |
| `prop` | string | The specific property that forms the left hand side of an expression |
| `op` | string | The specific operation to be performed. Can be compounded with a value translation |
| `value` | string | The specific Value that forms the right hand side of an expression |
| `mod` | string | A secondary condition is modified with this Operator |
| `range` | string | A secondary condition is compared with this Value |
| `cond` | string | A Secondary condition Operator used 1-to1 with `int` to form a time-range limitation on the main match |
| `int` | string | Used 1-to-1 with `cond` to specify an interval |

Not all combinations of keys and values will work, see the other subsections for specific definitions and usage.

## Operators

> *Note: The table below should be read with the description prefixed with **The User property (is/has)...***

| Operator | description                                                  |
| -------- | ------------------------------------------------------------ |
| `ex`     | Has any value (the key is present even null)                 |
| `nx`     | Does not have any value (the key is missing)                 |
| `eq`     | Equal to                                                     |
| `ne`     | Not equal to                                                 |
| `gt`     | Greater than (number, string or specific timestamp)          |
| `lt`     | Less than                                                    |
| `gt-d`   | Greater than when the value is treated as a number of days in the past (timestamp is newer than X days ago) |
| `lt-d`   | Less than when the value is treated as a number of days in the past (timestamp is older than X days ago) |
| `in`     | Contains (i.e. one string is contained within another)       |
| `nin`    | Not contains                                                 |
| `in-v`   | *Included* in the list when value is treated as a CSV        |
| `nin-v`  | *Excluded* from list when the value is treated as a CSV      |
| `in-a`   | The property is an Array, is this value *Included* in the list |
| `nin-a`  | The property is an Array, is this value *Excluded* from the list |

Not all combinations of kinds and operators will work, see the other subsections for specific definitions and usage

## Examples

#### User whose "role is admin"

```json
{
  "kind": "property",
  "prop": "role",
  "op": "eq",
  "value": "admin"
}
```

#### User whose "role is admin or owner or superuser"

Operator if `in-v` means treat the value as a CSV `["admin","owner","superuser"]` and see if `role` is contained in the list.

```json
{
  "kind": "property",
  "prop": "role",
  "op": "in-v",
  "value": "admin,owner,superuser"
}
```

#### User was was last seen more than 7 days ago

The postfix `-d` in `lt-d` instructs the value to be treated as a number of days.

Subtract X days from the current time and look for `last_seen_at` values that are less than it.


```json
{
  "kind": "property",
  "prop":"last_seen_at",
  "op":"lt-d",
  "value":"7"
}
```

