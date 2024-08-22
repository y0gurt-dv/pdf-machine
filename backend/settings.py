from playwright.async_api import Browser, BrowserContext
from dataclasses import dataclass
import os

@dataclass
class Settings:
    browser: Browser | None = None
    browser_context: BrowserContext | None = None
    base_tmp: str = os.path.join('tmp')

