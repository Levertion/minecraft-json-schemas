# Change Logs

All notable changes to the "minecraft-json-schemas" project will be documented
in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to
[Semantic Versioning](http://semver.org/spec/v2.0.0.html)

## [v0.4.0] - 2018-10-11

-   1.13 update
-   License change - the schemas are now distributed under the CC-BY-4.0 license
    (rather than the unlicense)
-   Special thanks to [Misode](https://twitter.com/misoloo) for their hard work
    creating this update in
    [#3](https://github.com/Levertion/minecraft-json-schemas/pull/3)

## Added

-   Support for 1.13(.1):

    -   Data pack `pack.mcmeta`
    -   Updated IDs

-   Limited support for vscode snippets. This is only used in the `pack.mcmeta`
    schema currently.
-   `package.json` so the schemas can be installed using `npm`
-   A playground in the repository itself for faster testing

### Changed

-   Changed all paths:
    -   all schemas are in the `java` folder for java edition
    -   schemas are split into `assets` and `data` folders for resource and data
        packs respectively
    -   `shared/minecraft_definitions` has been split into multiple files

### Fixed

-   Erroneous failures due to misuse of schema `not` key with `properties`.
-   [#2](https://github.com/Levertion/minecraft-json-schemas/issues/2) - support
    "empty" loot table type

## [v0.3.0] - 2017-10-29

-   Maintenance Update

### Added

-   Blockstate definitions

### Changed

-   Moved all shared definitions inside a `"definitions"` key to validate
    against the schema schema (http://json-schema.org/schema#)
-   Refactored Loot table `"entries"` so that quality and weight are not
    repeatedly defined
-   Description of `"parent"`, `"requirements"`
-   Advancement criteria default to have a default of `""`

### Fixed

-   Missing `player_hurt_entity` advancement criteria
-   Text object not showing an error when there are undefined properties

## [v0.2.0] - 2017-10-16

-   Namespace Update

### Changed

-   Force all places that a `minecraft:` namespace can be used to be used and
    add mention in README.md
-   Effects object of advancements now checks if it follows the name of an
    effect

### Fixed

-   Namespace recognition not working properly

## [v0.1.2] - 2017-10-15

-   Important Bugfix update

### Fixed

-   Property not allowed error
    -   Due to `"additionalProperties":false` being outside `oneOf`s rather than
        inside
    -   Property tree is not automatically collapsing
    -   Had to remove `"additionalProperties":false` for text components, as it
        is not possible to block additional properties for text components
        without moving all parts which can apply to all component types

## [v0.1.1] - 2017-10-11

-   Bugfix update

### Fixed

-   Incorrect references to json_component in shared definition
-   Only allows functions and conditions with a `minecraft:` namespace in loot
    tables, as even the vanilla loot tables don't use it
-   Property not defined error

## v0.1.0 - 2017-10-10

-   Initial release

### Added

-   advancement support
-   loot table support
-   `pack.mcmeta` support
-   `sounds.json` support
-   other `.mcmeta` file support

[unreleased]:
    https://github.com/Levertion/minecraft-json-schemas/compare/v0.3.0...HEAD
[v0.3.0]:
    https://github.com/Levertion/minecraft-json-schemas/compare/v0.2.0...v0.3.0
[v0.2.0]:
    https://github.com/Levertion/minecraft-json-schemas/compare/v0.1.2...v0.2.0
[v0.1.2]:
    https://github.com/Levertion/minecraft-json-schemas/compare/v0.1.1...v0.1.2
[v0.1.1]:
    https://github.com/Levertion/minecraft-json-schemas/compare/v0.1.0...v0.1.1
