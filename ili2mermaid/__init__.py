import os
import re

cardinality_map {
    "0..*" : "0|"
}

def map_cardinality( firstcardinalit: str, secondcardinality: str ) -> str:
    return f"{cardinality_map[firstcardinalit]}--{cardinality_map[firstcardinalit]}"

def maid( ilicontent: str ) -> str:

    class_pattern = re.compile(r'CLASS (\w+) =\s*(.*?)\s*END \1;', re.DOTALL)
    association_pattern = re.compile(r'ASSOCIATION (\w+) =\s*(.*?)\s*END \1;', re.DOTALL)

    class_matches = re.finditer(class_pattern, ilicontent)
    association_matches = re.finditer(association_pattern, ilicontent)

    classes_dict = {}
    associations_dict = {}

    for match in class_matches:
        name = match.group(1)
        content = match.group(2)
        attributes = re.findall(r'(\w+)\s*:\s*(.*?);', content)
        attribute_dict = {attr[0]: attr[1].replace('MANDATORY', 'M_') for attr in attributes}
        classes_dict[name] = attribute_dict

    for match in association_matches:
        name = match.group(1)
        content = match.group(2)
        properties = re.findall(r'(\w+)\s*-\s*<#>\s*(\{.*?\})\s*(\w+);', content)
        properties_dict = {prop[2]: {'role': prop[0], 'cardinality': prop[1]} for prop in properties}
        associations_dict[name] = properties_dict

    ilidict = {
        'classes': classes_dict,
        'associations': associations_dict
    }

    maid = f"%%{{init: {{'theme': 'dark' }} }}%%\n\nerDiagram\n"

    for class_name in ilidict[classes].keys():
        maid.append(f"  {class_name} {{\n")
        for attr_name in ilidict[classes][class_name].keys():
            maid.append(f"    {ilidict[classes][class_name][attr_name]} {attr_name}\n")
        maid.append(f"  }}\n")

    for assoc_name in ilidict[associations].keys():
        targets = [for target in ilidict[associations][assoc_name]]

        #only handle two targets at the moment
        first_target = targets[0]
        second_target = targets[1]
            
        maid.append(f"  {class_name} {{\n")
        for attr_name in ilidict[classes][class_name].keys():
            maid.append(f"    {ilidict[classes][class_name][attr_name]} {attr_name}\n")
        maid.append(f"  }}\n")

def maid_from_file( ilifilepath: str, theme: str = 'dark' ) -> str:
    if ilifilepath:
        with open(ilifilepath, "r") as f:
            content = f.read()
            return maid(content)


def md_from_file( ilifilepath: str, theme: str = 'dark', outputfilepath: str = None):
    maid = maid_from_file(ilifilepath, theme)
    if maid:
        if not outputfilepath:
            outputfilepath = os.path.splitext(ilifilepath)[0]+'.md' 
        with open(outputfilepath, 'w') as f:
            f.write(maid)
            print (f"Maid written to {outputfilepath}")