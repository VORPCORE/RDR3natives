# Pull request template
> [!IMPORTANT]
> Please complete all fields. PRs will not be merged if any fields are incomplete. Be respectful, and keep in mind that it may take some time for your PR to be reviewed.



### Description
- definition of _0x67A43EA3F6FE0076 as _CLEAR_HERD(Herd herd)
- definition of _0xE0961AED72642B80 as _DELETE_HERD(Herd herd)
- definition of _0x9E13ACC38BA8F9C3 as _IS_PED_IN_HERD(Herd herd, Ped ped)
- definition of _0x408D1149C5E39C1E as _REMOVE_HERD_PED(Herd herd, Ped ped)

### Examples

```lua
local Herd = CreateHerd()
AddPedToFlock(Herd, animalPed)
print(Citizen.InvokeNative(0x9E13ACC38BA8F9C3, animalPed)) -- _IS_PED_IN_HERD Print true
Citizen.InvokeNative(0x408D1149C5E39C1E, Herd, animalPed) -- _REMOVE_HERD_PED
print(Citizen.InvokeNative(0x9E13ACC38BA8F9C3, animalPed)) -- _IS_PED_IN_HERD Print false
Citizen.InvokeNative(0x67A43EA3F6FE0076, Herd) -- _CLEAR_HERD
Citizen.InvokeNative(0xE0961AED72642B80, Herd) -- _DELETE_HERD
print(IsHerdValid(Herd)) -- Print false
```

### Source 

- script_rel/act_caunc_rustling.ysc.c (l5855 ; l5856 ; l5913 ; l5915)

### Notes

- add any extra notes here