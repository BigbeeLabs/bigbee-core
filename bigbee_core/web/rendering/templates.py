# bigbee_core/web/rendering/templates.py
from __future__ import annotations
from pathlib import Path
from typing import Iterable, Union, List

from jinja2 import Environment, FileSystemLoader, ChoiceLoader, PackageLoader
from starlette.templating import Jinja2Templates
from pypugjs.ext.jinja import PyPugJSExtension

_TEMPLATES: Jinja2Templates | None = None

def configure_templates(
    roots: Iterable[Union[str, Path]],
    include_core_package: bool = True,
) -> Jinja2Templates:
    loaders: List = [FileSystemLoader(str(Path(r))) for r in roots]
    if include_core_package:
        loaders.append(PackageLoader("bigbee_core", "web"))
    env = Environment(loader=ChoiceLoader(loaders), autoescape=True)
    env.add_extension(PyPugJSExtension)

    templates = Jinja2Templates(env=env)
    global _TEMPLATES
    _TEMPLATES = templates
    return templates

def T() -> Jinja2Templates:
    if _TEMPLATES is None:
        raise RuntimeError("Templates not configured. Call configure_templates([...]) at startup.")
    return _TEMPLATES