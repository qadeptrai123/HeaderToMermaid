#Author: Le Quoc Anh 23CLC04 HCMUS
#Donate: fuck you

def getText(path: str):
    text = ""
    with open(path, "r") as f:
        text = f.read()
    return text

def setFlag(flag):
    if flag == 1:
        return '+'
    else:
        return '-'

def export(path: str, classes):
    with open(path, "w") as f:
        f.write("```mermaid\n")
        f.write("classDiagram\n")
        for cls in classes:
            lines = [line.strip() for line in cls.split("\n") if line != '']
            f.write(lines[0] + '\n')
            
            attributes = []
            actions = []
            
            if lines[1].find(':') == -1:
                lines.insert(1, 'private:')
            flag = 0
            # print(lines)
            for i in range(1, len(lines)-1):
                if lines[i][-1] == ':':
                    if lines[i] == 'private:':
                        flag = -1
                    else:
                        flag = 1
                else:
                    lines[i] = lines[i][:-1]
                    if lines[i].find('(') == -1:
                        dataType = lines[i][:(lines[i].find(' '))]
                
                        variables = [setFlag(flag) + dataType + ' ' + var.strip() for var in lines[i][lines[i].find(' '):].split(',') if var]
                        attributes.extend(variables)
                    else:
                        actions.append(setFlag(flag) + ' ' + lines[i])
            # print(attributes)
            for attr in attributes:
                f.write(attr + '\n')
            # print(actions)
            for act in actions:
                f.write(act + '\n')
            # print('\n\n\n')
            f.write('}\n')
                    
        f.write("```")
            
def main():
    src = input("Enter the path of the header file: ")
    content = getText(src)
    pos = content.find('class ')
    if pos == -1:
        print("Invalid format")
        return    
    content = content[pos:]
    classes = [("class " + cls).strip() for cls in content.split('class ') if cls != '']
    # print(classes)
    dest = input("Enter name of output file (file will generate in Output folder): ")
    output = export('./Output/' + dest, classes)
    
    
if __name__ == "__main__":
    main()

