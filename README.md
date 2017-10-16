# minecraft-json-schema
Json schemas for various minecraft files. 
Json schema information can be found at [json-schema.org](http://json-schema.org/)


## Design decisions  
 - The use of the `minecraft:` namespace is mandatory anywhere it can be used. This does mean that it will not necessarily validate against all vanilla files

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

1. ~~Implementations into different uses of schemas - especially VSCODE, which has built in support~~ - Already implemented into VSCODE

## License  
These schemas are licensed under the UnLicense, and may be used freely without giving credit in your projects or for personal use

### Projects known to be using this