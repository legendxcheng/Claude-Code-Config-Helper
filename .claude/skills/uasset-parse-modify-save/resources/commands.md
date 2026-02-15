# Command Templates

Run all commands from:

```powershell
E:\panda-oasis\UAssetAPI
```

## 1) Batch parse all `.uasset` files

```powershell
python scripts/test_uasset_parse.py "E:\panda-oasis\proj" "UNKNOWN"
```

Optional CSV report:

```powershell
python scripts/test_uasset_parse.py "E:\panda-oasis\proj" "UNKNOWN" "E:\panda-oasis\proj\uasset-parse-report.csv"
```

## 2) Discover export names for one file

Use a fake export/property so the tool prints available hints:

```powershell
python scripts/set_uasset_property.py `
  "E:\panda-oasis\proj\Asset\Blueprint\MainWidget.uasset" `
  "E:\panda-oasis\proj\Asset\Blueprint\MainWidget.modified.uasset" `
  "__NOT_FOUND__" `
  "__NOT_FOUND__" `
  "float" `
  "1.0" `
  "UNKNOWN"
```

## 3) Discover properties of a known export

```powershell
python scripts/set_uasset_property.py `
  "E:\panda-oasis\proj\Asset\Blueprint\MainWidget.uasset" `
  "E:\panda-oasis\proj\Asset\Blueprint\MainWidget.modified.uasset" `
  "MainWidget_C" `
  "__NOT_FOUND__" `
  "float" `
  "1.0" `
  "UNKNOWN"
```

## 4) Modify and save

```powershell
python scripts/set_uasset_property.py `
  "E:\panda-oasis\proj\Asset\Blueprint\MainWidget.uasset" `
  "E:\panda-oasis\proj\Asset\Blueprint\MainWidget.modified.uasset" `
  "MainWidget_C" `
  "bCookSlowConstructionWidgetTree" `
  "bool" `
  "false" `
  "UNKNOWN"
```

Success output includes `EDIT_OK` and `Before=` / `After=` lines.

## 5) Common failures

- `UnknownEngineVersionException` on parse: rerun with explicit engine version (for example `VER_UE4_18`).
- `Export not found`: use discovery command to list example exports.
- `Property not found`: use discovery command to list available properties for that export.
- `Property type mismatch`: change `value_type` to the property's actual type.
