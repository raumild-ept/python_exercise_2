from xml.dom import minidom #importing module to parse xml file.
doc = minidom.parse("pro5.xml")#xml file parsed.
templates = doc.getElementsByTagName("template")#made list of elements whose tag is "template"
for template in templates:
    template_id = template.getAttribute("id")#getting id attribute.
    print("\n")
    print(f"Template id is {template_id}")
    x_path = template.getElementsByTagName("xpath")
    x_path_position = x_path.getAttribute("position")
    print(f"x_path position : {x_path_position}")
    links = x_path.getElementsByTagName("link")
    print("HREF")
    for y in links:
            href = y.getAttribute("href").split('/')[-1]
            print(f"\tLink is {href}\n")
    scripts = x_path.getElementsByTagName("script")
    print("SOURCE")
    for y in scripts:
            src = y.getAttribute("src").split('/')[-1]
            print(f"\tSource of script is {src}\n")