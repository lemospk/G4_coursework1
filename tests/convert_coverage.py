import xml.etree.ElementTree as ET

tree = ET.parse("coverage.xml")
root = tree.getroot()

new_root = ET.Element("coverage", version="1")

for package in root.findall(".//package"):
    for class_ in package.findall(".//class"):
        filename = class_.get("filename")  
        file_element = ET.SubElement(new_root, "file", path=filename)

        for line in class_.find("lines"):
            line_number = line.get("number")
            hits = int(line.get("hits"))
            covered = "true" if hits > 0 else "false"
            ET.SubElement(file_element, "lineToCover", lineNumber=line_number, covered=covered)

tree = ET.ElementTree(new_root)
tree.write("sonar-coverage.xml")