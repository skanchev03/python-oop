from math import ceil


class PhotoAlbum:
    PHOTOS_PER_PAGE = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = ceil(photos_count / cls.PHOTOS_PER_PAGE)
        return cls(pages)


    def add_photo(self, label: str):
        for index, page in enumerate(self.photos):
            if len(page) < self.PHOTOS_PER_PAGE:
                page.append(label)
                return f"{label} photo added successfully on page {index + 1} slot {len(page)}"
        return "No more free slots"

    def display(self):
        output = []
        separator = "-----------"
        for page in self.photos:
            output.append(separator)
            if page:
                output.append(" ".join("[]" for _ in page))
            else:
                output.append("")
        output.append(separator)
        return "\n".join(output)
