import zipfile, os, datetime
from datetime import datetime
zipFilename='ren'+'_'+str(datetime.date(datetime.now()))+'.zip'

target_folder='E:\\'+zipFilename
print(target_folder)
def backupToZip(folder):
    # Backup the entire contents of 'folder' into a ZIP file.
    folder=os.path.abspath(folder)  #make sure folder is absolute    
    # Create the ZIP file.
    print(f'Creating {zipFilename}...')
    #global target_folder
    #targetFolder=open(target_folder,'w')
    backupZip=zipfile.ZipFile(str(target_folder),'w')
    print(backupZip)
    print('////',os.getcwd())
    # Walk the entire folder tree and compress the files in each folder.
    for foldername, subfolders, filenames in os.walk('C:\\Users\\Shaik Azharuddin\\Desktop\\Python'):
        print(f'Adding files in {foldername}...')
        #add the current folder to the Zip file
        backupZip.write(foldername)

        #add all the files in this folder to the Zip file.
        for filename in filenames:
            backupZip.write(os.path.join(foldername,filename))
    backupZip.close()

    print('Done')


backupToZip('C:\\Users\\Shaik Azharuddin\\Desktop\\Python')

