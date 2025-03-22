# Element Interface: All elements in the document must implement this
class DocumentElement:
    def accept(self, visitor):
        pass


# Concrete Elements: Heading, Paragraph, Image
class Heading(DocumentElement):
    def __init__(self, text):
        self.text = text

    def accept(self, visitor):
        visitor.visit_heading(self)


class Paragraph(DocumentElement):
    def __init__(self, text):
        self.text = text

    def accept(self, visitor):
        visitor.visit_paragraph(self)


class Image(DocumentElement):
    def __init__(self, src):
        self.src = src

    def accept(self, visitor):
        visitor.visit_image(self)


# Visitor Interface: Defines operations for each element type
class DocumentVisitor:
    def visit_heading(self, heading):
        pass

    def visit_paragraph(self, paragraph):
        pass

    def visit_image(self, image):
        pass


# Concrete Visitors: HTML Exporter and Spell Checker
class HTMLExporter(DocumentVisitor):
    def visit_heading(self, heading):
        print(f"<h1>{heading.text}</h1>")

    def visit_paragraph(self, paragraph):
        print(f"<p>{paragraph.text}</p>")

    def visit_image(self, image):
        print(f'<img src="{image.src}" />')


class SpellChecker(DocumentVisitor):
    def visit_heading(self, heading):
        print(f"Spell-checking heading: {heading.text}")

    def visit_paragraph(self, paragraph):
        print(f"Spell-checking paragraph: {paragraph.text}")

    def visit_image(self, image):
        print(f"Spell-checking skipped for image: {image.src}")


# Document: A collection of elements
class Document:
    def __init__(self):
        self.elements = []

    def add_element(self, element):
        self.elements.append(element)

    def accept(self, visitor):
        for element in self.elements:
            element.accept(visitor)


# Usage
if __name__ == "__main__":
    # Create a document
    document = Document()
    document.add_element(Heading("Welcome to the Visitor Pattern"))
    document.add_element(Paragraph("This is a simple example of the Visitor Pattern."))
    document.add_element(Image("example.jpg"))

    # Export to HTML
    print("Exporting to HTML:")
    html_exporter = HTMLExporter()
    document.accept(html_exporter)

    # Spell-check the document
    print("\nSpell-checking the document:")
    spell_checker = SpellChecker()
    document.accept(spell_checker)
