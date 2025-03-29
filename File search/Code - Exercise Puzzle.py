import shutil, os, re, pdb
filename = 'unzip_me_for_instructions.zip'
dir_to_unzip = os.getcwd()

shutil.unpack_archive(filename, '', format='zip')

cwd = dir_to_unzip #Current working Directory
with open(cwd + '\\extracted_content\\Instructions.txt', 'r') as file:
    print('Instructions below:\n'+file.read()+'\n')

#set the pattern for the phone number
search_pattern = r'\d{3}-\d{3}-\d{4}'

#define a function to seach the pattern within the file
def pattern_search(file, pattern = r'\d{3}-\d{3}-\d{4}'):
    f = open(file, 'r')
    text = f.read()

    if re.search(pattern, text):
        #returning a Tuple
        return (re.search(pattern, text), file)

#Set working directory
work_dir = cwd + '\\test_folder'    #change this to '\\extracted_content' once the contents are unzipped

result = []

#find all the files present with os.walk()
for folder, subfolders, files in os.walk(work_dir):
    #print('Currently looking at the folder:\n'+folder)
    
    for file in files:
        full_path = folder+'\\'+file

        result.append(pattern_search(full_path, search_pattern))

for r in result:
    if r:
        match, file = r #Tuple unpacking
        print('Phone number: '+match.group())
        print(f'Full Path: \n\t{file}')
        print(f'\nFilepath: {'\\'.join(re.findall(r'[^\\]+', file)[:-1])}')
        print(f'\nFilename: {re.search(r'[^\\]+$', file).group()}')