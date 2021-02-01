from xml.dom import minidom #importing module to parse xml file.
doc = minidom.parse("pro5.xml")#xml file parsed.
templates = doc.getElementsByTagName("template")#made list of elements whose tag is "template"
for template in templates:
    template_id = template.getAttribute("id")#getting id attribute.
    print("\n")
    print(f"Template id is {template_id}")
    x_path = template.getElementsByTagName("xpath")#getting x_path of current template.
    for x in x_path:
        x_path_position = x.getAttribute("position")#getting postition of xpath.
        print(f"x_path position : {x_path_position}")
        links = x.getElementsByTagName("link")#getting elementes named "links"
        print("HREF")
        for y in links:
            href = y.getAttribute("href").split('/')[-1]#getting name of the link.
            print(f"\tLink is {href}\n")
        scripts = x.getElementsByTagName("script")#getting script element.
        print("SOURCE")
        for y in scripts:
            src = y.getAttribute("src").split('/')[-1]#getting source_name of the element.
            print(f"\tSource of script is {src}\n")
        print("""-------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------""")