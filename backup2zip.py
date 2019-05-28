#! python3
# backupToZip.py - Copies an entire folder and its contents into
# a ZIP file whose filename contains time stamp.
# This script is for windows - davis

import zipfile, os, time, logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL)
logging.debug('Start of program')

def backupToZip(sourceFolder):

    # Backup the entire contents of "sourcefolder" into a ZIP file.

    sourceFolder = os.path.abspath(sourceFolder) # make sure folder is absolute
    print('The folder being backup is:  [ ' + sourceFolder + ' ]')
  
    destinationFolder = 'D:\\backup'
    os.chdir(destinationFolder) # place the zip file into the folder - added by davis
        
    # Figure out the filename this code should use based on current time stamp.

    timeStamp = time.strftime("%Y%m%d%H%M",time.localtime(time.time())) # Get current time stamp

    # Create a txt file that specifies the source folder
    logFileName = os.path.basename(sourceFolder) + '_backup' + timeStamp + '.txt'   # Create a log file name (in txt format)
    print('Creating a log file:    %s    ...'%(logFileName))
    logFile = open(logFileName,'w')
    logFileContent = 'The source folder is:  [ ' + sourceFolder + ' ]'
    print('The following info is saved in the log file:     ' + logFileContent)   # show the content of log file
    logFile.write(logFileContent)
    logFile.flush()                 # save it immediately into the log file
     
    logFile.close

    verifyLOG = open(logFileName)
    logging.debug('Verifying log file content :    %s'%(verifyLOG.read()))
    verifyLOG.close
    
    zipFilename = os.path.basename(sourceFolder) + '_backup' + timeStamp + '.zip'   # Figure out zip file name
   
   
    # Create the ZIP file.
    print('Creating %s    ...' % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # Walk the entire folder tree and compress the files in each folder.
    for foldername, subfolders, filenames in os.walk(sourceFolder):
        print('Adding files in %s...' % (foldername))
        zipPath = foldername.replace(sourceFolder,'')   # to shorten the path in zip file

        logging.debug('Verifying zipPath :  [  %s  ] '%(zipPath))
            
        # Add all the files in this folder to the ZIP file.
        for filename in filenames:
            newBase = os.path.basename(sourceFolder) + '_backup'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue   # don't backup the backup ZIP files
            backupZip.write(os.path.join(foldername, filename), os.path.join(zipPath,filename), compress_type=zipfile.ZIP_DEFLATED)

    logFilePath = os.path.join(destinationFolder,logFileName)
    backupZip.write(logFilePath, logFileName, compress_type=zipfile.ZIP_DEFLATED)
    backupZip.close()
    print('Done.')
    print(zipFilename + ' is saved at ' + destinationFolder)
    print('Backup is finished successfully!')


print('Pls specify the folder you would like to back up...')  # added by davis
print('Example: D:\\file\\python\\AutomatePDF')
folder_backup = input()   # specify a folder being backup  - added by davis

logging.debug('Input folder  is:  [ ' + folder_backup + ' ]')     # check input validation

backupToZip(folder_backup)

logging.debug('      = End of program =')








