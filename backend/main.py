from contextlib import asynccontextmanager
from playwright.async_api import async_playwright
from fastapi import FastAPI, Query, Response, HTTPException
from settings import Settings
from enums import FormatEnum, WaitUntilEnum


settings = Settings()

@asynccontextmanager
async def lifespan(app: FastAPI):
    playwright = await async_playwright().start()
    browser = await playwright.chromium.launch()
    browser_context = await browser.new_context()

    settings.browser = browser
    settings.browser_context = browser_context

    yield

    # on end
    await browser.close()
    await playwright.stop()


app = FastAPI(
    lifespan=lifespan,
    title="PDF Create",
    docs_url="/docs/"
)


@app.get("/create-pdf/")
async def get_pdf(
    landscape: bool = False, 
    link: str = Query(description="Link of page. If page under base auth url must be: https://username:password@google.com"),
    format: str | None = Query(default=None, enum=[i.value for i in FormatEnum]),
    page_ranges: str | None = Query(default=None, description="Paper ranges to print, e.g., '1-5, 8, 11-13'. Defaults to the empty string, which means print all pages."), 
    width: int | None = Query(default=None, description="Output width in pixels. Use only in format is None"),
    height: int | None = Query(default=None, description="Output height in pixels. Use only in format is None"),
    name: str = Query(default="output", description="Output filename without format"),
    wait_until: str = Query(
        default="networkidle",
        description=(
            " - **domcontentloaded** - consider operation to be finished when the `DOMContentLoaded` event is fired.\n"
            " - **load** - consider operation to be finished when the `load` event is fired.\n"
            " - **networkidle** - consider operation to be finished when there are no network connections for at least 500 ms\n"
            " - **commit** - consider operation to be finished when network response is received and the document started loading.\n"
        ),
        enum=[i.value for i in WaitUntilEnum]
    )) -> Response:


    if format is None and (width is None or height is None):
        raise HTTPException(400, detail="You must set format or width with height")

    if format is not None and width is not None and height is not None:
        raise HTTPException(400, detail="You must set only format or width with height")

    page = await settings.browser_context.new_page()
    await page.goto(link, wait_until=wait_until)
    
    query = {
        "landscape": landscape,
        "format": format,
        "page_ranges": page_ranges,
        "width": width,
        "height": height,
        "print_background": True,
    }
    buffer = await page.pdf(**query)

    await page.close()

    headers = {'Content-Disposition': f'inline; filename="{name}.pdf"'}
    return Response(buffer, headers=headers, media_type='application/pdf')
