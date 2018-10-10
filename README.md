# minecraft-json-schema

Json schemas for Minecraft files. Information about json schemas can be found at
[json-schema.org](http://json-schema.org/)

## Design decisions

-   The use of the `minecraft:` namespace is mandatory anywhere it can be used.
    This does mean that it will not necessarily validate against all vanilla
    files

## Current progress

At the moment, the following files are supported:

1. `advancements`
2. `pack.mcmeta`
3. `.mcmeta` animation files
4. `loot_tables` files
5. `sounds.json`

### Future plans

The following files should be supported in the future

1. `model files`
2. `recipe files` (Waiting on official release in 1.13)

The following additions are planned

1. ~~Implementations into different uses of schemas - especially VSCODE, which
   has built in support~~ - Already implemented into VSCODE
2. An update/tidy up using more suitable schema object parts

## License

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons Licence" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This
work is licensed under a
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative
Commons Attribution 4.0 International License</a>.

Note that in `41a72f7` and earlier, the schemas were available under the
unlicense

### Projects known to be using this
