#Instructions: use this to get the photos into the categories folder, 
# from there sort and rename the category1,category2,category3 folders
# to set the category names on the website. The category1 folder name 
# will determine said category name, and the folders inside will be the 
# folder of photos that sort under that
#I would automate it but different who knows what categories futures would want 

#next step is to run the 

import instaloader
import os
import shutil
loader = instaloader.Instaloader()
USER = 'poetixending'
PASSWORD = 'mrob6277MROB!!'






for post in list(instaloader.Profile.from_username(loader.context,'jenaissante').get_posts()):
    # post is an instance of instaloader.Post    print( post.shortcode)

    loader.download_post(post, target='instagram.com-p-' +post.shortcode)


def filter_and_copy_folders(root_dir, destination_dir, extensions):
    
    for foldername in os.listdir(root_dir):
        folder_path = os.path.join(root_dir, foldername)
        if os.path.isdir(folder_path) and 'instagram.com-p-' in str(folder_path) :
            destination_path = os.path.join(destination_dir, foldername)
            os.makedirs(destination_path, exist_ok=True)
            for filename in os.listdir(folder_path):
                file_path = os.path.join(folder_path, filename)
                if os.path.isfile(file_path) and filename.lower().endswith(extensions):

                    new_file_path = os.path.join(destination_path, filename)
                    shutil.copy2(file_path, new_file_path)
                    print(f"Copied file '{filename}' to '{new_file_path}'")

                    os.remove(file_path)
                else:
                    os.remove(file_path)
            os.rmdir(folder_path)





root_dir = os.path.dirname(os.path.abspath(__file__))

destination_dir = str(root_dir) + '/Categories_folder' # The destination directory where 'client' folders will be moved
extensions_to_move = ('.jpeg', '.jpg', '.mp4')

filter_and_copy_folders(root_dir, destination_dir,extensions_to_move)

