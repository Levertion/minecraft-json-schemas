# Change Logs
All notable changes to the "minecraft-json-schemas" project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html)

## [Unreleased]
### Fixed
 - Incorrect references to json_component in shared definition
 - Fix only allowing functions and conditions with a `minecraft:` namespace in loot tables, as even the vanilla loot tables don't use it

## v0.1.0 - 2017-10-10
- Initial release
### Added
 - advancement support
 - loot table support
 - `pack.mcmeta` support
 - `sounds.json` support
 - other `.mcmeta` file support

 [Unreleased]: https://github.com/Levertion/minecraft-json-schemas/compare/v0.1.0...HEAD