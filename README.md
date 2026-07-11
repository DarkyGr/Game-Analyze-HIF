# GA - HIF

Calculate the quantity of each item to have for the Happy Island Fantasy run
(Read the README)

The numbers in the file_island.dat file must be changed.

The program returns the change for the in-game currency.

# TEInt Calculator

This utility calculates the `v0` and `v1` values used by the `TEInt` structure found in the game's save file.

## Formula

Encoding:

- `v0 = (value XOR 54321) + 13579`
- `v1 = (value + 13579) XOR 54321`

Decoding:

- `value = (v0 - 13579) XOR 54321`

## Limits

For safety, the tool only accepts values between:

- Minimum: `0`
- Maximum: `999999`

## Requirements

- Python 3.x

## Usage

```bash
python teint_calculator.py
```

Enter the desired amount of Bills when prompted. The program will output:

- `v0`
- `v1`
- A JSON snippet ready to paste into the save file.
