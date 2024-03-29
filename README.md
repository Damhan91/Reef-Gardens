![Responsive](https://github.com/Damhan91/Reef-Gardens/blob/main/readme%20images/Am%20I%20responsive.JPG)

Reef Gardens has been built for my 5th and final project for Code Institutes Full Stack Software Development program. Reef Gardens is an E-commerce Website, where customer can purchase and browse for either captive breed Marine fish or corals. The website provides a list of products that can be conveniently purchased from the store. After the user has selected their goods, they are taken through the order confirmation process and collection of payment. This system is implemented using python and the Django framework.

Link to Reef Gardens can be found [Here](https://reef-gardens.herokuapp.com/)

## User Stories

**Primary Goals**
  
**As a first time user, I want to:**
  * Easily understand what the website is trying to achieve and understand its purpose
  * Be able to navigate through the website with ease
  * View the list of products based on their category.
  * View the details of a single products, so I can understand the details, price and rating if any.
  * I can add product to my bag with "add to bag" so that I can purchase the item.
  * I can click the remove button, so that I can easily remove products from my cart.
  * Sort the view of products by price low to high. So that I can make an informed purchased based on price.
  * Be able to register for an account, which would allow me to have a more personalised experience.
  * Easily view the value of my shopping cart anywhere on the website. So that I can understand how much I have selected.
  * I want to be able to easily view the total amount in my shopping kart anywhere on the website. This will help me understand how much my total spend is.
  * I want to be able to see what products are in my shopping bag, so I can make adjustments if necessary.
  * Access to the companies social media links.
  * Easily search for items in the search bar.
  * Be able to sign up to a newsletter if I choose to do so. This will allow me to keep up do date with the companies newsletters
  
**As a registered user, I want to:**
  * Be able to login to my account with ease and view my orders
  * Be able to logout with ease.
  * View the list of products based on their category.
  * Be able to update my payment and personnel details.
  * Be able to view my order history.

**As a super user, I want to:**
  * Be able to add new products to the store.
  * Edit and update existing store products to change pricing, images etc.
  * Delete items from the store if necessary.
  

## Business Model
I have chosen a B2C (Business to Customer) business model. This is more straight forward for the end user as they only have one point of contact. Having the business model B2C also allows for the customer to get the best price possible as you do not have to pay a middleman.

The business flow is as follows:

  * Reef Gardens breed fish and cultivate corals (captive breeding program)
  * The products are then set up on the website for the user to purchase.
  
**Marketing**
For marketing Reef Gardens will use a FaceBook Business Page. Reef Gardens will also use Mailchimp for user who wish to sign up. The user will be given a notification once they have successfully sign up.

Facebook Business Page<details>
        ![Facebook](https://github.com/Damhan91/Reef-Gardens/blob/main/media/Facebook.png)        
        </details>
**Search Engine Optimisation**

I researched some of the most popular words that is used for searching for tropical fish. I included them in the title and description.

![Meta Description](https://github.com/Damhan91/Reef-Gardens/blob/main/media/meta%20tags.JPG)


## Features 
**Top Header**
  * **Navigation bar**: The navigation bar is available throughout the website. This ensures that the user can access any page ant any time. It helps the user move through the website with ease.  
  * **Search Bar**: The navigation bar is available throughout the website. This gives the user a great experience in searching for an item quickly,
  * **Login/Logout and Register**: This is located at the top right-hand corner of the website. This feature allows a user to either login, logout, or register.
  * **Shopping bag**: Again, the shopping bag is also located in the top right-hand corner of the website, which ensure the user will always have visibility to the value of the shopping bag and is also available throughout the website. The increase and decrease buttons also work as expected.
  * **Checkout**: The checkout is accessed through the shopping bag. When the user is happy with what they have chosen to purchase, they are brought to the checkout area, where they can see the summary of what they are about to buy and update their details.
  * **Payment**: The payment feature is used by implementing stripe. Once the user had finished entering their shipping details, they can then enter their card details and are notified once their payment is successful.
**Products**
The product can be views from anywhere in the website. The user can choose to view all products or choose a specific category (fish or coral), once they are on their selected category, they can choose from multiple choices to filter through the products (low to high price, a-z name etc).

**About Us**
The about us tab gives the user a short background on Reef gardens and what we are trying to achieve and accomplish.

**Blog**
The blog section is where blogs for tips an news will be posted for the user to read.

**Footer**
The footer is located at the bottom of the website. This can be viewed from all webpages and have a few features within the footer
  * **Social Media links**: The social media links are displayed in very easy to see. it's important to have the social media link viable to ensure as many users as possible come and follow you links.
  * **Newsletter Sign up**: The sign-up form for newsletters is also displayed in the footer. This allows the user to sign up for Reef Gardens Newsletter is the wish. This can also be viewed anywhere on the site

**Future Features**
  
  * Add a blog section
  * Add a video tutorial section
  * Add favourites to Profile
  * Add dry goods
  * Log in with social media
  * Add discount for active members (accumulate points with every purchase)

## Wireframes
Home<details>
        ![Wireframe](https://github.com/Damhan91/Reef-Gardens/blob/main/media/Wireframe%20Home%20Page.JPG)
        ![Wireframe](https://github.com/Damhan91/Reef-Gardens/blob/main/media/Wireframe%20Home%20Page%20Mobile.JPG)
        </details>
About<details>
        ![Wireframe](https://github.com/Damhan91/Reef-Gardens/blob/main/media/About%20Us%20Wireframe.JPG)
        ![Wireframe](https://github.com/Damhan91/Reef-Gardens/blob/main/media/About%20Us%20Wireframe%20Mobile.JPG)
        </details>
Blog<details>
        ![Wireframe](https://github.com/Damhan91/Reef-Gardens/blob/main/readme%20images/Blog%20Desktop.JPG)
        ![Wireframe](https://github.com/Damhan91/Reef-Gardens/blob/main/readme%20images/Blog%20mobile.JPG)
        </details>
All Products<details>
        ![Wireframe](https://github.com/Damhan91/Reef-Gardens/blob/main/media/Wireframe%20All%20Products%20Desktop.JPG)
        ![Wireframe](https://github.com/Damhan91/Reef-Gardens/blob/main/media/Wireframe%20All%20Products%20Mobile.JPG)
        </details>
Product Details<details>
        ![Wireframe](https://github.com/Damhan91/Reef-Gardens/blob/main/media/Product%20Detail%20Desktop.JPG)
        ![Wireframe](https://github.com/Damhan91/Reef-Gardens/blob/main/media/Product%20Detail%20Mobile.JPG)
        </details>
Login<details>
        ![Wireframe](https://github.com/Damhan91/Reef-Gardens/blob/main/media/Login%20Desktop.JPG)
        ![Wireframe](https://github.com/Damhan91/Reef-Gardens/blob/main/media/Login%20Mobile.JPG)
        </details>
Register<details>
        ![Wireframe](https://github.com/Damhan91/Reef-Gardens/blob/main/media/Register%20Desktop.JPG)
        ![Wireframe](https://github.com/Damhan91/Reef-Gardens/blob/main/media/Register%20Mobile.JPG)
        </details>
Profile<details>
        ![Wireframe](https://github.com/Damhan91/Reef-Gardens/blob/main/media/Profile%20Desktop.JPG)
        ![Wireframe](https://github.com/Damhan91/Reef-Gardens/blob/main/media/Profile%20Mobile.JPG)
        </details>
Add Products<details>
        ![Wireframe](https://github.com/Damhan91/Reef-Gardens/blob/main/media/Add%20Product%20Desktop.JPG)
        ![Wireframe](https://github.com/Damhan91/Reef-Gardens/blob/main/media/Add%20Product%20Mobile.JPG)
        </details>
Checkout<details>
        ![Wireframe](https://github.com/Damhan91/Reef-Gardens/blob/main/media/Checkout%20Desktop.JPG)
        ![Wireframe](https://github.com/Damhan91/Reef-Gardens/blob/main/media/Checkout%20Mobile.JPG)
        </details>
Bag<details>
        ![Wireframe](https://github.com/Damhan91/Reef-Gardens/blob/main/media/Bag%20Desktop.JPG)
        ![Wireframe](https://github.com/Damhan91/Reef-Gardens/blob/main/media/Bag%20Mobile.JPG)
        </details>

## Colour and Design
The colour and design is based on a very neutral but yet bright backgound, as I wanted the user to be not be distracted by colours in the background, rather their attention and focus to be on the products like the fish and corals. The onlt colour that I used was the balck banner that pointed out free shipping which I think is importnat afor a user to instantly see when coming onto the website
## Technology Used
HTML\
CSS\
JavaScript\
Python\
Django- main framework for project\
Pip3- install packages to python\
Git- version control\
GitHub\
Gitpod\
Heroku\
Crispy forms\
Stripe\
AWS\
Bootstrap\
Font Awesome

## Data Model
Data Model <details>  
  ![datamodel](https://github.com/Damhan91/Reef-Gardens/blob/main/readme%20images/data%20model.JPG)  
        </details>
## Testing
Testing has been done manually throughout this website. All the features in the site have gone through testing on both desktop and mobile version.

* Product Assortment: AAll the products appear as expected with the correct price and nname showing
  ![Wireframe](https://github.com/Damhan91/Reef-Gardens/blob/main/readme%20images/testingproducts.JPG)
* Product Details: All the product details are showing correctly. The correct price and product descrption are showing for each product
  ![Wireframe](https://github.com/Damhan91/Reef-Gardens/blob/main/readme%20images/testingproduct.JPG)
* Product Reviews: The product reviews are showing correctly. With the correct user name and date appearing
  ![Wireframe](https://github.com/Damhan91/Reef-Gardens/blob/main/readme%20images/product%20reviews.JPG)
* Search bar:  The search bar is working and is showing the products that contain the searched word.
  ![Wireframe](https://github.com/Damhan91/Reef-Gardens/blob/main/readme%20images/testing%20search.JPG)
* Products: All filters on the product pages work as expected. Products can also be delted and update by the super user only (as expected) and not by a site user.
  ![Wireframe](https://github.com/Damhan91/Reef-Gardens/blob/main/readme%20images/testing%20sorting.JPG)
* Navigation bar: All the links to all products, fish, coral and about us work correctly. All items are categorised and are appearing in the correct tab. The tabs also condense in mobile format, and the links also work in that format.
 ![Wireframe](https://github.com/Damhan91/Reef-Gardens/blob/main/readme%20images/Nav%20testing.JPG)
* Add item to Bag: Each product gives the user an aoption to add the item to their bag
 ![Wireframe](https://github.com/Damhan91/Reef-Gardens/blob/main/readme%20images/add%20to%20bag.JPG)
* View contents of bag: Once a user adds the product to their bag, they can view the contents of the bag and make adjsutments where needed, either with the qty or remove the item all together
 ![Wireframe](https://github.com/Damhan91/Reef-Gardens/blob/main/readme%20images/add%20to%20bag%201.JPG)
* Checkout: The user can perfrom a checkout and pay for their products that have chosen to purchase.
  ![Wireframe](https://github.com/Damhan91/Reef-Gardens/blob/main/readme%20images/checkout.JPG)
* Register: The user can register for an account so they can get addtional features of the website.
  ![Wireframe](https://github.com/Damhan91/Reef-Gardens/blob/main/readme%20images/Sign%20up.JPG)
* Login: THe user can log in to then use the features reserved for signed up members
  ![Wireframe](https://github.com/Damhan91/Reef-Gardens/blob/main/readme%20images/Sign%20In.JPG)
* Logged in: The user is notified when they are logged in.
  ![Wireframe](https://github.com/Damhan91/Reef-Gardens/blob/main/readme%20images/logged%20in.JPG)
* Logout: The user can log out of their account incase they do not wish to be kept logged in.
  ![Wireframe](https://github.com/Damhan91/Reef-Gardens/blob/main/readme%20images/Sign%20out.JPG)
* Reviews: A registered user can leave a review under the products
  ![Wireframe](https://github.com/Damhan91/Reef-Gardens/blob/main/readme%20images/add%20review.JPG)
* Edit reviews: A registered user can edit or delete their own comments
  ![Wireframe](https://github.com/Damhan91/Reef-Gardens/blob/main/readme%20images/Edit%20review.JPG)
* Worng User: If a user tries to edit someones elses comment they are redirected to the home page and shown an error
  ![Wireframe](https://github.com/Damhan91/Reef-Gardens/blob/main/readme%20images/edit%20comment.JPG)
* My profile: A registered user can update their infomration and also check their order history
  ![Wireframe](https://github.com/Damhan91/Reef-Gardens/blob/main/readme%20images/account.JPG)
* Contact Us: The user can submit any question they may have to admin
  ![Wireframe](https://github.com/Damhan91/Reef-Gardens/blob/main/readme%20images/contact%20us.JPG)
* As the admin I can manage user accounts so that any required changes to them can be made.
 ![Wireframe](https://github.com/Damhan91/Reef-Gardens/blob/main/readme%20images/admin%20usewrs.JPG)
* As the admin I can view messages submitted via the contact us section so that I may look intot and action anything that is needed.
 ![Wireframe](https://github.com/Damhan91/Reef-Gardens/blob/main/readme%20images/admin%20contact%20us.JPG)
* As a site admin I can manage the content on the blog section and create or delete any that are needed.
 ![Wireframe](https://github.com/Damhan91/Reef-Gardens/blob/main/readme%20images/adming%20blog.JPG)
* As a site admin I can manage the reviews section from either the admin or website
  ![Wireframe](https://github.com/Damhan91/Reef-Gardens/blob/main/readme%20images/admin%20reviews.JPG)
* As a site admin I can manage the products of the store.
  ![Wireframe](https://github.com/Damhan91/Reef-Gardens/blob/main/readme%20images/admin%20products.JPG)


### Css testing

Static Css<details>  
  ![CSS](https://github.com/Damhan91/Reef-Gardens/blob/main/readme%20images/base.css%20test.JPG)  
        </details>

Profile Css<details>    
  ![CSS](https://github.com/Damhan91/Reef-Gardens/blob/main/readme%20images/Profile.css%20test.JPG)
        </details>
        
Checkout Css Css<details> 
  ![CSS](https://github.com/Damhan91/Reef-Gardens/blob/main/readme%20images/Checkout.css%20test.JPG)
        </details>     
        
### Js testing

Js <details>  
  ![CSS](https://github.com/Damhan91/Reef-Gardens/blob/main/readme%20images/JS%20test.JPG)  
        </details>

Country Field Js<details>    
  ![CSS](https://github.com/Damhan91/Reef-Gardens/blob/main/readme%20images/countryfiled.js%20test.JPG)  
        </details>


### PEP8 testing
All the PEP8 testing passed, with just a few python lines being to long. All secreen shots can be founf here [Here](https://github.com/Damhan91/Reef-Gardens/tree/main/readme%20images)

### Validator w3
About Us <details>  
  ![HTML](https://github.com/Damhan91/Reef-Gardens/blob/main/readme%20images/About%20Us.JPG)  
        </details>

Corals <details>    
  ![Html](https://github.com/Damhan91/Reef-Gardens/blob/main/readme%20images/Corals.JPG)  
        </details>
Fish <details>  
  ![Html](https://github.com/Damhan91/Reef-Gardens/blob/main/readme%20images/fish.JPG)  
        </details>

Home<details>    
  ![Html](https://github.com/Damhan91/Reef-Gardens/blob/main/readme%20images/Home.JPG)  
        </details>
Login <details>  
  ![Html](https://github.com/Damhan91/Reef-Gardens/blob/main/readme%20images/login.JPG)  
        </details>

Products<details>    
  ![Html](https://github.com/Damhan91/Reef-Gardens/blob/main/readme%20images/Products.JPG)  
        </details>
Register <details>  
  ![Html](https://github.com/Damhan91/Reef-Gardens/blob/main/readme%20images/Register.JPG)  
        </details>
## Deployment


**Gitpod**
* Create new repository from CI template
* Install Django and required libaries into Gitpod workspace
* Create new Django project called "Reef Gardens"
* Create procfile as required
* Run "pip3 freeze --local > requirements.txt" to update requirements file
* Ensure all required files up-to-date and that application is working
* Run "pip3 freeze --local > requirements.txt" to update requirements file
* Ensure "DEBUG = False" set in settings.py
* Perform commit and push to GitHub

**Heroku**

This application has been deployed from Github using Heroku.

* Create an account at heroku.com.
* Create a new app, add app name and your region.
* Click on create app.
* Go to "Settings".
* Under Config Vars, add your sensitive data (creds.json for example).
* For this project, I set buildpacks to and in that order.
* Go to "Deploy" and at "Deployment method", click on "Connect to Github".
* Enter your repository name and click on it when it shows below.
* Choose the branch you want to buid your app from.

**AWS**

The deployed website has static and media files. These are hosted using Amazon Web Services (AWS)

* Create an account at aws.amazon.com.
* Navigate to the IAM application and create a user and group.
* Set the AmazonS3FullAccess for the user and copy the AWS ACCESS and SECRET keys as config vars to your workspace and deployment environment.
* Create a new Bucket within the S3 application with an appropriate name.
* Enable public access for your bucket so users can access and use the services on your website (upload, view, download, etc).
## Credits
I had no data on the images for I taken the images from my local aquarium store link below.

https://www.seahorseaquariums.com/store/ 

I would also like to thank everyone at code institute from my mentor to the tutuor support and people on slack. They have been a great support to me over this project 
