## Project Description

The simple way of making GIF.

You can make gif with image urls or PIL image list.

## Installation

The recommended way to install is via [pip](https://pypi.org/project/pip/)

```bash
$ pip install py-gifmaker
```

## Getting Started

```python
from py_gifmaker import GifMaker
gifmaker = GifMaker()
```

-   output_filename: ex) "output.gif"
-   images: List of image src
-   fps: 1 frame per second
-   loop: 0 for infinite 1 for once

<strong>If you want to make GIF with image urls</strong>

```python
images = [## Image src]

GifMaker.Make(output_filename, images, fps, loop)
```

<strong>If you want to make GIF with PIL images</strong>

```python
pil_images = [## PIL Image]

GifMaker.PIL(output_filename, pil_images, fps, loop)
```

## Support

If you find an bug, have any questions about how to use py-gifmaker or have suggestions for improvements then feel free to file an issue on the [Github project page](https://github.com/schooldevops/gifmaker/issues).

## License

All of the code contained here is licensed by the MIT.