from dataclasses import dataclass
from playwright.sync_api import sync_playwright, Page


@dataclass
class ChemicalElement:
    atomic: str
    name: str
    weight: str

    def __str__(self):
        return f"{self.atomic}: {self.name}, {self.weight}"


def get_chemical_elements(page: Page) -> list[ChemicalElement]:
    elements = page.query_selector_all('[data-atomic]')
    chemical_elements = []
    for element in elements:
        atomic_number = element.get_attribute('data-atomic')
        name = element.query_selector('em').inner_text()
        weight = element.query_selector('data').get_attribute('data-abridged')
        chemical_elements.append(ChemicalElement(atomic_number, name, weight))
    return chemical_elements


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto('https://ptable.com/?lang=ru')

        elements = get_chemical_elements(page)
        for el in elements:
            print(el)

        browser.close()


if __name__ == "__main__":
    main()
