# UI Validator

This tool is designed to compare a set of baseline images with their corresponding current versions and detect any differences beyond a specified tolerance level. It also supports region of interest (ROI) comparison if provided in a YAML file.

## Requirements

- Python 3.x
- PIL (Python Imaging Library)
- PyYAML

## Usage

1. Place your baseline images in the `baseline` directory.
2. Place the current versions of the images in the `atual` directory with filenames prefixed by `atual_`.
3. Optionally, define regions of interest (ROIs) in a YAML file named `rois.yaml`.
4. Run the script `validador_roi.py`.

## Configuration

- `diretorio_baseline`: Directory containing baseline images.
- `diretorio_atual`: Directory containing current version images.
- `diretorio_divergentes`: Directory to store images where differences are found.
- `tolerancia`: Tolerance level for image comparison.
- `rois.yaml`: YAML file containing ROIs for selective comparison.

## Output

- The script generates a combined image highlighting the differences if any are found.
- Results are printed to the console indicating the total tests performed, tests passed, and tests failed.

## Handling Failures

- If any tests fail, the script exits with a status code of 1.

## Example

```
python validador_roi.py
```

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

