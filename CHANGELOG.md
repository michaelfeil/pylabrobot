# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## Unreleased

### Changed

- The `offset` attribute of `Pickup`, `Drop`, `Aspirate`, and `Dispense` dataclasses are now always wrt the center of its `resource`.
- The `offset` parameter is no longer optional in `Pickup`, `Drop`, `Aspirate`, and `Dispense` dataclasses. With LiquidHandler it defaults to `Coordinate(0, 0, 0)`.
- When providing offsets to LH, individual items in the `offsets` list are no longer optional. They must be provided as `Coordinate` objects. The `offsets` list itself is still optional and defaults to `[Coordinate(0, 0, 0)]*len(use_channels)`.
- To aspirate from a single resource with multiple channels, you must now provide that single resource in a list when calling `LiquidHandler.aspirate` and `LiquidHandler.dispense`.
- The non-firmware level commands of `STAR` now take parameters in PLR-native units (mm, uL, mg, etc.) instead of the mixture of PLR-native and firmware-native units (0.1mm, 0.1uL, etc.) that were previously used. The affected commands are `pick_up_tips`, `drop_tips`, `aspirate`, `dispense`, `pick_up_tips96`, `drop_tips96`, `aspirate96`, `dispense96`, `iswap_pick_up_resource`, `iswap_move_picked_up_resource`, `iswap_release_picked_up_resource`, `core_pick_up_resource`, `core_move_picked_up_resource`, `core_release_picked_up_resource`, `move_resource`, and `core_check_resource_exists_at_location_center` (https://github.com/PyLabRobot/pylabrobot/pull/191).
- Also for Vantage, the units of the parameters are now in PLR-native units instead of the mixture of PLR-native and firmware-native units (0.1mm, 0.01uL, 0.1uL, etc.) that were previously used. The affected commands are `pick_up_tips`, `drop_tips`, `aspirate`, `dispense`, `pick_up_tips96`, `drop_tips96`, `aspirate96`, `dispense96`, `pick_up_resource`, and `release_picked_up_resource`.
- Fixed well z position: now it actually refers to the distance between the bottom of the well (including the material) and the bottom of the plate. Before, it sometimes mistakenly referred to what is now `material_z_thickness` (https://github.com/PyLabRobot/pylabrobot/pull/183).
- A resource's origin (lfb) is not changed on rotation, it is always fixed locally (https://github.com/PyLabRobot/pylabrobot/pull/195). Before, we updated the location after 90, 180, and 270 degree rotations.
- `Resource.rotate` and `Resource.rotated` now support all planes and all angles (before it was limited to 90 degree rotations around the z axis) (https://github.com/PyLabRobot/pylabrobot/pull/195)
- Resource children will not be relocated when the parent resource is rotated (https://github.com/PyLabRobot/pylabrobot/pull/195)
- `Resource.rotation` attribute is now a `Rotation` object (https://github.com/PyLabRobot/pylabrobot/pull/195)
- Parameters to higher-level STAR commands may be ints or floats, and will be converted to int when passed to the firmware-level commands.
- `ItemizedResource` now supports arbitrary patterns, not just full grids (https://github.com/PyLabRobot/pylabrobot/pull/201/):
  - Parameter `items` of `ItemizedResource.__init__` is deprecated in favor of `ordered_items`.
  - Rename parameter `identifier` of `ItemizedResource.get_items` to `identifiers`.
  - Attributes `ItemizedResource.num_items_x` and `ItemizedResource.num_items_y` are now computed, and raise an error when the grid is not rectangular/full.
  - `ItemizedResource` now serializes `"ordering"`, and not `"num_items_x"` and `"num_items_y"`.

### Added

- Cor_96_wellplate_360ul_Fb plate (catalog number [3603](https://ecatalog.corning.com/life-sciences/b2b/NL/en/Microplates/Assay-Microplates/96-Well-Microplates/Corning®-96-well-Black-Clear-and-White-Clear-Bottom-Polystyrene-Microplates/p/3603))
- Add attribute `material_z_thickness: Optional[float]` to `Container`s (https://github.com/PyLabRobot/pylabrobot/pull/183).
- `Coordinate.vector()` to return a 3-item list of floats.
- `Rotation` class to represent a rotation in 3D space (https://github.com/PyLabRobot/pylabrobot/pull/195)
- `Resource.get_absolute_rotation()` to get the absolute rotation of a resource (https://github.com/PyLabRobot/pylabrobot/pull/195)
- `pedestal_size_z` to `PLT_CAR_L5MD` and `PLT_CAR_L5MD_A00` (https://github.com/PyLabRobot/pylabrobot/pull/198/).
- `create_ordered_items_2d`, similar to `create_equally_spaced_2d`, but a dictionary keyed by the item's position identifier in the grid (https://github.com/PyLabRobot/pylabrobot/pull/201/)

### Deprecated

- All VENUS-imported Corning-Costar plates, because they don't have unique and usable identifiers, and are probably wrong.
- HamiltonDeck.load_from_lay_file
- Passing single values to LiquidHandler `pick_up_tips`, `drop_tips`, `aspirate`, and `dispense` methods. These methods now require a list of values.
- `hamilton_parse` module and the VENUS labware database parser.
- `PLT_CAR_L4_SHAKER` was deprecated in favor of `MFX_CAR_L5_base` (https://github.com/PyLabRobot/pylabrobot/pull/188/).
- `utils.positions`: `string_to_position`, `string_to_index`, `string_to_indices`, `string_to_pattern`.

### Fixed

- Don't apply an offset to rectangle drawing in the Visualizer.
- Fix Opentrons resource loading (well locations are now lfb instead of ccc)
- Fix Opentrons backend resource definitions: Opentrons takes well locations as ccc instead of lfb
- Fix ThermoScientific_96_DWP_1200ul_Rd to ThermoScientific_96_wellplate_1200ul_Rd (https://github.com/PyLabRobot/pylabrobot/pull/183).
- `libusb_package` is now an optional dependency.
