from bs4 import BeautifulSoup
import copy
import os






# Read the HTML content from index.html
with open("Web_portion\index.html", "r") as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, 'html.parser')

def first_filters(category):
    category_container = soup.find('ul',{'id':'portfolio-flters'})
    filter_option = soup.new_tag('li')
    filter_option['data-filter'] = '.filter-'+str(category)
    filter_option.string = str(category)
    category_container.append(filter_option)
    
    category_container = soup.prettify()

    with open("index2.html", "w") as f:
            f.write(category_container)
            print('done with filters')

def post_field(folder,category = None):
    

    
    container = soup.find('div',{'class': 'portfolio-container'})
    filter_div = soup.new_tag('div')
    if category:
        filter_div['class'] = 'col-lg-3 col-md-6 portfolio-item filter-' + str(category)
    else: 
        filter_div['class'] = 'col-lg-3 col-md-6 portfolio-item '
    portfolio_wrap = soup.new_tag('div')
    portfolio_wrap['class'] = 'portfolio-wrap'
    img_container = soup.new_tag('img')
    img_container['class'] = 'img-fluid'
    img_container['src'] = os.path.join(folder,os.listdir(folder)[0])
    portfolio_wrap.append(img_container)
    info_div =  soup.new_tag('div')
    info_div['class'] = 'portfolio-info'

    portfolio_wrap.append(info_div)

    portfolio_links_div =  soup.new_tag('div')
    portfolio_links_div['class']= 'portfolio-links'
    slider_link1 = soup.new_tag('a')
    print(str(os.path.join(folder,os.listdir(folder)[0])))

    slider_link1['href'] =  os.path.join(folder,os.listdir(folder)[0])

    slider_link1['title'] = 'Example title'
    slider_link1['class'] = 'portfolio-lightbox'
    slider_link1['data-gallery'] = os.path.basename(folder)
    portfolio_linksI =  soup.new_tag('i')
    portfolio_linksI['class'] = 'bx bx-plus'
    slider_link1.append(portfolio_linksI)
    slider_link2 = soup.new_tag('a')

    slider_link2['href'] =  'https://www.' + str(os.path.basename(folder)).replace('-','/')
    slider_link2['class']= "More Details"
    slider_link2['target'] ="_blank"
    portfolio_links2I =  soup.new_tag('i')
    portfolio_links2I['class'] = "fa fa-instagram"
    slider_link2.append(portfolio_links2I)
    portfolio_links_div.append(slider_link1)
    portfolio_links_div.append(slider_link2)
    portfolio_wrap.append(portfolio_links_div)

    for photo in os.listdir(folder)[1::]:
            photo_link = os.path.join(folder,photo)
            photo_linkA = soup.new_tag('a')            
            photo_linkA['class'] = 'portfolio-lightbox'
            photo_linkA['data-gallery'] = os.path.basename(folder)
            photo_linkA['href'] = photo_link

            portfolio_wrap.append(photo_linkA)
    
    filter_div.append(portfolio_wrap)
    
    container.append(filter_div)
    
    container = soup.prettify()

    with open("index2.html", "w") as f:
            f.write(container)
            print('dome')


def new_post(folder):
    original_portfolio_item = soup.find('div', {'class': 'portfolio-item'})

    if original_portfolio_item:
        # Create a copy of the original portfolio-item div
        portfolio_item_copy = copy.copy(original_portfolio_item)
        counter = 1
        first_image = portfolio_item_copy.find('img',{'class' : 'img-fluid'})
        first_image['data-gallery'] = os.path.basename(folder)
        
        # Update the data-gallery and href attributes of the anchor tags inside the copied div
        for anchor_tag in portfolio_item_copy.find_all('a', {'class': 'portfolio-lightbox'}):
            anchor_tag['data-gallery'] = os.path.basename(folder)
            print(os.listdir(folder))
            print(str(os.path.join(folder,os.listdir(folder)[counter])))
            anchor_tag['href'] = os.path.join(folder,os.listdir(folder)[counter])
            counter +=1

        # Append the copy to the parent container, right after the original div
        parent_container = original_portfolio_item.find_parent()
        parent_container.append(portfolio_item_copy)

        # Save the updated HTML content back to index.html
        updated_html_content = soup.prettify()

        with open("index2.html", "w") as f:
            f.write(updated_html_content)

        print("Portfolio-item div duplicated and saved to index.html with updated attributes.")
    else:
        print("Portfolio-item div not found in the HTML content.")
  
  
  
def all_in_one(root_folder):
    for post_folder in os.listdir(root_folder):
        
        original_portfolio_item = soup.find('div', {'class': 'portfolio-item'})
            # Create a copy of the original portfolio-item div
        portfolio_item_copy = copy.copy(original_portfolio_item)
        for post_image in os.listdir(os.path.join(root_folder,post_folder)):
           
            post_image_link = os.path.join(root_folder,os.path.join(post_folder,post_image))
            
            if post_image != os.listdir(os.path.join(root_folder,post_folder))[0]:#if its not the last make a copy for the next iteration to edit
                to_delete = (image_panel.find('i'))
                print(to_delete)
                if to_delete:
                    to_delete.extract()
            if post_image == os.listdir(os.path.join(root_folder,post_folder))[0]:  #if its the first image, it needs to be the one seen and leads to the gallary
                
                first_image = portfolio_item_copy.find('img',{'class' : 'img-fluid'})
                first_image['src'] = post_image_link
                
                first_cover_image = portfolio_item_copy.find('a', {'class': 'portfolio-lightbox'})
                first_cover_image['data-gallery'] = os.path.basename(post_folder)
                first_cover_image['href'] =post_image_link
                
                parent_container = original_portfolio_item.find_parent()
                parent_container.append(portfolio_item_copy)

                # Save the updated HTML content back to index.html
                updated_html_content = soup.prettify()

                with open("index2.html", "w") as f:
                    f.write(updated_html_content)
                       
            image_panel = portfolio_item_copy.findNext('a',{'class' : 'portfolio-lightbox'})
            image_panel['data-gallery'] = os.path.basename(post_folder)
            image_panel['href'] =post_image_link

            
            if post_image != os.listdir(os.path.join(root_folder,post_folder))[-1]:#if its not the last make a copy for the next iteration to edit

                image_panel2 = copy.copy(image_panel)
                parent_container = image_panel.find_parent()
                parent_container.append(image_panel2)


                    # Save the updated HTML content back to index.html
            updated_html_content = soup.prettify()

            with open("index2.html", "w") as f:
                f.write(updated_html_content)
                       
      
      
pathway = r"C:\Users\ratth\Downloads\Insta to Bootstrap\Categories_folder"

def category_level_down(head_folder):
    for category in os.listdir(head_folder):
        first_filters(str(os.path.basename(category)))
        category_path = os.path.join(head_folder,category)
        for folder in os.listdir(category_path):
            post_field(os.path.join(category_path,folder),str(os.path.basename(category_path)))
                

category_level_down(pathway)
